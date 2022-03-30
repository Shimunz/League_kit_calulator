
class AbilityCalculations:

    def ability_check(data, name):
        ability_list = [] 
        for i in data[name]["Abilities"]:
            ability_list.append(i)
        return ability_list

    