class Damage:
    def __init__(self, damage_type, base_damage, scaling, CD):
        self.damage_type = damage_type
        self.base_damage = base_damage
        self.scaling = scaling
        if(CD == 0):    #Internal cooldown 
            self.CD = None  
        else:
            self.CD = CD  
    
