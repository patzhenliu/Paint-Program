from pygame import *

class ShapeSelection:

    def __init__(self,borderColour,location):
        self.borderColour=borderColour
        self.location = location

    def changeBorderColour(self,borderColour):
        self.borderColour=borderColour

    def draw(self, screen):
        draw.rect(screen,(255,255,255),self.location)
        draw.rect(screen,self.borderColour,self.location,3)

    def mouseCollision(self, screen, mx, my):
        if(self.location.collidepoint(mx,my)):
            self.hoverEffect(screen)
        
        return self.location.collidepoint(mx,my)

    def hoverEffect(self, screen):
        rect=Surface((36,36), SRCALPHA, 32)
        rect.fill((150,150,150,100))
        screen.blit(rect,(self.location.left+2,self.location.top+2))

class ShapeTool:

    def __init__(self,inactiveColour,activeColour,titleColour,
                 titleFont,descriptionColour,descriptionFont,subtitleFont,shapeType):

        self.numOfShapes=19

        self.title="SHAPES/LINES"
        self.description1="Select a shape and opacity to draw a"
        self.description2="shape on the canvas."
        self.subtitle1="O U T L I N E"
        self.subtitle2="F I L L"
           
        self.lineDescription="*Tip: Hold SHIFT for a V/H line."
        self.rectangleDescription="*Tip: Hold SHIFT for a perfect square."
        self.ellipseDescription="*Tip: Hold SHIFT for a perfect circle."
        self.customToolDescription="*Tip: Press ENTER to finish the shape."

        self.inactiveColour = inactiveColour
        self.activeColour=activeColour
        self.titleColour=titleColour
        self.titleFont=titleFont
        self.descriptionColour=descriptionColour
        self.descriptionFont=descriptionFont
        self.subtitleFont=subtitleFont

        self.shapeList=[]
        for i in range(self.numOfShapes):
            if (i+1)<=5:
                self.shapeList.append(ShapeSelection(self.inactiveColour, Rect(155+(45*i),250,40,40)))
            if 6<=(i+1)<=10:
                self.shapeList.append(ShapeSelection(self.inactiveColour, Rect(155+(45*(i-5)),300,40,40)))
            if 11<=(i+1)<=15:
                self.shapeList.append(ShapeSelection(self.inactiveColour, Rect(155+(45*(i-10)),410,40,40)))
            if (i+1)>=16:
                self.shapeList.append(ShapeSelection(self.inactiveColour, Rect(155+(45*(i-15)),460,40,40)))

        self.selected=1
        self.getShape(self.selected).changeBorderColour(self.activeColour)

    def draw(self,screen,shape):
        
        toolBox=Rect(130,90,270,680)
        smallToolBox=Rect(140,100,250,660)

        draw.rect(screen,(255,255,255),smallToolBox)
        draw.line(screen,self.titleColour,(150,150),(380,150),5)
        shapeTitle=self.titleFont.render(self.title,True,self.titleColour)
        screen.blit(shapeTitle,(178,115))
        display.text=self.descriptionFont.render(self.description1,True,self.descriptionColour)
        screen.blit(display.text,(152,155))
        display.text=self.descriptionFont.render(self.description2,True,self.descriptionColour)
        screen.blit(display.text,(152,175))

        draw.rect(screen,(57,96,128),[145,200,240,150])
        display.text=self.subtitleFont.render(self.subtitle1,True,(255,255,255))
        screen.blit(display.text,(195,210))
        draw.rect(screen,(57,96,128),[145,360,240,150])
        display.text=self.subtitleFont.render(self.subtitle2,True,(255,255,255))
        screen.blit(display.text,(225,370))

        if shape=="Line":
            display.text=self.descriptionFont.render(self.lineDescription,True,self.descriptionColour)
            screen.blit(display.text,(146,515))

        if shape=="Rectangle":
            display.text=self.descriptionFont.render(self.rectangleDescription,True,self.descriptionColour)
            screen.blit(display.text,(146,515))

        if shape=="Ellipse":
            display.text=self.descriptionFont.render(self.ellipseDescription,True,self.descriptionColour)
            screen.blit(display.text,(146,515))

        if shape=="Custom":
            display.text=self.descriptionFont.render(self.customToolDescription,True,self.descriptionColour)
            screen.blit(display.text,(146,515))

        for i in range(self.numOfShapes):
            self.shapeList[i].draw(screen)

    def getOutlineWidth(self,shapeNum):
        if shapeNum<=10:
            width=3
        if shapeNum>=11:
            width=0

        return width

    def getShapeType(self,shapeNum):
        shapeTypeList=["Rectangle", "Ellipse", "Triangle", "Pentagon", "Hexagon",
                       "Octogon", "Diamond", "Right Triangle","Custom"]
        #shapeNum=self.getShape(shapeNum)
        
        if shapeNum==1:
            shape="Line"
        elif shapeNum<=10:
            shape=shapeTypeList[shapeNum-2]
        elif shapeNum>=11:
            shape=shapeTypeList[shapeNum-11]

        return shape

    def getShape(self,shapeNum):
        return self.shapeList[shapeNum-1]

    def selectShape(self,shapeNum):
        for i in range(self.numOfShapes):
            self.shapeList[i].changeBorderColour(self.inactiveColour)
        self.selected=shapeNum

        self.getShape(self.selected).changeBorderColour(self.activeColour)

        width=self.getOutlineWidth(shapeNum)
        
        return width

    def drawShapeIcons(self,screen,black):
        
        draw.line(screen,black,(189,256),(161,283),4)
        draw.rect(screen,black,(208,260,24,20),3)
        draw.circle(screen,black,(265,270),13,3)
        draw.polygon(screen,black,((309,259),(296,279),(322,279)),3)
        draw.polygon(screen,black,((354,259),(367,268),(361,280),(347,280),(342,268)),3)
        draw.polygon(screen,black,((167,309),(182,309),(187,318),(182,330),(167,330),(162,319)),3)
        draw.polygon(screen,black,((213,309),(226,309),(231,314),(231,324),(226,329),(213,329),(208,324),(208,315)),3)
        draw.polygon(screen,black,((265,308),(277,319),(265,330),(253,319)),3)
        draw.polygon(screen,black,((299,310),(299,330),(320,330)),3)
        draw.polygon(screen,black,((347,310),(360,310),(358,320),(366,320),(364,330),(344,330)),3)
        
        draw.rect(screen,black,(163,420,24,20))
        draw.circle(screen,black,(220,430),13)
        draw.polygon(screen,black,((264,419),(251,439),(278,439)))
        draw.polygon(screen,black,((310,417),(323,428),(318,440),(302,440),(297,428)))
        draw.polygon(screen,black,((347,419),(362,419),(367,428),(362,440),(347,440),(342,428)))
        draw.polygon(screen,black,((168,470),(180,470),(186,475),(186,484),(180,491),(169,491),(163,485),(163,476)))
        draw.polygon(screen,black,((219,468),(232,480),(219,493),(206,480)))
        draw.polygon(screen,black,((255,470),(255,489),(274,489)))
        draw.polygon(screen,black,((301,469),(314,469),(312,479),(320,479),(318,489),(298,489)))












                
