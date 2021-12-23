import json
from Champion import Abilities, Champion
from AbilityType import *
from JsonExtractor import *

f = open('Aatrox.json')
fdata = json.load(f)

champion_name = Extractor.getChampionName(fdata)
print(champion_name)

champion_stats = Extractor.getChampionStats(fdata, champion_name)
print(champion_stats)

# f = open("Test.txt")

# while (True):
#     line = f.readline()
#     if(line != ""):
#         print(line)
#     else:
#         break


# def reader(line):
#     return line

# ability_properties = []
# ab_list = []

# a = AbilityType("AP", [55,95,135,175,215], 0.6, 12)
# b = AbilityType("AD", [5,9,13,17,21], 1, 12)

# ability_properties.append(a)
# ability_properties.append(b)

# ablity = Abilities("soul", ability_properties, 10)
# ab_list.append(ablity)

# ability_properties.clear()

# a = AbilityType("AD", [10,20,30,40,50], 0.7, 0)

# ability_properties.append(a)

# ablity = Abilities("ass", ability_properties, 5)
# ab_list.append(ablity)

# base_stats = [500, 40, 40, 70, 0, 330, 0] #health, ar, mr, ad, ap, speed tenacity

# nasus = Champion("nasus", base_stats, ab_list)


# print(nasus.champion_name, nasus.base_stats, nasus.abilities)

# for x in range(len(nasus.abilities)):
#     print(nasus.abilities[x])