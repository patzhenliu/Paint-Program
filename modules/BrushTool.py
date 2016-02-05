from pygame import *

class BrushSize:

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
        draw.circle(screen,self.colour,((self.location.right+self.location.left)//2,(self.location.top+self.location.bottom)//2),self.thickness)
        draw.rect(screen,self.borderColour,self.location,3) 

    def mouseCollision(self, screen, mx, my):
        if(self.location.collidepoint(mx,my)):
            self.hoverEffect(screen)
        
        return self.location.collidepoint(mx,my)

    def hoverEffect(self, screen):
        rect=Surface((36,36), SRCALPHA, 32)
        rect.fill((150,150,150,100))
        screen.blit(rect,(self.location.left+2,self.location.top+2))

class BrushTool:

    def __init__(self,inactiveColour,activeColour,titleColour,
                 titleFont,descriptionColour,descriptionFont,subtitleFont):

        self.numOfBrushes=10

        self.title="PAINT BRUSH"
        self.description1="Select a brush size and opacity to"
        self.description2="draw on the canvas."
        self.subtitle1="S I Z E"
        self.subtitle2="O P A C I T Y"

        self.inactiveColour = inactiveColour
        self.activeColour=activeColour
        self.titleColour=titleColour
        self.titleFont=titleFont
        self.descriptionColour=descriptionColour
        self.descriptionFont=descriptionFont
        self.subtitleFont=subtitleFont

        self.brushList=[]
        self.brushThickness=[3,4,5,7,8,10,12,13,15,17]
        for i in range(self.numOfBrushes):
            if (i+1)<=5:
                self.brushList.append(BrushSize(self.brushThickness[i],self.inactiveColour, Rect(155+(45*i),250,40,40)))
            if (i+1)>=6:
                self.brushList.append(BrushSize(self.brushThickness[i],self.inactiveColour, Rect(155+(45*(i-5)),300,40,40)))

        self.selected=6
        self.getBrush(self.selected).changeBorderColour(self.activeColour)

    def draw(self,screen):

        toolBox=Rect(130,90,270,680)
        smallToolBox=Rect(140,100,250,660)

        draw.rect(screen,(255,255,255),smallToolBox)
        draw.line(screen,self.titleColour,(150,150),(380,150),5)
        brushTitle=self.titleFont.render(self.title,True,self.titleColour)
        screen.blit(brushTitle,(182,115))
        display.text=self.descriptionFont.render(self.description1,True,self.descriptionColour)
        screen.blit(display.text,(162,155))
        display.text=self.descriptionFont.render(self.description2,True,self.descriptionColour)
        screen.blit(display.text,(162,175))

        draw.rect(screen,(57,96,128),[145,200,240,150])
        display.text=self.subtitleFont.render(self.subtitle1,True,(255,255,255))
        screen.blit(display.text,(230,210))
        draw.rect(screen,(57,96,128),[145,360,240,100])
        display.text=self.subtitleFont.render(self.subtitle2,True,(255,255,255))
        screen.blit(display.text,(195,370))

        for i in range(self.numOfBrushes):
            self.brushList[i].draw(screen)

    def getBrush(self, brushNum):
        return self.brushList[brushNum-1]

    def selectBrush(self, brushNum):
        for i in range(self.numOfBrushes):
            self.brushList[i].changeBorderColour(self.inactiveColour)
        self.selected=brushNum

        self.getBrush(self.selected).changeBorderColour(self.activeColour)
        
        return self.getBrush(brushNum).getThickness()


















    


                                  
