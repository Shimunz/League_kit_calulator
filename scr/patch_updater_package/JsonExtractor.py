import pathlib
from champion_package.Champion import *
from patch_updater_package.Misc import *

class Extractor:
    
    def getChampionName(data):
        for element in data["data"]:
            result = data["data"][element]["name"]
            return result

    def getChampionStats(data, bname):
        result = data["data"][bname]["stats"]
        return result

    def getAllChampionNames(patch_no):
        data = Misc.getJsonWeb("http://ddragon.leagueoflegends.com/cdn/" + patch_no + "/data/en_US/champion.json")
        champion_names_list = []

        for i in data["data"]:
            champion_names_list.append(i)

        return champion_names_list
    
    def getBaseStats(name):
        path = pathlib.Path(__file__).parent.parent.parent.joinpath("Patch/12.4/game/data/characters/" + name + "/" + name + ".json")
        data = Misc.getData(path)
        ename = Misc.checkExtractorName(name)
        if (name==ename):
            ename = Misc.capFistLetter(name)

        data_location = "Characters/" + ename +"/CharacterRecords/Root"

        baseHP = data[data_location]["baseHP"]
        hpPerLevel = data[data_location]["hpPerLevel"]
        hpRegenPerLevel = data[data_location]["hpRegenPerLevel"]
        baseDamage = data[data_location]["baseDamage"]
        damagePerLevel = data[data_location]["damagePerLevel"]
        baseArmor = data[data_location]["baseArmor"]
        armorPerLevel = data[data_location]["armorPerLevel"]
        baseSpellBlock = data[data_location]["baseSpellBlock"]
        spellBlockPerLevel = data[data_location]["spellBlockPerLevel"]
        baseMoveSpeed = data[data_location]["baseMoveSpeed"]
        attackRange = data[data_location]["attackRange"]
        attackSpeed = data[data_location]["attackSpeed"]
        attackSpeedRatio = data[data_location]["attackSpeedRatio"]
        attackSpeedPerLevel = data[data_location]["attackSpeedPerLevel"]
                
        champ_stats = BaseStats(baseHP, hpPerLevel, hpRegenPerLevel, baseDamage, damagePerLevel, baseArmor, armorPerLevel, baseSpellBlock, spellBlockPerLevel, baseMoveSpeed, attackRange, attackSpeed, attackSpeedRatio, attackSpeedPerLevel)

        return champ_stats