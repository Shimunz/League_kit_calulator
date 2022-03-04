
class Points:

    def __init__(self):
        self.points_properties={
            'hp' : [],
            'bonusHp' : [],
            'baseHp': [],
            'baseAD' : [],
            'bonusAD' : [],
            'AP': [],
            'baseArmour' : [],
            'bonusArmour' : [],
            'baseMR' : [],
            'bonusMR' : [],
            'attackSpeed' : [],
            'attackRange' : [],
            'critDamage' : [],
            'critChance' : []
        }

    def __getitem__(self,key):
        return self.points_properties[key]

    def __setitem__(self, key, value):
        self.points_properties[key] = value

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)