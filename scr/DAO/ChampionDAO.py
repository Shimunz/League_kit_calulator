from patch_updater_package.PatchUpdate import *
from patch_updater_package.JsonExtractor import *
from champion_package.AbilityType import *
from calculator_package.Calculations import *
from champion_package.Champion import *
from patch_updater_package.PatchDAO import *

class ChampionDAO:
    all_champion_names = PatchUpdate.getAllLocalChampionNames()
    champion_list = []

    def getAllChampionNames():
        return PatchUpdate.getAllLocalChampionNames

    def getAllChampionStats(name_list):
        champion_list = []

        for champ in name_list:
            c_base_stats = Extractor.getBaseStats(champ, PatchDAO.cc_patch_number)
            abilities = AbilityType(0, 0, 0, 0)
            total_stats = Calculations.calculateBaseStats(c_base_stats, 18)
            champion = Champion(champ, c_base_stats, abilities, total_stats)
            champion_list.append(champion)
        
        return champion_list

    