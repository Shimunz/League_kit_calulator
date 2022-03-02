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
    
    #Redundant code
    def getAllChampionNames(patch_no):
        data = Misc.getJsonWeb("http://ddragon.leagueoflegends.com/cdn/" + patch_no + "/data/en_US/champion.json")
        champion_names_list = []

        for i in data["data"]:
            champion_names_list.append(i)

        return champion_names_list
    
    def getBaseStats(name):
        path = pathlib.Path(__file__).parent.parent.parent.joinpath("Patch/12.4/game/data/characters/" + name + "/" + name + ".json")
        data = Misc.getData(path)
        '''
        ename = Misc.checkExtractorName(name)
        if (name==ename):
            ename = Misc.capFistLetter(name)
        
        
        elif(ename == 'Jarvaniv'):
            ename = 'JarvanIV'
        elif(ename == 'Leesin'):
            ename = 'LeeSin'
        '''
        if (name == 'Fiddlesticks'):
            name = 'FiddleSticks'

        data_location = "Characters/" + name +"/CharacterRecords/Root"

        if (name == 'Renata'):
            data_location = "{541edaee}"

        if (name == 'Kled'):
            baseHP = data[data_location]["baseHP"] + 450
        else:
            baseHP = data[data_location]["baseHP"]
        hpPerLevel = data[data_location]["hpPerLevel"]
        hpRegenPerLevel = data[data_location]["hpRegenPerLevel"]
        baseDamage = data[data_location]["baseDamage"]
        if (name != 'Senna'):
            damagePerLevel = data[data_location]["damagePerLevel"]
        else:
            damagePerLevel = 0
        
        baseArmor = data[data_location]["baseArmor"]

        if (name != 'Thresh'):
            armorPerLevel = data[data_location]["armorPerLevel"]
        else:
             armorPerLevel = 0

        baseSpellBlock = data[data_location]["baseSpellBlock"]
        spellBlockPerLevel = data[data_location]["spellBlockPerLevel"]
        baseMoveSpeed = data[data_location]["baseMoveSpeed"]
        attackRange = data[data_location]["attackRange"]
        attackSpeed = data[data_location]["attackSpeed"]
        attackSpeedRatio = data[data_location]["attackSpeedRatio"]

        if (name != 'Jhin'):
            attackSpeedPerLevel = data[data_location]["attackSpeedPerLevel"]
        else:
            attackSpeedPerLevel = 0
                
        champ_stats = BaseStats(baseHP, hpPerLevel, hpRegenPerLevel, baseDamage, damagePerLevel, baseArmor, armorPerLevel, baseSpellBlock, spellBlockPerLevel, baseMoveSpeed, attackRange, attackSpeed, attackSpeedRatio, attackSpeedPerLevel)

        return champ_stats