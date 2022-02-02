import json
from FileOpener import *

class FileOpener:
    
    def getData(file_location):
        file = open(file_location, encoding='utf-8')
        data = json.load(file)
        return data