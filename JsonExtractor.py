import json

class Extractor:
    
    def getChampionName(data):
        for element in data["data"]:
            p = data["data"][element]["name"]
            return p
