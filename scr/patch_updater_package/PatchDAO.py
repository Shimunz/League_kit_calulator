from patch_updater_package.JsonExtractor import *
from patch_updater_package.PatchUpdate import *
from patch_updater_package.Extra import *

class PatchDAO:
    
    dd_patch_number = PatchUpdate.getLatestPatch()
    cc_patch_number = Extra.ddToCcPatchNo(dd_patch_number)

    def update():
        PatchUpdate.getAllLastestVersion()
        dd_patch_number = PatchUpdate.getLatestPatch()
        cc_patch_number = Extra.ddToCcPatchNo(dd_patch_number)
        PatchUpdate.getAllLastestChampionNames(dd_patch_number)
        all_champion_name_list = PatchUpdate.getAllLocalChampionNames()
        all_champion_name_list_alpha = Extra.aplhaOnly(all_champion_name_list)
        print(all_champion_name_list)
        PatchUpdate.updateAllChampions(
            cc_patch_number, all_champion_name_list_alpha)