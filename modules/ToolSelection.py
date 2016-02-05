from pygame import *

class ToolSelection:

    def __init__(self,colour,borderColour,location):
        self.colour=colour
        self.borderColour=borderColour
        self.location = location

    def changeBorderColour(self,borderColour):
        self.borderColour=borderColour

    def drawToolBackground(self, screen):
        draw.rect(screen,self.colour,self.location)            

    def drawToolBorder(self, screen):
        draw.rect(screen,self.borderColour,self.location,3)

    def mouseCollision(self, screen, mx, my):
        if(self.location.collidepoint(mx,my)):
            self.hoverEffect(screen)
        
        return self.location.collidepoint(mx,my)

    def hoverEffect(self, screen):
        rect=Surface((30,30), SRCALPHA, 32)
        rect.fill((230,230,230,50))
        screen.blit(rect,(self.location.left,self.location.top))

class ToolBox:

    def __init__(self,inactiveColour,activeColour):

        self.numOfTools=11
        
        self.inactiveColour = inactiveColour
        self.activeColour=activeColour

        self.toolList=[]
        for i in range(self.numOfTools):
            self.toolList.append(ToolSelection(self.inactiveColour,self.inactiveColour, Rect(60,175+(55*i),30,30)))

        self.selected=3
        self.getTool(self.selected).changeBorderColour(self.activeColour)

    def drawToolBackground(self,screen):
        for i in range(self.numOfTools):
            self.toolList[i].drawToolBackground(screen)

    def drawToolBorder(self, screen):
        for i in range(self.numOfTools):
            self.toolList[i].drawToolBorder(screen)

    def getTool(self, toolNum):
        return self.toolList[toolNum-1]

    def selectTool(self, toolNum):
        for i in range(self.numOfTools):
            self.toolList[i].changeBorderColour(self.inactiveColour)
        self.selected=toolNum

        self.getTool(self.selected).changeBorderColour(self.activeColour)

        toolNameList=["Palette","Cursor","Pencil","Eraser","Brush",
                      "Spray","Pen","Fill","Text","Shape","Stamp"]
        selectedTool=toolNameList[toolNum-1]
        return selectedTool




    
        
