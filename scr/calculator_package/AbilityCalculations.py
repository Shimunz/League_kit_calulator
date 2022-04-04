
class AbilityCalculations:

    #reads the ability list of a champion
    def ability_check(data, name):
        ability_list = [] 
        for i in data[name]["Abilities"]:
            ability_list.append(i)
        return ability_list

    #Reads Abliity values and use to calculate
    def ability_part(data, name, ls):
        for part in ls:
            if(part=="Base_Damage"):
                values = data[name]["Values"]
                damage_type = data[name]["Type"]

            if(part=="CD"):
                cd = data[name]["CD"]

            if(part=="CC"):
                cc_type = data[name]["Type"]
                cc_duration = data[name]["Duration"]
            
            if(part=="Scaling"):
                scaling_type = data[name]["Type"]
                scaling_values = data[name]["Values"]
            
            if(part=="Cast_Time"):
                cast_time = data[name]["Cast_Time"]

            if(part=="Range"):
                cast_time = data[name]["Range"]

            if(part=="Radius"):
                cast_time = data[name]["Radius"]

            if(part=="Counters"):
                cast_time = data[name]["Counters"]
            
            if(part=="Type"):
                cast_time = data[name]["Type"]