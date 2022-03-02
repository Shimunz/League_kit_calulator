
from calculator_package.Calculations import *
from champion_package.AbilityType import *
from champion_package.Champion import *
from patch_updater_package.JsonExtractor import *
from patch_updater_package.PatchUpdate import *
from calculator_package.Points import *

def update():
    PatchUpdate.getAllLastestVersion()
    dd_patch_number = PatchUpdate.getLatestPatch()
    cc_patch_number = Misc.ddToCcPatchNo(dd_patch_number)
    PatchUpdate.getAllLastestChampionNames(dd_patch_number)
    all_champion_name_list = PatchUpdate.getAllLocalChampionNames()
    all_champion_name_list_alpha = Misc.aplhaOnly(all_champion_name_list)
    print(all_champion_name_list)
    PatchUpdate.updateAllChampions(cc_patch_number, all_champion_name_list)

#update()

all_champion_name_list = PatchUpdate.getAllLocalChampionNames()

all_champions = []

for champ in all_champion_name_list:
    c_base_stats = Extractor.getBaseStats(champ)
    abilities = AbilityType(0, 0, 0, 0)
    total_stats = Calculations.calculateBaseStats(c_base_stats, 18)
    champion = Champion(champ, c_base_stats, abilities, total_stats)
    all_champions.append(champion)

arr = []

for champ in all_champions:
    hp = champ.champion_properties['stats'].total_stats['hp']

    arr.append(hp)
    
arr.sort()

p = Points()

i = Calculations.calculatePoints(arr)
p.points_properties['hp'] = i

#c_base_stats = Extractor.getBaseStats("aatrox")

#total_stats = Calculations.calculateBaseStats(c_base_stats, 18)

#print(aatrox.champion_properties['stats'].total_stats['attackSpeed'])

print("done")




#all_champion_list = []
"""
for champ in all_champion_name_list:
    location = 'Patch/'+patch_number+'/data/champion/'+champ+".json"
    data = Misc.getData(location)

    champion_name = Extractor.getChampionName(data)
    champion_stats = Extractor.getChampionStats(data, champion_name)

    name = Champion(champion_name, champion_stats, "")

    all_champion_list.append(name)

print("done")
"""
#result = Misc.getJsonWeb("https://raw.communitydragon.org/12.3/game/data/characters/aatrox/aatrox.bin.json")
#PatchUpdate.updateChampion(cc_patch_number, "aatrox")
#print ("done")


#champion_name = Extractor.getChampionName(fdata)
#print(champion_name)

#champion_stats = Extractor.getChampionStats(fdata, champion_name)
#print(champion_stats)

#name = Champion(champion_name, champion_stats, "")
#print(name)



# f = open("Test.txt")

# while (True):
#     line = f.readline()
#     if(line != ""):``
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
