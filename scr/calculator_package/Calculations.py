import numpy as np
from champion_package.Champion import Stats


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
    
    def calculateBaseStats(base_stats, lvl):
        result = Stats()
        result.total_stats['lvl'] = lvl
        result.total_stats['baseHp'] = base_stats['baseHP']
        result.total_stats['hp'] = base_stats['baseHP'] + (base_stats['hpPerLevel'] * lvl)
        result.total_stats['baseAD'] = base_stats['baseDamage'] + (base_stats['damagePerLevel'] * lvl)
        result.total_stats['baseArmour'] = base_stats['baseArmor'] + (base_stats['armorPerLevel'] * lvl)
        result.total_stats['baseMR'] = base_stats['baseSpellBlock'] + (base_stats['spellBlockPerLevel'] * lvl)
        result.total_stats['attackSpeed'] = (base_stats['attackSpeedRatio'] * base_stats['attackSpeed']) + (base_stats['attackSpeedPerLevel'] * lvl)
        result.total_stats['attakRange'] = base_stats['attackRange']
        return result

    def calculatePoints(a):
        i = []
        n = 20
        arr = np.array(a)

        while (n < 100):
            p = np.percentile(arr, n)
            i.append(p)
            n += 20
        
        return i
