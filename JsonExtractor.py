from Misc import *

class Extractor:
    
    def getChampionName(data):
        for element in data["data"]:
            result = data["data"][element]["name"]
            return result

    def getChampionStats(data, bname):
        result = data["data"][name]["stats"]
        return result

    def getAllChampionNames(patch_no):
        data = Misc.getJsonWeb("http://ddragon.leagueoflegends.com/cdn/" + patch_no + "/data/en_US/champion.json")
        champion_names_list = []

        for i in data["data"]:
            champion_names_list.append(i)

        return champion_names_list