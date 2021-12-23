class Extractor:
    
    def getChampionName(data):
        for element in data["data"]:
            result = data["data"][element]["name"]
            return result

    def getChampionStats(data, name):
        result = data["data"][name]["stats"]
        return result
