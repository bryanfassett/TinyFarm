import pygame, sys, json
from Game.Common import isValidType, Logger, Throw, SpriteState
from Game.Common.fileExists import fileExists
from Game.config import SPRITES_PATH

class SpriteSheet():
    def __init__(self,name):
        if not isValidType(name, ""):
            return None
        
        self.Name = name
        self._BasePath = f"{SPRITES_PATH}{self.Name}\\"
        self._BaseConfig = self._loadConfig()
        self._SpriteSheetData = self._loadSpriteSheetData()

        if self._BaseConfig == {}:
            return None
        
        for sprite in self._SpriteSheetData:
            if self._SpriteSheetData[sprite] == None:
                return None
    
    def _loadConfig(self):
        if not fileExists(f"{self._BasePath}_config.json"):
            return {}
        with open(f"{self._BasePath}_config.json") as f:
            return json.load(f)
    
    def _loadSpriteSheetData(self):
        data = {}
        for sprite in self._BaseConfig["sprites"]:
            data[sprite] = _SpriteSheetData(self._BasePath,self._BaseConfig["sprites"][sprite])
        return data

class _SpriteSheetData():
    def __init__(self,basepath,data):
        self.Sprite = pygame.image.load(f"{basepath}{data['spritesheet']}").convert()
        self.JsonData = self._loadJsonData(basepath,data["json"])
        self.Animations = data["anims"]
    
    def _loadJsonData(self,basepath,file):
        fp = f"{basepath}{file}"
        if not fileExists(fp):
            return None
        with open(fp) as f:
            return json.load(f)
