
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

class Abilities:
    def __init__(self, ability_name, AbilityType, CD):
        self.ability_name = ability_name
        self.AbilityType = AbilityType
        self.CD = CD

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)
    

