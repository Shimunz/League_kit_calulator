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