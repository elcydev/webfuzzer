

def parser_wordlist(filepath: str):
  wordlists = []
  try:
    with open(filepath, 'r') as f:
      for chunk in readChunks(f):
        for x in chunk.split():
          wordlists.append(x)

  except Exception:
    pass
  return wordlists

def readChunks(fileObj, chunkSize=2048):
  while True:
    data = fileObj.read(chunkSize)
    if not data: 
      break
    yield data