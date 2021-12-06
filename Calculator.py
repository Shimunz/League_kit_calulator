from Champion import Abilities, Champion
from AbilityType import *

# f = open("Test.txt")

# while (True):
#     line = f.readline()
#     if(line != ""):
#         print(line)
#     else:
#         break


# def reader(line):
#     return line


e = AbilityType("AP", [55,95,135,175,215], 0.6, 12)
ablity = Abilities("soul", e, 10)

print(e.base_numbers, e.CD)
print(ablity.ability_name, ablity.AbilityType.base_numbers, ablity.AbilityType.scaling, ablity.CD)