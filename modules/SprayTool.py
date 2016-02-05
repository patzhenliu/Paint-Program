from pygame import *

class SpraySize:

    def __init__(self,thickness,borderColour,location):
        self.thickness=thickness
        self.colour=(0,0,0)
        self.borderColour=borderColour
        self.location = location

    def changeThickness(self,thickness):
        self.thickness=thickness

    def getThickness(self):
        return self.thickness

    def changeBorderColour(self,borderColour):
        self.borderColour=borderColour

    def draw(self, screen):
        draw.rect(screen,(255,255,255),self.location)            
        ####ICON
        draw.rect(screen,self.borderColour,self.location,3) 

    def mouseCollision(self, screen, mx, my):
        if(self.location.collidepoint(mx,my)):
            self.hoverEffect(screen)
        
        return self.location.collidepoint(mx,my)

    def hoverEffect(self, screen):
        rect=Surface((36,36), SRCALPHA, 32)
        rect.fill((150,150,150,100))
        screen.blit(rect,(self.location.left+2,self.location.top+2))

class SprayTool:

    def __init__(self,inactiveColour,activeColour,titleColour,
                 titleFont,descriptionColour,descriptionFont,subtitleFont):

        self.numOfSprays=10

        self.title="SPRAY PAINT"
        self.description1="Select a spray paint size and opacity"
        self.description2="to draw on the canvas."
        self.subtitle1="S I Z E"
        self.subtitle2="O P A C I T Y"

        self.inactiveColour = inactiveColour
        self.activeColour=activeColour
        self.titleColour=titleColour
        self.titleFont=titleFont
        self.descriptionColour=descriptionColour
        self.descriptionFont=descriptionFont
        self.subtitleFont=subtitleFont

        self.sprayList=[]
        self.sprayThickness=[3,4,5,7,8,10,12,13,15,17]
        for i in range(self.numOfSprays):
            if (i+1)<=5:
                self.sprayList.append(SpraySize(self.sprayThickness[i],self.inactiveColour, Rect(155+(45*i),250,40,40)))
            if (i+1)>=6:
                self.sprayList.append(SpraySize(self.sprayThickness[i],self.inactiveColour, Rect(155+(45*(i-5)),300,40,40)))

        self.selected=6
        self.getSpray(self.selected).changeBorderColour(self.activeColour)

    def draw(self,screen):

        toolBox=Rect(130,90,270,680)
        smallToolBox=Rect(140,100,250,660)

        draw.rect(screen,(255,255,255),smallToolBox)
        draw.line(screen,self.titleColour,(150,150),(380,150),5)
        sprayTitle=self.titleFont.render(self.title,True,self.titleColour)
        screen.blit(sprayTitle,(185,115))
        display.text=self.descriptionFont.render(self.description1,True,self.descriptionColour)
        screen.blit(display.text,(152,155))
        display.text=self.descriptionFont.render(self.description2,True,self.descriptionColour)
        screen.blit(display.text,(152,175))

        draw.rect(screen,(57,96,128),[145,200,240,150])
        display.text=self.subtitleFont.render("S I Z E",True,(255,255,255))
        screen.blit(display.text,(230,210))
        draw.rect(screen,(57,96,128),[145,360,240,100])
        display.text=self.subtitleFont.render("O P A C I T Y",True,(255,255,255))
        screen.blit(display.text,(195,370))

        for i in range(self.numOfSprays):
            self.sprayList[i].draw(screen)

    def getSpray(self, sprayNum):
        return self.sprayList[sprayNum-1]

    def selectSpray(self, sprayNum):
        for i in range(self.numOfSprays):
            self.sprayList[i].changeBorderColour(self.inactiveColour)
        self.selected=sprayNum

        self.getSpray(self.selected).changeBorderColour(self.activeColour)
        
        return self.getSpray(sprayNum).getThickness()












                    
