class Champion:

    def __init__(self) -> None:
        pass

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    

    def Abillties ():
    # def __init__(self, ability_name, Damage):
    #     self.ability_name = ability_name
    #     self.Damage = Damage
        pass

    def Damage():
    # def __init__(self, damage_type, base_damage, scaling, CD):
    #     self.damage_type = damage_type
    #     self.base_damage = base_damage
    #     self.scaling = scaling
    #     self.CD = CD 
        pass



class Abilities:
    def __init__(self, ability_name, AbilityType, CD):
        self.ability_name = ability_name
        self.AbilityType = AbilityType
        self.CD = CD

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
    

