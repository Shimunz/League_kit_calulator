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
        
        result = name

        if(name=="aurelionsol"):
            result = "AurelionSol"
            return result
        if(name=="chogath"):
            result = "Chogath"
            return result
        elif(name=='drmundo'):
            result = "DrMundo"
            return result
        elif(name=="kaisa"):
            result = "Kaisa"
            return result
        elif(name=="khazix"):
            result = "Khazix"
            return result
        elif(name=="kogmaw"):
            result = "KogMaw"
            return result
        elif(name=='leblanc'):
            result = 'Leblanc'
            return result
        elif(name=='wukong'):
            result = 'MonkeyKing'
            return result
        elif(name=='monkeyking'):
            result = 'MonkeyKing'
            return result
        elif(name=='nunu & willump'):
            result = 'Nunu'
            return result
        elif(name=="reksai"):
            result = "RekSai"
            return result
        elif(name=="velkoz"):
            result = "Velkoz"
            return result
        elif(name=="xinzhao"):
            return "XinZhao"

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
    
    def capFistLetter(word):
        result = word.capitalize()
        return result
    