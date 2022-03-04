
class Champion:
    def __init__(self, champion_name, base_stats, abilities, stats):
        self.champion_properties = {
            'champion_name' : champion_name,
            'base_stats' : base_stats,
            'abilities' : abilities,
            'items' : None,
            'stats' : stats,
            'pointStats' : PointStats()
        }
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __getitem__(self,key):
        return self.champion_properties[key]

    def __setitem__(self, key, value):
        self.base_stats_properties[key] = value

    def getChampionName(self):
        return self.__getitem__("champion_name")

class BaseStats:
    def __init__(self, baseHP, hpPerLevel, hpRegenPerLevel, baseDamage, damagePerLevel, baseArmor, armorPerLevel, baseSpellBlock, spellBlockPerLevel, baseMoveSpeed, attackRange, attackSpeed, attackSpeedRatio, attackSpeedPerLevel):
        self.base_stats_properties = {
            "baseHP" : baseHP,
            'hpPerLevel' : hpPerLevel,
            'hpRegenPerLevel' : hpRegenPerLevel,
            'baseDamage' : baseDamage,
            'damagePerLevel' : damagePerLevel,
            'baseArmor' : baseArmor,
            'armorPerLevel': armorPerLevel,
            'baseSpellBlock' : baseSpellBlock,
            'spellBlockPerLevel' : spellBlockPerLevel,
            'baseMoveSpeed' : baseMoveSpeed,
            'attackRange' : attackRange,
            'attackSpeed' : attackSpeed,
            'attackSpeedRatio' : attackSpeedRatio,
            'attackSpeedPerLevel' : attackSpeedPerLevel
        }        
    
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __getitem__(self,key):
        return self.base_stats_properties[key]

    def __setitem__(self, key, value):
        self.base_stats_properties[key] = value
    
    def getBaseStat(self, key):
        return self.__getitem__(key)

class Abilities:
    def __init__(self, ability_name, AbilityType, CD):
        self.ability_name = ability_name
        self.AbilityType = AbilityType
        self.CD = CD

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)
    
class Stats:
    def __init__(self):
        self.total_stats = {
            'hp' : 0,
            'bonusHp' : 0,
            'baseHp': 0,
            'baseAD' : 0,
            'bonusAD' : 0,
            'AP': 0,
            'baseArmour' : 0,
            'bonusArmour' : 0,
            'baseMR' : 0,
            'bonusMR' : 0,
            'attackSpeed' : 0,
            'attackRange' : 0,
            'critDamage' : 0,
            'critChance' : 0
        }

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)

    def __getitem__(self,key):
        return self.total_stats[key]

    def calculateInitalStats(self, base_stats, lvl):
        self.total_stats['lvl'] = lvl
        pass

class PointStats:
    def __init__(self):
        self.point_stats = {
            'lvl' : 0,
            'hp' : 0,
            'bonusHp' : 0,
            'baseHp': 0,
            'baseAD' : 0,
            'bonusAD' : 0,
            'AP': 0,
            'baseArmour' : 0,
            'bonusArmour' : 0,
            'baseMR' : 0,
            'bonusMR' : 0,
            'attackSpeed' : 0,
            'attackRange' : 0,
            'critDamage' : 0,
            'critChance' : 0
        }

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)

    def __getitem__(self,key):
        return self.total_stats[key]

    def calculateInitalStats(self, base_stats, lvl):
        self.total_stats['lvl'] = lvl
        pass