from pygame import *

class OpacitySelection:

    def __init__(self,titleLocation,boxLocation,barXPos,
                 barYPos,titleFont,barColour):
        self.titleLocation=titleLocation
        self.boxLocation=boxLocation
        self.barXPos=barXPos
        self.barYPos=barYPos
        self.barColour=barColour
        
        self.title="O P A C I T Y"
        self.titleFont=titleFont

    def draw(self,screen,opacity):
        draw.rect(screen,(57,96,128),self.boxLocation)
        display.text=self.titleFont.render(self.title,True,(255,255,255))
        draw.rect(screen,self.barColour,[self.barXPos,self.barYPos,100,4])
        draw.rect(screen,(255,255,255),[self.barXPos,self.barYPos,opacity,4])
        #draw.polygon(screen,(255,255,255),((self.barXPos+opacity,
        
class OpacityTool:

    def __init__(self,titleLocation,boxLocation,barXPos,
                 barYPos,titleFont,barColour,screen):
        self.titleLocation=titleLocation
        self.boxLocation=boxLocation
        self.barXPos=barXPos
        self.barYPos=barYPos
        self.barColour=barColour
        self.titleFont=titleFont
        self.screen=screen

    def draw(self,opacity):
        OpacitySelection=OpacitySelection(self.titleLocation,self.boxLocation,
                                          self.barXPos,self.barYPos,self.barColour,
                                          self.titleFont,self.screen)
        OpacitySelection.draw(self.screen,opacity)

    def changeOpacity(self,opacity):
        
