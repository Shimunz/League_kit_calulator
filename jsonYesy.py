import json
from types import SimpleNamespace

f = open('Aatrox.json')
fdata = json.load(f)

print(fdata["data"]["Aatrox"]["stats"])

for element in fdata["data"]:
    p = fdata["data"][element]["name"]
    print(p)