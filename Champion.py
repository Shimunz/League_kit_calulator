
class Champion:
    def __init__(self, champion_name, base_stats, abilities):
        self.champion_properties = {
            'champion_name' : champion_name,
            'base_stats' : base_stats,
            'abilities' : abilities
        }
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __getitem__(self,key):
        return self.champion_properties[key]

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

class Abilities:
    def __init__(self, ability_name, AbilityType, CD):
        self.ability_name = ability_name
        self.AbilityType = AbilityType
        self.CD = CD

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)
    

