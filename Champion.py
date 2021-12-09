class Champion:

    def __init__(self, champion_name, base_stats, abilities):
        self.champion_name = champion_name
        self.base_stats = base_stats
        self.abilities = abilities

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Abilities:
    def __init__(self, ability_name, AbilityType, CD):
        self.ability_name = ability_name
        self.AbilityType = AbilityType
        self.CD = CD

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)
    

