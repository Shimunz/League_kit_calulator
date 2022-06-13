class Abilities:
    def __init__(self, ability_name, AbilityType, CD):
        self.ability_name = ability_name
        self.AbilityType = AbilityType
        self.CD = CD

    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)