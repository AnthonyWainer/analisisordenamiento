import json

def readFile(nombre):
    with open(nombre+'.json') as f:
        d = json.load(f)
    return d


