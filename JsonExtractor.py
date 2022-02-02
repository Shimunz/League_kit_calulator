from FileOpener import *

class Extractor:
    
    def getChampionName(data):
        for element in data["data"]:
            result = data["data"][element]["name"]
            return result

    def getChampionStats(data, name):
        result = data["data"][name]["stats"]
        return result

    def getAllChampionNames(patch_no):
        file_location = 'Patch/' + patch_no +'/data/champion.json'
        data = FileOpener.getData(file_location) 

        champion_names_list = []

        for i in data["data"]:
            champion_names_list.append(i)

        return champion_names_list