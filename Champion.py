
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
        self.baseHP = baseHP
        self.hpPerLevel = hpPerLevel
        self.hpRegenPerLevel = hpRegenPerLevel
        self.baseDamage = baseDamage
        self.damagePerLevel = damagePerLevel
        self.baseArmor = baseArmor
        self.armorPerLevel= armorPerLevel
        self.baseSpellBlock = baseSpellBlock
        self.spellBlockPerLevel = spellBlockPerLevel
        self.baseMoveSpeed = baseMoveSpeed
        self.attackRange = attackRange
        self.attackSpeed = attackSpeed
        self.attackSpeedRatio = attackSpeedRatio
        self.attackSpeedPerLevel = attackSpeedPerLevel

class Abilities:
    def __init__(self, ability_name, AbilityType, CD):
        self.ability_name = ability_name
        self.AbilityType = AbilityType
        self.CD = CD

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)
    

