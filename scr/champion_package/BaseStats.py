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