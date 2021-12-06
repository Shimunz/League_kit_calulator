class Damage:
    def __init__(self, damage_type, base_damage, scaling, CD):
        self.damage_type = damage_type
        self.base_damage = base_damage
        self.scaling = scaling
        self.CD = CD 
    
    # def setBaseDamage(self, base_damage):
    #     self.base_damage = base_damage

    # def getBaseDamage(self):
    #     return self.base_damage

    # def setDamageType(self, damage_type):
    #     self.damage_type = damage_type

    # def getDamageType(self):
    #     return self.damage_type

    # def setScaling(self, scaling):
    #     self.scaling = scaling

    # def getScaling(self):
    #     return self.scaling

    # def setScaling(self, CD):
    #     self.CD = CD

    # def getScaling(self):
    #     return self.CD