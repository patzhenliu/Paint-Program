from pygame import *

class CustomShape:

    def __init__(self,screen):
        self.screen=screen
        self.screenShot="Nothing"

        self.pointList=[]
    
    def getPoints(self,mx,my):
        self.pointList.append((mx,my))
        

    def drawLine(self,mx,my,colour):
        self.getPoints(mx,my)
        if len(self.pointList)>=2:
            draw.line(self.screen,colour,(self.pointList[-2]),(self.pointList[-1]),3)

    def stopDrawing(self,colour,filled):
        draw.line(self.screen,colour,(self.pointList[-1]),self.pointList[0],3)
        if filled==0:
            self.screen.blit(self.screenShot,(447,92))
            draw.polygon(self.screen,colour,self.pointList)
        self.clearPoints()

    def clearPoints(self):
        self.pointList=[]

    def getScreenShot(self,canvasLocation):
        self.screenShot=self.screen.subsurface(canvasLocation).copy()
        
