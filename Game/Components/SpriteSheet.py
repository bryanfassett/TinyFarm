import pygame, sys, json
from Game.Common import isValidType, Logger, Throw, SpriteState
from Game.Common.fileExists import fileExists
from Game.config import SPRITES_PATH

# Class for loading and gathering all spritesheets and json data related to the specified sprite name
#
# Params:
# name - The name of the folder containing the sprite. The folder must contain a _config.json
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
    
    # Public function to return animation files available for the sprite
    #
    # Params:
    # animtype - type of animation category as listed under anims section in the json config. (ex: "Idle" or "Walk")
    # state - SpriteState object declaring the direction of the sprite
    def getAnimationList(self,animtype,state):
        if not isValidType(state,SpriteState.SpriteState.LEFT) or not isValidType(animtype,""):
            return []
        return self._SpriteSheetData[animtype].Animations[state.value]
    
    # Public function to get the surface containing the specified sprite
    #
    # Params:
    # animtype - type of animation category as listed under anims section in the json config. (ex: "Idle" or "Walk")
    # animation - the name of the animation to blit on current frame (use getAnimationList to find)
    # state - SpriteState object declaring the direction of the sprite
    # x - the x coordinate placement for the surface
    # y - the y coordinate placement for the surface
    # w (optional) - the width of the surface
    # h (optional) - the height of the surface
    # surface (optional) - a predefined surface may be provided. The sprite will then be blitted onto the provided surface
    def getSpriteSurface(self,animtype,animation, state, x, y, w = 0, h = 0, surface = None):
        if not isValidType(animtype,"") or not isValidType(animation,"") or not isValidType(state,SpriteState.SpriteState.LEFT):
            return None

        jsondata = self._SpriteSheetData[animtype].JsonData

        xx,yy = 0,0        
        for key in jsondata:
            if key["filename"] == animation:
                xx = key["spriteSourceSize"]["x"]
                yy = key["spriteSourceSize"]["y"]
                if w == 0:
                    w = key["spriteSourceSize"]["w"]
                if h == 0:
                    h = key["spriteSourceSize"]["h"]
                break

        if surface == None:
            surface = pygame.Surface((w,h))
        
        surface.set_colorkey((0,0,0))
        surface.blit(self._SpriteSheetData[animtype].Sprite, (x,y), (xx,yy,w,h))
        return surface

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
