from pygame import *

class TextInput:

    def __init__(self,screen,mx,my,canvasLocation,useTextBox=True):
       font.init()
       self.screen = screen
       self.mx=mx
       self.my=my
       self.canvasLocation=canvasLocation
       self.useTextBox=useTextBox

       #self.textFont = font.SysFont(self.fontName,self.size,self.bold,self.italics)
       self.userInput = ""

       self.beforeText=self.screen.copy()
       self.textBox=Rect(self.mx,self.my,10,25)
       #draw.rect(self.screen,self.colour,self.textBox,1)
       self.cursor=0
       self.typing = False

    def changeFont(self):
        self.textFont = font.SysFont(self.fontName,self.size,self.bold,self.italics)

    def drawText(self,colour,fontName,size,bold,italics,underline,strike):
        self.colour = colour
        self.fontName = fontName
        self.size = size
        self.bold = bold
        self.italics = italics
        self.underline=underline
        self.strike=strike
        self.lineThickness=self.size//15
        if self.lineThickness==0:
            self.lineThickness=1
        
        self.getText()
        self.screen.blit(self.beforeText,(0,0))
        self.screen.blit(self.txt,(self.textBox.x+3,self.textBox.y+2))
        if len(self.userInput)>0:
            if self.underline:
                    draw.line(self.screen,self.colour,(self.textBox.x+3,self.textBox.y+self.txt.get_height()),
                              (self.textBox.x+self.txt.get_width(),self.textBox.y+self.txt.get_height()),self.lineThickness)
            if self.strike:
                    draw.line(self.screen,self.colour,(self.textBox.x+3,self.textBox.y+self.txt.get_height()//2),
                              (self.textBox.x+self.txt.get_width(),self.textBox.y+self.txt.get_height()//2),self.lineThickness)
        return self.userInput

    def getText(self):
        myclock = time.Clock()
        self.typing=True
        while self.typing:
            self.moveCursorForward()
            test = self.getTyping()
            if not self.typing:
                return
            self.changeFont()
            self.txt = self.textFont.render(self.userInput,True,self.colour)
            self.textBox = Rect(self.mx,self.my,self.txt.get_width()+10,self.txt.get_height()+6)
            self.screen.blit(self.beforeText,(0,0))
            if len(self.userInput)>0:
                if self.underline:
                    draw.line(self.screen,self.colour,(self.textBox.x+3,self.textBox.y+self.txt.get_height()),
                              (self.textBox.x+self.txt.get_width(),self.textBox.y+self.txt.get_height()),self.lineThickness)
                if self.strike:
                    draw.line(self.screen,self.colour,(self.textBox.x+3,self.textBox.y+self.txt.get_height()//2),
                              (self.textBox.x+self.txt.get_width(),self.textBox.y+self.txt.get_height()//2),self.lineThickness)
            if self.useTextBox:
                #draw.rect(self.screen,(255,255,255),self.textBox)
                draw.polygon(self.screen,(255,255,255),((self.mx,self.my+self.size//8),(self.mx,self.my+self.size//4),(self.mx+self.size//8,self.my+self.size//8)))
                draw.polygon(self.screen,(0,0,0),((self.mx,self.my+self.size//8),(self.mx,self.my+self.size//4),(self.mx+self.size//8,self.my+self.size//8)),1)
                #draw.rect(self.screen,(0,0,0),self.textBox,1)
            self.screen.blit(self.txt,(self.textBox.x+3,self.textBox.y+2))
            self.drawCursor()
            myclock.tick(100)
            display.flip()

    def getTyping(self):
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(self.userInput)>0:
                        self.userInput = self.userInput[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN:
                    #self.userInput+="\n"
                    #self.textBox = Rect(self.mx,self.my,self.txt.get_width()+10,(self.txt.get_height()*2)+9)
                    self.typing = False
                #elif self.canvasLocation.collidepoint(self.mx,self.my) and not self.textBox.collidepoint(self.mx,self.my):
                    #self.textBox = Rect(self.mx,self.my,self.txt.get_width()+6,self.txt.get_height()+6)
                    #self.typing = False
                elif e.key < 256:
                    if self.useTextBox:
                        self.userInput += e.unicode       # add character to ans
                    else:
                        if 47<e.key<58 and len(self.userInput)<2:
                            self.userInput += e.unicode

        return self.userInput
                        
    def moveCursorForward(self):
        self.cursor += 1

    def moveCursorBackwards(self):
        self.cursor -= 1

    def drawCursor(self):
        if self.cursor // 50 % 2 == 1:
            cx = self.textBox.x+self.txt.get_width()+3
            cy = self.textBox.y+3
            draw.rect(self.screen,(0,0,0),(cx,cy,2,self.textBox.height-6))
            
        display.flip()

    

    

            

            
            







            
        
