from Champion import Champion
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

print(e.base_damage, e.CD)