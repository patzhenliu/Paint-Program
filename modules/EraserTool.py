from pygame import *

class EraserSize:

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
        rect=Surface((self.location.right-self.location.left-4,self.location.bottom-self.location.top-4), SRCALPHA, 32)
        rect.fill((150,150,150,100))
        screen.blit(rect,(self.location.left+2,self.location.top+2))

class EraserTool:

    def __init__(self,inactiveColour,activeColour,titleColour,
                 titleFont,descriptionColour,descriptionFont,subtitleFont):

        self.title="ERASER"
        self.description1="Select an eraser size below and erase"
        self.description2="your mistakes on canvas."
        self.subtitle1="S I Z E"
        self.subtitle2="O P A C I T Y"

        self.inactiveColour = inactiveColour
        self.activeColour=activeColour
        self.titleColour=titleColour
        self.titleFont=titleFont
        self.descriptionColour=descriptionColour
        self.descriptionFont=descriptionFont
        self.subtitleFont=subtitleFont

        self.eraserList=[]
        self.eraserThickness=[3,4,5,7,8,10,12,13,15,17,19,20,21,22]
        self.numOfErasers=len(self.eraserThickness)
        
        for i in range(self.numOfErasers-4):
            if (i+1)<=5:
                self.eraserList.append(EraserSize(self.eraserThickness[i],self.inactiveColour, Rect(155+(45*i),250,40,40)))
            if (i+1)>=6:
                self.eraserList.append(EraserSize(self.eraserThickness[i],self.inactiveColour, Rect(155+(45*(i-5)),300,40,40)))        

        for i in range(self.numOfErasers-4,self.numOfErasers):
            self.eraserList.append(EraserSize(self.eraserThickness[i],self.inactiveColour, Rect(155+(57*(i-10)),350,50,50)))

        self.selected=6
        self.getEraser(self.selected).changeBorderColour(self.activeColour)

    def draw(self, screen):

        toolBox=Rect(130,90,270,680)
        smallToolBox=Rect(140,100,250,660)
                                           
        draw.rect(screen,(255,255,255),smallToolBox)
        draw.line(screen,self.titleColour,(150,150),(380,150),5)
        eraserTitle=self.titleFont.render(self.title,True,self.titleColour)
        screen.blit(eraserTitle,(215,115))
        display.text=self.descriptionFont.render(self.description1,True,self.descriptionColour)
        screen.blit(display.text,(151,155))
        display.text=self.descriptionFont.render(self.description2,True,self.descriptionColour)
        screen.blit(display.text,(151,175))

        draw.rect(screen,(57,96,128),[145,200,240,210])
        display.text=self.subtitleFont.render("S I Z E",True,(255,255,255))
        screen.blit(display.text,(230,210))
        draw.rect(screen,(57,96,128),[145,420,240,100])
        display.text=self.subtitleFont.render("O P A C I T Y",True,(255,255,255))
        screen.blit(display.text,(195,430))

        for i in range(self.numOfErasers):
            self.eraserList[i].draw(screen)

    def getEraser(self, eraserNum):
        return self.eraserList[eraserNum-1]

    def selectEraser(self, eraserNum):
        for i in range(self.numOfErasers):
            self.eraserList[i].changeBorderColour(self.inactiveColour)
        self.selected=eraserNum

        self.getEraser(self.selected).changeBorderColour(self.activeColour)
        
        return self.getEraser(eraserNum).getThickness()
