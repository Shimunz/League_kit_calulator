import json
import requests
import os

class Misc:
    
    # Gets data from a .json file and returns that data
    # Takes in file location as input
    # Returns the .json data
    def getData(file_location):
        file = open(file_location, encoding='utf-8')
        data = json.load(file)
        return data

    def checkExtractorName(str):
        
        if(str=="Cho'Gath"):
            result = "Chogath"
            return result
        elif(str=='Dr. Mundo'):
            result = "DrMundo"
            return result
        elif(str=="Kai'Sa"):
            result = "Kaisa"
            return result
        elif(str=="Kha'Zix"):
            result = "Khazix"
            return result
        elif(str=="Kog'Maw"):
            result = "KogMaw"
            return result
        elif(str=='LeBlanc'):
            result = 'Leblanc'
            return result
        elif(str=='Wukong'):
            result = 'MonkeyKing'
            return result
        elif(str=='Nunu & Willump'):
            result = 'Nunu'
            return result
        elif(str=="Rek'Sai"):
            result = "RekSai"
            return result
        elif(str=="Vel'Koz"):
            result = "Velkoz"
            return result
        else:
            result = str.replace(" ","")
            result = result.replace(".","")
            return result

    def getJsonWeb(url):
        result = json.loads(requests.get(url).text)
        return result

    def createDir(dir):
        isDir = os.path.isdir("Patch/" + dir)
        if not isDir:
            os.makedirs("Patch/" + dir)
        else:
            print("Directory already existed : " + " Patch/" + dir)

    def ddToCcPatchNo(no):
        i = no.rindex(".")
        result = no[0:i]
        return result