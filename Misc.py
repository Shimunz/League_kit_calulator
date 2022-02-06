import json
from unittest import result
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

    def checkExtractorName(name):
        
        if(name=="Cho'Gath"):
            result = "Chogath"
            return result
        elif(name=='Dr. Mundo'):
            result = "DrMundo"
            return result
        elif(name=="Kai'Sa"):
            result = "Kaisa"
            return result
        elif(name=="Kha'Zix"):
            result = "Khazix"
            return result
        elif(name=="Kog'Maw"):
            result = "KogMaw"
            return result
        elif(name=='LeBlanc'):
            result = 'Leblanc'
            return result
        elif(name=='Wukong'):
            result = 'MonkeyKing'
            return result
        elif(name=='Nunu & Willump'):
            result = 'Nunu'
            return result
        elif(name=="Rek'Sai"):
            result = "RekSai"
            return result
        elif(name=="Vel'Koz"):
            result = "Velkoz"
            return result
        else:
            result = name.replace(" ","")
            result = result.replace(".","")
            return result

    def getJsonWeb(url):
        result = json.loads(requests.get(url).text)
        return result

    def createDir(dir):
        isDir = os.path.isdir("Patch/" + dir)
        if not isDir:
            os.makedirs("Patch/" + dir)

    def ddToCcPatchNo(no):
        i = no.rindex(".")
        result = no[0:i]
        return result

    def aplhaOnly(data):
        result = []
        for i in data:
            result.append(''.join(filter(str.isalpha, i)).lower())
        return result