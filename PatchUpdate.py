from asyncio.windows_events import NULL
from cgitb import reset
import json
from msilib.schema import Patch
import os
from unittest import result
from Misc import *

from Misc import *

class PatchUpdate:

    def getLatestPatch():
        url = 'https://ddragon.leagueoflegends.com/api/versions.json'
        result = Misc.getJsonWeb(url)
        for i in result:
            return i
        return NULL

    def getPatch(patch_no):
        url = "https://raw.communitydragon.org/" + patch_no

    def updateAllChampions(patch_no, champ_list):
        for champ in champ_list:
            PatchUpdate.updateChampion(patch_no, champ)

    def updateChampion(patch_no, champ_name):
        url = "https://raw.communitydragon.org/" + patch_no + "/game/data/characters/" + champ_name + "/" + champ_name + ".bin.json"
        Misc.createDir(patch_no)
        data = Misc.getJsonWeb(url)

        dir = "Patch/" + patch_no + "/game/data/characters/" + champ_name + "/"
        isDir = os.path.isdir(dir)
        if not isDir:
            os.makedirs(dir)

        with open(dir + champ_name + ".json", 'w') as outfile:
            json.dump(data, outfile)
            print("Done: " + champ_name)


    

    
