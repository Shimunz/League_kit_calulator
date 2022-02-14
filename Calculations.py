from email.mime import base
from unittest import result


class Calculations:
    
    def getMaxHP(baseHP, HPPerLvl, bonusHP, lvl):
        result = baseHP + (HPPerLvl*lvl) + bonusHP
        return result

    def getTotalArmour(baseArmour, ArPerLvl, bonusArmour, lvl):
        result = baseArmour + (ArPerLvl*lvl) + bonusArmour
        return result
    
    def getTotalMR(baseMR, MRPerLvl, bonusMR, lvl):
        result = baseMR + (MRPerLvl*lvl) + bonusMR
        return result
    
    def getTotalMS(baseMS, bonusMS):
        result = baseMS + bonusMS
        return result
    
    def getTotalAD(baseAD, ADPerLvl, bonusAD, lvl):
        result = baseAD + (ADPerLvl*lvl), bonusAD
        return result
    
    def getTotalAP(baseAP, bonusAP):
        result = baseAP + bonusAP
        return result