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
        self._BaseConfig = {}
        self._SpriteSheetData = {}

        if not self._loadConfig():
            return None
        self._loadSpriteSheetData()
    
    def _loadConfig(self):
        if not fileExists(f"{self._BasePath}_config.json"):
            return False
        
        with open(f"{self._BasePath}_config.json") as f:
            self._BaseConfig = json.load(f)
        
        return True
    
    def _loadSpriteSheetData(self):
        for sprite in self._BaseConfig["sprites"]:
            self._SpriteSheetData[sprite] = _SpriteSheetData(self._BasePath,self._BaseConfig["sprites"][sprite])

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
