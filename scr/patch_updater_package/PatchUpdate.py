import json
import os

from patch_updater_package.Extra import *


class PatchUpdate:

    #Gets the lastest patch version
    def getLatestPatch(): 
        result = PatchUpdate.getLocalVersions()
        for i in result:
            return i
    
    #Gets all versoin numbers off the web
    def getAllLastestVersion():
        url = 'https://ddragon.leagueoflegends.com/api/versions.json'
        result = Extra.getJsonWeb(url)
        with open("versions.json", 'w') as outfile:
            json.dump(result, outfile)
        return result

    def getLocalVersions():
        result = Extra.getData("versions.json")
        return result


    def getPatch(patch_no):
        url = "https://raw.communitydragon.org/" + patch_no

    def getAllLastestChampionNames(patch_no):
        data = Extra.getJsonWeb("http://ddragon.leagueoflegends.com/cdn/" + patch_no + "/data/en_US/champion.json")
        champion_names_list = []

        for i in data["data"]:
            champion_names_list.append(i)

        with open("champion_list.json", 'w') as outfile:
            json.dump(champion_names_list, outfile)

    def getAllLocalChampionNames():
        result = Extra.getData("champion_list.json")
        return result

    def updateAllChampions(patch_no, champ_list):
        for champ in champ_list:
            PatchUpdate.updateChampion(patch_no, champ)

    def updateChampion(patch_no, champ_name):
        url = "https://raw.communitydragon.org/" + patch_no + "/game/data/characters/" + champ_name + "/" + champ_name + ".bin.json"
        Extra.createDir(patch_no)
        data = Extra.getJsonWeb(url)

        dir = "Patch/" + patch_no + "/game/data/characters/" + champ_name + "/"
        isDir = os.path.isdir(dir)
        if not isDir:
            os.makedirs(dir)

        with open(dir + champ_name + ".json", 'w') as outfile:
            json.dump(data, outfile)
            print("Done: " + champ_name)


    

    
