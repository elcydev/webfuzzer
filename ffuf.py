import argparse
import urllib3
import requests
from core.models import GroupType, HTTPMethod, PluginType, SessionBaseModel
import concurrent.futures
from core.pluginmanager import PluginManager
from core.utils import parser_wordlist

parser = argparse.ArgumentParser(description='ffuf - web fuzzer modulado')

parser.add_argument('-u', dest="url", help='Define a URL para ataque', required=True)
parser.add_argument('-X', dest="method", help='Método HTTP a ser usado', default=HTTPMethod.GET.value)
parser.add_argument('-d', dest="data", help='Corpo do conteúdo da solicitação HTTP para o método POST', default="")
parser.add_argument('-t', dest="timeout", type=int, help='Duração do timeout da solicitação: o padrão é 10 s', default=10)
parser.add_argument('-w', dest="wordlist", help='Caminho do arquivo de lista de palavras', required=True)

pm = PluginManager(parser)

p = parser.parse_args()
wordlists = parser_wordlist(p.wordlist)

if not wordlists:
    exit("[*] A lista de palavras está vazia ou não foi encontrada")

sbms = [SessionBaseModel(p.url, line) for line in wordlists]

def ThreadRequestTask(sb: SessionBaseModel, pm: PluginManager, p: argparse.Namespace):
    response = None

    pm.setParserRequest(GroupType.INPUT, sb)

    if p.method == HTTPMethod.GET.value:
        try:
            response = requests.get(url=sb.getUrl, headers=sb.getHeaders, timeout=p.timeout)  
        except Exception as e:
            print(e)
    else:
        payload = p.data.encode('utf-8')  # Codifica o payload para bytes
        if 'Content-Type' not in sb.getHeaders.keys():
            sb.addHeaders('Content-Type', 'application/x-www-form-urlencoded')
        try:
            response = requests.post(url=sb.getUrl, 
                                     data=sb.getPayload,
                                     headers=sb.getHeaders, 
                                     timeout=p.timeout)
        except Exception as e:
            print(e)
    sb.setResponse(response)

    plugins_filters = pm.getPlugins(PluginType.FILTER)
    if any([p.checkNameSpace for p in plugins_filters if p.checkNameSpace]):
        if all([p.parserResponse(sb) for p in plugins_filters if p.checkNameSpace]):
            return "{} [{}]".format(sb.getUrl, sb.getResponse.status_code)
        return None
    return "{} [{}]".format(sb.getUrl, sb.getResponse.status_code)

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for sbm in sbms:
        futures.append(executor.submit(ThreadRequestTask, sb=sbm, pm=pm, p=p))
    for future in concurrent.futures.as_completed(futures):
            if future.result():
                print(future.result())
