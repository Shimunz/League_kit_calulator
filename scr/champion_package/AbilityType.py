class AbilityType:
    def __init__(self, ability_type, base_numbers, scaling, CD):
        self.ability_type = ability_type
        self.base_numbers = base_numbers
        self.scaling = scaling
        if(CD == 0):    #Internal cooldown 
            self.CD = None  
        else:
            self.CD = CD  


    def __str__(self):  #Print formatting
        return str(self.__class__) + ": " + str(self.__dict__)
    
