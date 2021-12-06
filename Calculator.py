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


a = AbilityType("AP", [55,95,135,175,215], 0.6, 12)

b = AbilityType("AD", [5,9,13,17,21], 1, 12)

ability_properties = []

ability_properties.append(a)
ability_properties.append(b)

ablity = Abilities("soul", ability_properties, 10)


print(a.base_numbers, a.CD)
print(ablity.ability_name, len(ablity.AbilityType), ablity.CD)

for x in range(len(ablity.AbilityType)):
    print(ability_properties[x])