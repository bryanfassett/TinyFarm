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

    # Public function to return animation type options
    def getAnimationTypes(self):
        animtypes = []
        for anim in self._SpriteSheetData:
            animtypes.append(anim)
        
        return animtypes
    
    # Public function to return animation files available for the sprite
    #
    # Params:
    # animtype - type of animation category as listed under anims section in the json config. (ex: "Idle" or "Walk")
    # state - SpriteState object declaring the direction of the sprite
    def getAnimationList(self,animtype,state):
        if not isValidType(state,SpriteState.LEFT) or not isValidType(animtype,""):
            return []
        return self._SpriteSheetData[animtype].Animations[state.value]
    
    # Public function to get the surface containing the specified sprite
    #
    # Params:
    # animtype - type of animation category as listed under anims section in the json config. (ex: "Idle" or "Walk")
    # animation - the name of the animation to blit on current frame (use getAnimationList to find)
    # x - the x coordinate placement for the surface
    # y - the y coordinate placement for the surface
    # scalex (optional) - image resize in pixels x
    # scaley (optional) - image resize in pixels y
    # surface (optional) - a predefined surface may be provided. The sprite will then be blitted onto the provided surface
    def getSpriteSurface(self,animtype,animation, x, y, scalex = 0, scaley = 0, surface = None):
        if not isValidType(animtype,"") or not isValidType(animation,""):
            return None
        jsondata = self._SpriteSheetData[animtype].JsonData

        xx,yy = 0,0               
        for key in jsondata["frames"]:
            if key["filename"] == animation:
                xx = key["frame"]["x"]
                yy = key["frame"]["y"]
                w = key["frame"]["w"]
                h = key["frame"]["h"]
                break

        if surface == None:
            surface = pygame.Surface((w,h))
        
        surface.set_colorkey((0,0,0))
        surface.blit(self._SpriteSheetData[animtype].Sprite, (x,y), (xx,yy,w,h))

        if not scalex == 0 or not scaley == 0:
            surface = pygame.transform.scale(surface, (scalex,scaley))

        return surface

class _SpriteSheetData():
    def __init__(self,basepath,data):
        self.Sprite = pygame.image.load(f"{basepath}{data['spritesheet']}").convert_alpha()
        self.JsonData = self._loadJsonData(basepath,data["json"])
        self.Animations = data["anims"]
    
    def _loadJsonData(self,basepath,file):
        fp = f"{basepath}{file}"
        if not fileExists(fp):
            return None
        with open(fp) as f:
            return json.load(f)
