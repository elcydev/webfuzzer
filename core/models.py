from enum import Enum
import requests

class GroupType(Enum):
    DEFAULT = "GENERAL"
    FILTERS = "Filters options"
    INPUT = "Input options"

class PluginType(Enum):
    PARSER = 0
    FILTER = 1

class HTTPMethod(Enum):
    GET = "GET"
    POST = "POST"

class SessionBaseModel(object):
    def __init__(self, url: str, variable: str, verbose: bool = False):
        self._prefix_val = variable
        self._url = url.replace("FUZZ", variable) if 'FUZZ' in url else url + variable
        self._verbose = verbose
        self._headers = {}
        self._payload = None
        self._response = None

    @property
    def getHeaders(self):
        return self._headers

    def parserFuzzReplace(self, data: str) -> str:
        return data.replace("FUZZ", self._prefix_val) if 'FUZZ' in data else data

    def addHeaders(self, key, value):
        value = self.parserFuzzReplace(value)
        self._headers[key] = value

    @property
    def getPayload(self):
        return self._payload

    def setPayload(self, data: str):
        self._payload = data

    @property
    def getUrl(self):
        return self._url

    def setUrl(self, url):
        self._url = url

    @property
    def getResponse(self):
        return self._response

    def setResponse(self, r: requests.Response):
        self._response = r

# Exemplo de uso:
url = "http://testphp.vulnweb.com/FUZZ"
variable = "example"
sb = SessionBaseModel(url, variable, verbose=True)

# Configurando cabeçalhos e payload
sb.addHeaders("User-Agent", "Mozilla/5.0")
sb.addHeaders("Accept", "text/html")
sb.setPayload("example_payload")

# Obtendo informações
print(sb.getHeaders)
if sb.getPayload and 'FUZZ' in sb.getPayload:
    print(sb.getPayload)
print(sb.getUrl)
