from Champion import Abilities, Champion
from Damage import *

# f = open("Test.txt")

# while (True):
#     line = f.readline()
#     if(line != ""):
#         print(line)
#     else:
#         break


# def reader(line):
#     return line


e = Damage("AP", [55,95,135,175,215], 0.6, 12)
ablity = Abilities("soul", e, 10)

print(e.base_damage, e.CD)
print(ablity.ability_name, ablity.Damage.base_damage, ablity.Damage.scaling, ablity.CD)