class Champion:
    def __init__(self, champion_name, base_stats, abilities, stats):
        self.champion_properties = {
            'champion_name' : champion_name,
            'base_stats' : base_stats,
            'abilities' : abilities,
            'items' : None,
            'stats' : stats,
            'pointStats' : None
        }
        
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __getitem__(self,key):
        return self.champion_properties[key]

    def __setitem__(self, key, value):
        self.base_stats_properties[key] = value

    def getChampionName(self):
        return self.__getitem__("champion_name")
    