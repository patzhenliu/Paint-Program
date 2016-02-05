from pygame import *

class PenSize:

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

class PenTool:

    def __init__(self,inactiveColour,activeColour,titleColour,
                 titleFont,descriptionColour,descriptionFont,subtitleFont,penType):

        self.numOfPens=10
        self.penType=penType

        self.title="PEN"
        self.description1="Select a pen size and opacity to draw"
        self.description2="on the canvas."
        self.subtitle1="S I Z E"
        self.subtitle2="O P A C I T Y"

        self.inactiveColour = inactiveColour
        self.activeColour=activeColour
        self.titleColour=titleColour
        self.titleFont=titleFont
        self.descriptionColour=descriptionColour
        self.descriptionFont=descriptionFont
        self.subtitleFont=subtitleFont

        self.penList=[]
        self.penThickness=[3,4,5,6,7]
        for i in range(self.numOfPens):
            if (i+1)<=5:
                self.penList.append(PenSize(self.penThickness[i],self.inactiveColour, Rect(155+(45*i),250,40,40)))
            if (i+1)>=6:
                self.penList.append(PenSize(self.penThickness[i-5],self.inactiveColour, Rect(155+(45*(i-5)),300,40,40)))

        self.selected=5
        self.getPen(self.selected).changeBorderColour(self.activeColour)

    def draw(self,screen):

        toolBox=Rect(130,90,270,680)
        smallToolBox=Rect(140,100,250,660)

        draw.rect(screen,(255,255,255),smallToolBox)
        draw.line(screen,self.titleColour,(150,150),(380,150),5)
        penTitle=self.titleFont.render(self.title,True,self.titleColour)
        screen.blit(penTitle,(237,115))
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

        for i in range(self.numOfPens):
            self.penList[i].draw(screen)

    def getPenType(self,penNum):
        if penNum<=5:
            penType="Right Pen"
        if penNum>=6:
            penType="Left Pen"

        return penType

    def getPen(self, penNum):
        return self.penList[penNum-1]

    def selectPen(self, penNum):
        for i in range(self.numOfPens):
            self.penList[i].changeBorderColour(self.inactiveColour)
        self.selected=penNum

        self.getPen(self.selected).changeBorderColour(self.activeColour)
        
        return self.getPen(penNum).getThickness()


















        
