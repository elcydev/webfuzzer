<p align="center">
  <img src="logo.png" alt="WebFuzzer Logo" width="250">
</p>

<h1 align="center">WebFuzzer 🕷️</h1>
<p align="center">
  Um fuzzer modular e extensível para aplicações web, inspirado no ffuf.
</p>

---

## 🚀 Sobre o projeto

O **WebFuzzer** foi desenvolvido para facilitar o teste de diretórios e endpoints em aplicações web.  
Ele permite injetar palavras de uma wordlist em uma URL base, realizar requisições GET ou POST e aplicar filtros com plugins.

✅ Foco em modularidade  
✅ Suporte a plugins  
✅ Paralelismo com ThreadPoolExecutor  
✅ Cabeçalhos personalizados incluídos

---

## 🛠️ Funcionalidades

- Injeção de paths a partir de wordlists
- Suporte a métodos HTTP `GET` e `POST`
- Timeout customizável
- Headers personalizáveis (`User-Agent`, `Accept`, etc.)
- Filtros por status HTTP (ex: ignora 404)
- Estrutura orientada a plugins

---

## ⚙️ Parâmetros de uso

```bash
python ffuf.py -u <URL> -w <wordlist.txt> [opções]
