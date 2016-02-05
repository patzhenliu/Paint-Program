from pygame import *

class PencilSize:

    def __init__(self,thickness,borderColour, location):
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
        draw.line(screen,self.colour,(self.location.left + 10,self.location.top + 20),(self.location.right-10, self.location.top + 20),self.thickness)
        draw.rect(screen,self.borderColour,self.location,3) 
        
    def mouseCollision(self, screen, mx, my):
        if(self.location.collidepoint(mx,my)):
            self.hoverEffect(screen)
        
        return self.location.collidepoint(mx,my)

    def hoverEffect(self, screen):
        rect=Surface((216,36), SRCALPHA, 32)
        rect.fill((150,150,150,100))
        screen.blit(rect,(self.location.left+2,self.location.top+2))


class PencilTool:
    
    def __init__(self,inactiveColour,activeColour,titleColour,
                 titleFont,descriptionColour,descriptionFont,subtitleFont):
        
        self.numOfPencils=6
        
        self.title="PENCIL"
        self.description1="Select a pencil size below and sketch"
        self.description2="freely on the canvas."
        self.subtitle="S I Z E"
        
        self.inactiveColour = inactiveColour
        self.activeColour=activeColour
        self.titleColour=titleColour
        self.titleFont=titleFont
        self.descriptionColour=descriptionColour
        self.descriptionFont=descriptionFont
        self.subtitleFont=subtitleFont

        self.pencilList = []
        for i in range(self.numOfPencils):
            self.pencilList.append(PencilSize(i+1,self.inactiveColour, Rect(155,200 + (50 * (i+1)) ,220,40)))

        self.selected=1
        self.getPencil(self.selected).changeBorderColour(self.activeColour)
        
    def draw(self, screen):
        
        toolBox=Rect(130,90,270,680)
        smallToolBox=Rect(140,100,250,660)

        draw.rect(screen,(255,255,255),smallToolBox)
        draw.line(screen,self.titleColour,(150,150),(380,150),5)
        pencilTitle=self.titleFont.render(self.title,True,self.titleColour)
        screen.blit(pencilTitle,(217,115))
        display.text=self.descriptionFont.render(self.description1,True,self.descriptionColour)
        screen.blit(display.text,(152,155))
        display.text=self.descriptionFont.render(self.description2,True,self.descriptionColour)
        screen.blit(display.text,(152,175))
        
        draw.rect(screen,(57,96,128),[145,200,240,350])
        display.text=self.subtitleFont.render(self.subtitle,True,(255,255,255))
        screen.blit(display.text,(230,210))
        
        for i in range(self.numOfPencils):
            self.pencilList[i].draw(screen)

    def getPencil(self, pencilNum):
        return self.pencilList[pencilNum-1]

    def selectPencil(self, pencilNum):
        for i in range(self.numOfPencils):
            self.pencilList[i].changeBorderColour(self.inactiveColour)
        self.selected=pencilNum

        self.getPencil(self.selected).changeBorderColour(self.activeColour)
        
        return self.getPencil(pencilNum).getThickness()









    
