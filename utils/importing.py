import json

def import_json(path):
    f = open(path)
    data = json.load(f)
    f.close
    return data