from pygame import *
import TextInput

class FontTypes:

    def __init__(self,fontName,location,nameColour,fontNameSize,topOffSet):
        self.fontName=fontName
        self.location=location
        self.nameColour=nameColour
        self.darkBlue=nameColour
        self.selected=False
        self.fontNameSize=fontNameSize
        self.topOffSet=topOffSet
        self.textFont = font.SysFont(self.fontName,self.fontNameSize,False,False)


    def draw(self,screen):
        
        if not self.selected:
            draw.rect(screen,(255,255,255),self.location)
            txt=self.textFont.render(self.fontName,True,self.nameColour)
        else:
            draw.rect(screen,(49,98,138),self.location)
            txt=self.textFont.render(self.fontName,True,(255,255,255))
        screen.blit(txt,(self.location.left+8,self.location.top+self.topOffSet))

    def select(self):
        self.selected=not self.selected
        
    def deselected(self):
        self.selected=False

        
    def getSelected(self):
        return self.selected

    def mouseCollision(self, screen, mx, my):
        if(self.location.collidepoint(mx,my)):
            self.hoverEffect(screen)
            return True
        else:
            return False

    def hoverEffect(self, screen):
        rect=Surface((137,31), SRCALPHA, 32)
        rect.fill((150,150,150,100))
        screen.blit(rect,(self.location.left+2,self.location.top))

    def getFont(self):
        return self.textFont
    
    def getFontName(self):
        return self.fontName
    
class TextTypes:

    def __init__(self,inactiveColour,activeColour,borderColour,location, typeDisplay,bold,italics,underline,strike):
        self.inactiveColour=inactiveColour
        self.activeColour=activeColour
        self.location=location
        self.borderColour=borderColour
        self.selected=False
        self.typeDisplay=typeDisplay
        self.underline=underline
        self.strike=strike

        self.textFont = font.SysFont("Times New Roman",20)
        if bold:
            self.textFont = font.SysFont("Times New Roman",20,True)
        if italics:
            self.textFont = font.SysFont("Times New Roman",20,False,True)
    
    def draw(self,screen):
        if self.selected:
            draw.rect(screen,self.activeColour,self.location)
            text=self.textFont.render(self.typeDisplay,True,self.inactiveColour)
            lineCol=self.inactiveColour
        else:
            draw.rect(screen,self.inactiveColour,self.location)
            text=self.textFont.render(self.typeDisplay,True,self.activeColour)
            lineCol=self.activeColour
        draw.rect(screen,self.borderColour,self.location,2)
        screen.blit(text,(self.location.left+9,self.location.top+4))
        if self.underline:
            draw.line(screen,lineCol,(self.location.left+7,self.location.bottom-7),(self.location.right-7,self.location.bottom-7),1)
        if self.strike:
            draw.line(screen,lineCol,(self.location.left+7,self.location.bottom-15),(self.location.right-7,self.location.bottom-15),1)

    def mouseCollision(self, screen, mx, my):
        if(self.location.collidepoint(mx,my)):
            self.hoverEffect(screen)
            return True
        else:
            return False

    def hoverEffect(self, screen):
        rect=Surface((27,27), SRCALPHA, 32)
        rect.fill((150,150,150,100))
        screen.blit(rect,(self.location.left+2,self.location.top+2))

    def select(self):
        self.selected=not self.selected

    def getSelected(self):
        return self.selected

class TextSize:

    def __init__(self,darkBlue):
        self.size="24"
        self.darkBlue=darkBlue
        self.location=Rect(330,265,40,30)
        self.sizeFont=font.SysFont("Times New Roman",20)
        self.sizeText=self.sizeFont.render(self.size,True,self.darkBlue)
        
    def draw(self, screen):
        draw.rect(screen,(255,255,255),self.location)
        screen.blit(self.sizeText,(340,268))

    def mouseCollision(self, mx, my):
        if(self.location.collidepoint(mx,my)):
            return True
        else:
            return False

    def changeSize(self, screen):
        newSize=""
        self.sizeText=self.sizeFont.render(newSize,True,self.darkBlue)
        draw.rect(screen,(255,255,255),self.location)
        draw.rect(screen,self.darkBlue,self.location,2)
        self.TextInput = TextInput.TextInput(screen,337,266,self.location,False)
        
        newSize=self.TextInput.drawText(self.darkBlue,"Times New Roman",20,False,False,False,False)
        if newSize!="":
            self.size=newSize
        self.sizeText=self.sizeFont.render(self.size,True,self.darkBlue)

    def getSize(self):
        return int(self.size)

class TextTool:

    def __init__(self,inactiveColour,activeColour,darkBlue):

        self.numOfTextTypes=4
        self.inactiveColour=inactiveColour
        self.activeColour=activeColour
        self.darkBlue=darkBlue
        self.activeList=[]

        self.topOffSetList=[7,7,3,3]
        self.fontSizeList=[15,25,20,20]
        self.fontNameList=["Times New Roman","Comic Sans","Arial","Vladimir Script"]
        self.fontTypeList=[]
        for i in range(4):            
            self.fontTypeList.append(FontTypes(self.fontNameList[i],Rect(155,265+(32*i),140,30),self.darkBlue,self.fontSizeList[i],self.topOffSetList[i]))
        self.fontTypeList[0].select()

        self.boldList=[True,False,False,False]
        self.italicsList=[False,True,False,False]
        self.underlineList=[False,False,True,False]
        self.strikeList=[False,False,False,True]
        self.typeDisplayList=["B","I","U","S"]
        self.textTypeList=[]
        for i in range(self.numOfTextTypes):
            self.textTypeList.append(TextTypes(self.inactiveColour,self.activeColour,self.darkBlue,Rect(175+(50*i),215,30,30),
                                               self.typeDisplayList[i],self.boldList[i],self.italicsList[i],self.underlineList[i],
                                               self.strikeList[i]))

        self.textSize=TextSize(self.darkBlue)

    def getTextSize(self):
        return self.textSize
        
    def draw(self,screen):
        for i in range(self.numOfTextTypes):
            self.textTypeList[i].draw(screen)

    #def select
    def drawDropDown(self,screen):
        draw.rect(screen,self.darkBlue,[155,265,140,127])
        draw.polygon(screen,(255,255,255),((300,282),(310,282),(305,277)))
        for i in range(4):
            self.fontTypeList[i].draw(screen)
        draw.rect(screen,self.darkBlue,[155,265,140,127],2)

    def hideDropDown(self,screen):
        self.textFont = font.SysFont(self.getFont().getFontName(),self.fontSizeList[self.getFontNum()])
        draw.rect(screen,(255,255,255),(155,265,140,30))
        txt=self.textFont.render(self.getFont().getFontName(),True,self.darkBlue)
        screen.blit(txt,(155+8,265+self.topOffSetList[self.getFontNum()]))



    def font(self,fontNum):
        return self.fontTypeList[fontNum-1]
            
    def getFont(self):
        for i in range(4):
            if self.fontTypeList[i].getSelected():
                return self.fontTypeList[i]

    def deselect(self):
        for i in range(4):
            self.fontTypeList[i].deselected()


    def getFontNum(self):
        for i in range(4):
            if self.fontTypeList[i].getSelected():
                return i      
    #def selectFont(self,fontNum):
    

    def getBold(self):
        return self.getType(1)

    def getItalics(self):
        return self.getType(2)

    def getUnderline(self):
        return self.getType(3)

    def getStrike(self):
        return self.getType(4)

    def getType(self,typeNum):
        typeNum=typeNum-1
        return self.textTypeList[typeNum]

    #def selectTextType(self):
        
