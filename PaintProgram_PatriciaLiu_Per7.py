#PaintProgram_PatriciaLiu_Per7.py
#GALAXY PAINT
#https://github.com/patzhenliu/Paint-Program.git

from pygame import *
from random import *
from math import *
import sys
from pygame.locals import *

sys.path.insert(0, 'modules')

import TextInput as TextInput

import ToolSelection
import PencilTool
import EraserTool
import BrushTool
import SprayTool
import PenTool
import TextTool
import ShapeTool
import CustomShape
import ShortcutMenu

################SCREEN SETUP######################

#INITIATE/SCREEN SIZE SETUP
init()
screen = display.set_mode((0,0),RESIZABLE)
height=screen.get_height()
width=screen.get_width()

#SCREEN LOGO/TITLE
display.set_caption("Untitled")
logo=image.load("images/icon.png")
display.set_icon(logo)

##################################################

#FONTS+INITIATE FONT MODULE
font.init()
RGBFont=font.SysFont("Times New Roman",25)
ribbonFont=font.SysFont("Times New Roman",20)
ribbonFont2=font.SysFont("Times New Roman",15)
titleFont=font.SysFont("Times New Roman",25,True)
xyFont=font.SysFont("Times New Roman",10)

##################################################

#IMPORT TKINTER FOR SAVING/LOADING
from tkinter import *
root=Tk()
root.withdraw()

##################################################

#FLAG VARIABLES
mmode="up"
col2Switch=False
saved=False
colPick=False
leftClick=False
fullScreen=False
music=True
musicClick=False
transformTab=False

boldText=False
italicizeText=False
underlineText=False
strikeText=False
custom=False

textClick=False
showDropDown=False
textColRandom=False
textColChange=False

changeOpacity=False

selected=False
moveSelected=False
placeSelected=False
moveArea=True
copyArea=False
pasteArea=False
copiedAnArea=False

###########VARIABLE STARTING VALUES###############

#START POSITIONS FOR BOX IN THE COLOUR PALETTE
cmx1=156
cmy1=484
cmx2=156
cmy2=518

#DEFAULT SETTINGS
ribbon="None"
tool="Pencil"
subTool="None"
currentStamp="None"
shape="Line"
currentStamp="None"
stampPage=1
backgroundPage=1
fName=""

#PREVIOUS TOOL
#Used when tool becomes palette. If the user clicks "OK"
#at the bottom right corner tool goes back to the tool
#that was selected before "Palette".
prevTool="Pencil"

#DEFAULT PENCIL/ERASER/PAINT BRUSH THICKNESS
pencilLineThick=1
eraserThick=10
brushThick=10
sprayThick=10
penThick=7
penType="Right Pen"

#FILLS BRUSH/ERASER SPACES
#Fills in the spaces between the circles when using
#eraser and paint brush for a smooth consistent line.
pRandNum=0
pmx = 0
pmy = 0

#OPACITY
brushOpacity=220
sprayOpacity=220
eraserOpacity=220
penOpacity=220

####################COLOURS#######################

#BASIC COLOURS
white=255,255,255
black=0,0,0
darkBlue=9,58,98
lightBlue=80,148,201
medBlue=28,114,179
grayBlue=135,161,183
cyan=57,96,128

#COLOURS CHOSEN BY USER(2)
#Predefined as black and white
col=0,0,0
col2=255,255,255

#COLOUR ONLY FOR INPUTING TEXT
textCol=0,0,0

##############IMPORT/RESIZING IMAGES##############

#BACKGROUND IMAGE + BLIT
background=image.load("images/space2.jpg")
background=transform.scale(background,(width,height))
screen.blit(background,(0,0))

#COLOUR SWITCH/PALETTE IMAGES
pickColourImg=image.load("images/pickColour.png")
pickColour=transform.scale(pickColourImg,(226,320))
arrows=image.load("images/arrows.png")
arrows=transform.scale(arrows,(30,20))
arrowsReverse=image.load("images/arrowsReverse.png")
arrowsReverse=transform.scale(arrowsReverse,(30,20))

#MOVING TOOL POINTER IMAGE
pointer=image.load("images/pointer.png")
pointer=transform.scale(pointer,(76,50))

#TOOL ICON IMAGES
colourIcon=image.load("images/colourSpectrum.jpg")
colourIcon=transform.scale(colourIcon,(30,30))
paletteIcon=image.load("images/paletteIcon.png")
paletteIcon=transform.scale(paletteIcon,(20,20))
cursorIcon=image.load("images/cursorIcon.png")
cursorIcon=transform.scale(cursorIcon,(15,15))
moveIcon=image.load("images/moveIcon.png")
copyIcon=image.load("images/copyIcon.png")
pasteIcon=image.load("images/pasteIcon.png")
moveIcon2=image.load("images/moveIcon2.png")
copyIcon2=image.load("images/copyIcon2.png")
pasteIcon2=image.load("images/pasteIcon2.png")
pencilIcon=image.load("images/pencilIcon.png")
pencilIcon=transform.scale(pencilIcon,(20,20))
eraserIcon=image.load("images/eraserIcon.png")
eraserIcon=transform.scale(eraserIcon,(20,20))
brushIcon=image.load("images/brushIcon.png")
brushIcon=transform.scale(brushIcon,(20,20))
sprayPaintIcon=image.load("images/sprayPaintIcon.png")
sprayPaintIcon=transform.scale(sprayPaintIcon,(20,20))
penIcon=image.load("images/penIcon.png")
penIcon=transform.scale(penIcon,(20,20))
fillIcon=image.load("images/fillIcon.png")
fillIcon=transform.scale(fillIcon,(20,20))
textIcon=image.load("images/textIcon.png")
textIcon=transform.scale(textIcon,(15,15))
shapeIcon=image.load("images/shapeIcon.png")
shapeIcon=transform.scale(shapeIcon,(15,15))
stampIcon=image.load("images/stampIcon.png")
stampIcon=transform.scale(stampIcon,(20,20))
dropperIcon=image.load("images/dropperIcon.png")
dropperIcon=transform.scale(dropperIcon,(15,15))
diceIcon=image.load("images/diceIcon.png")
diceIcon=transform.scale(diceIcon,(15,15))

#BACKGROUNDS IMAGES
spaceImg1=image.load("images/spaceImg1.jpg")
spaceImg1=transform.scale(spaceImg1,(777,677))
spaceIcon1=transform.scale(spaceImg1,(155,135))
spaceImg2=image.load("images/spaceImg2.jpg")
spaceImg2=transform.scale(spaceImg2,(777,677))
spaceIcon2=transform.scale(spaceImg2,(155,135))
spaceImg3=image.load("images/spaceImg3.jpg")
spaceImg3=transform.scale(spaceImg3,(777,677))
spaceIcon3=transform.scale(spaceImg3,(155,135))
spaceImg4=image.load("images/spaceImg4.jpg")
spaceImg4=transform.scale(spaceImg4,(777,677))
spaceIcon4=transform.scale(spaceImg4,(155,135))
spaceImg5=image.load("images/spaceImg5.jpg")
spaceImg5=transform.scale(spaceImg5,(777,677))
spaceIcon5=transform.scale(spaceImg5,(155,135))
spaceImg6=image.load("images/spaceImg6.jpg")
spaceImg6=transform.scale(spaceImg6,(777,677))
spaceIcon6=transform.scale(spaceImg6,(155,135))
spaceImg7=image.load("images/spaceImg7.jpg")
spaceImg7=transform.scale(spaceImg7,(777,677))
spaceIcon7=transform.scale(spaceImg7,(155,135))
spaceImg8=image.load("images/spaceImg8.jpg")
spaceImg8=transform.scale(spaceImg8,(777,677))
spaceIcon8=transform.scale(spaceImg8,(155,135))
spaceImg9=image.load("images/spaceImg9.jpg")
spaceImg9=transform.scale(spaceImg9,(777,677))
spaceIcon9=transform.scale(spaceImg9,(155,135))
spaceImg10=image.load("images/spaceImg10.jpg")
spaceImg10=transform.scale(spaceImg10,(777,677))
spaceIcon10=transform.scale(spaceImg10,(155,135))

#MUSIC/NO MUSIC ICONS
noMusic=image.load("images/noMusic.png")
noMusic=transform.scale(noMusic,(15,15))
musicIcon=image.load("images/musicIcon.png")
musicIcon=transform.scale(musicIcon,(15,15))

#SPRAYPAINT ICONS
sprayIcon=image.load("images/sprayIcon.png")
spray1=transform.scale(sprayIcon,(13,13))
spray2=transform.scale(sprayIcon,(15,15))
spray3=transform.scale(sprayIcon,(17,17))
spray4=transform.scale(sprayIcon,(19,19))
spray5=transform.scale(sprayIcon,(21,21))
spray6=transform.scale(sprayIcon,(23,23))
spray7=transform.scale(sprayIcon,(27,27))
spray8=transform.scale(sprayIcon,(29,29))
spray9=transform.scale(sprayIcon,(33,33))
spray10=transform.scale(sprayIcon,(35,35))

#SPRAYPAINT ICONS
rpenIcon=image.load("images/rpenIcon.png")
lpenIcon=image.load("images/lpenIcon.png")
pen1=transform.scale(rpenIcon,(19,19))
pen2=transform.scale(rpenIcon,(21,21))
pen3=transform.scale(rpenIcon,(23,23))
pen4=transform.scale(rpenIcon,(27,27))
pen5=transform.scale(rpenIcon,(29,29))
pen6=transform.scale(lpenIcon,(19,19))
pen7=transform.scale(lpenIcon,(21,21))
pen8=transform.scale(lpenIcon,(23,23))
pen9=transform.scale(lpenIcon,(27,27))
pen10=transform.scale(lpenIcon,(29,29))

#STAMP IMAGES
asteroid=image.load("stamps/asteroidStamp.png")
earth=image.load("stamps/earthStamp.png")
earth=transform.scale(earth,(500,500))
jupiter=image.load("stamps/jupiterStamp.png")
jupiter=transform.scale(jupiter,(500,500))
mars=image.load("stamps/marsStamp.png")
mars=transform.scale(mars,(500,500))
mercury=image.load("stamps/mercuryStamp.png")
neptune=image.load("stamps/neptuneStamp.png")
rocket=image.load("stamps/rocketStamp.png")
saturn=image.load("stamps/saturnStamp.png")
sun=image.load("stamps/sunStamp.png")
sun=transform.scale(sun,(500,500))
stars=image.load("stamps/starStamp.png")
ufo=image.load("stamps/ufoStamp.png")
uranus=image.load("stamps/uranusStamp.png")
uranus=transform.scale(uranus,(500,500))
venus=image.load("stamps/venusStamp.png")
venus=transform.scale(venus,(500,500))
shootStar=image.load("stamps/shootStarStamp.png")

#STAMP IMAGES FOR HOVERING OVER STAMPS
asteroidWhite=image.load("stamps/asteroidWhite.png")
earthWhite=image.load("stamps/earthWhite.png")
earthWhite=transform.scale(earthWhite,(500,500))
jupiterWhite=image.load("stamps/jupiterWhite.png")
jupiterWhite=transform.scale(jupiterWhite,(500,500))
marsWhite=image.load("stamps/marsWhite.png")
marsWhite=transform.scale(marsWhite,(500,500))
mercuryWhite=image.load("stamps/mercuryWhite.png")
neptuneWhite=image.load("stamps/neptuneWhite.png")
rocketWhite=image.load("stamps/rocketWhite.png")
saturnWhite=image.load("stamps/saturnWhite.png")
sunWhite=image.load("stamps/sunWhite.png")
sunWhite=transform.scale(sunWhite,(500,500))
starsWhite=image.load("stamps/starsWhite.png")
ufoWhite=image.load("stamps/ufoWhite.png")
uranusWhite=image.load("stamps/uranusWhite.png")
uranusWhite=transform.scale(uranusWhite,(500,500))
venusWhite=image.load("stamps/venusWhite.png")
venusWhite=transform.scale(venusWhite,(500,500))
shootStarWhite=image.load("stamps/shootStarWhite.png")

#NUMBER IMAGES FOR STAMP PAGE NUMBER
pageOne=image.load("images/1.png")
pageOne=transform.scale(pageOne,(40,40))
pageTwo=image.load("images/2.png")
pageTwo=transform.scale(pageTwo,(40,40))

###################TOOL BOXES#####################
#Used mainly to see if mouse makes contact with
#the rectangle.

#TOOL SELECTION BOXES
colourRect1=Rect(60,120,30,30)
colourRect2=Rect(45,105,30,30)
arrowRect=Rect(90,95,30,20)
dropperRect=Rect(155,715,30,30)
diceRect=Rect(195,715,30,30)

#COLOUR HISTORY BOXES
#Keeps track of previously used colours
colHisRect1=Rect(155,545,20,20)
colHisRect2=Rect(195,545,20,20)
colHisRect3=Rect(235,545,20,20)
colHisRect4=Rect(275,545,20,20)
colHisRect5=Rect(315,545,20,20)
colHisRect6=Rect(355,545,20,20)
colHisRect7=Rect(395,545,20,20)

#COLOUR SELECTION BOXES(PALETTE)
pickColourRect=Rect(155,210,220,320)
pickColourRect2=Rect(152,207,226,326)
doneColourRect=Rect(320,715,55,30)

#PAGE TURN BOXES(STAMPS)(NOT VISIBLE)
pageLeftRect=Rect(225,730,10,20)
pageRightRect=Rect(295,730,10,20)

#STAMP BOXES(NOT VISIBLE)
earthRect=Rect(150,215,110,105)
marsRect=Rect(275,220,105,100)
uranusRect=Rect(150,330,110,105)
venusRect=Rect(275,335,105,100)
saturnRect=Rect(170,460,190,125)
shootStarRect=Rect(155,620,90,80)
jupiterRect=Rect(270,600,110,105)
sunRect=Rect(257,165,118,110)
starsRect=Rect(153,199,94,87)
neptuneRect=Rect(190,325,50,60)
neptuneRect2=Rect(225,290,110,110)
neptuneRect3=Rect(320,305,50,60)
rocketRect=Rect(155,390,65,100)
rocketRect2=Rect(155,430,80,50)
rocketRect3=Rect(155,475,100,90)
asteroidRect=Rect(270,410,90,80)
mercuryRect=Rect(275,500,100,100)
ufoRect=Rect(150,595,120,115)
ufoRect2=Rect(270,605,60,100)

#FILL BOXES
changeColRect=Rect(155,200,220,40)
fillCanvasRect=Rect(155,250,220,40)

#################BORDER COLOURS###################
#Used to highlight the tool borders when they are
#selected

#TOOL BORDERS
dropperCol=darkBlue
diceCol=darkBlue

#COLOUR HISTORY BORDERS
colHisCol1=white
colHisCol2=white
colHisCol3=white
colHisCol4=white
colHisCol5=white
colHisCol6=white
colHisCol7=white

##################CANVAS SETUP####################

#CANVAS BOX
canvasRect=Rect(447,92,776,676)
canvasBorderRect=Rect(435,80,800,705)
xyRect=Rect(450,770,100,10)

#CANVAS+BORDER
draw.rect(screen,darkBlue,canvasBorderRect)
draw.rect(screen,white,canvasRect)
draw.rect(screen,lightBlue,canvasBorderRect,4)

xTxt=xyFont.render("X:",True,white)
yTxt=xyFont.render("Y:",True,white)
screen.blit(xTxt,(450,770))
screen.blit(yTxt,(490,770))
xyBuff=screen.subsurface(xyRect).copy()

#################TOOL BOX SETUP###################
#Area where all the tool options(eg.Size) are shown.

#TOOL BOX BOXES
toolBox=Rect(130,90,270,680)
smallToolBox=Rect(140,100,250,660)

#TRANSLUCENT BOX(AROUND TOOL BOX AREA)
transBox=Rect(35,80,375,700)
transBorder=Surface((375,700), SRCALPHA, 32)
transBorder.fill((9,58,98,100))
screen.blit(transBorder,(35,80))

##################POINTER SETUP###################
#A moving pointer that points to the currently selected tool
#from the tool box(starts at pencil).

#SCREENSHOT(TRANSLUCENT BOX)
pointerBuff=screen.subsurface(transBox).copy()

#POINTER POSITIONS
#Position for the pointer when a certain tool from
#the tool box is selected
palettePos=165+24
cursorPos=220+24
pencilPos=275+24
eraserPos=330+24
brushPos=385+24
sprayPos=440+24
penPos=495+24
fillPos=550+24
textPos=605+24
shapePos=660+24
stampPos=715+24

#CURRENT POINTER POSITION
newPos=pencilPos

###################RIBBON SETUP###################

#RIBBONS
fileTab=Rect(5,10,90,31)
editTab=Rect(100,10,90,31)
viewTab=Rect(195,10,90,31)
darkBlueRect=Rect(0,0,width,41)
rect=Surface((width,41),SRCALPHA,32)
rect.fill((9,58,98,100))
screen.blit(rect,(0,0))
draw.rect(screen,lightBlue,[0,41,width,4])

#RIBBON FEATURE BOXES
fileNewRect=Rect(9,45,162,27)
fileOpenRect=Rect(9,76,162,27)
fileSaveRect=Rect(9,107,162,27)
fileSaveAsRect=Rect(9,138,162,27)

editUndoRect=Rect(104,45,162,27)
editRedoRect=Rect(104,76,162,27)
editClearRect=Rect(104,107,162,27)
editTransformRect=Rect(104,138,162,27)

transformRect=Rect(266,134,170,128)
lRotateRect=Rect(270,138,162,27)
rRotateRect=Rect(270,169,162,27)
hFlipRect=Rect(270,200,162,27)
vFlipRect=Rect(270,231,162,27)

viewModeRect=Rect(199,45,162,27)
viewShortcutRect=Rect(199,76,162,27)

################EDIT(CLEAR) SETUP#################

#CLEAR YES/NO RECTS
yesClearRect=Rect(730,350,80,30)
noClearRect=Rect(835,350,80,30)

################UNDO/REDO SETUP###################

#UNDO/REDO LISTS
undoList=[screen.subsurface(canvasRect).copy()]
redoList=[]
screenShot=False
undo=False
undid=False

####################MUSIC SETUP###################()

#LOAD MUSIC
mixer.music.load("songs/festival.mp3")
error=mixer.Sound("songs/error.wav")

#MUSIC BOX(NOT VISIBLE)
musicRect=Rect(295,17,15,15)

#VOLUME SELECTION BOX(NOT VISIBLE)
volRect=Rect(317,17,80,15)

#VOLUME SELECTION BAR
volControl=Rect(386,17,8,14)
volBar=Rect(320,22,70,4)

#MUSIC ICON & VOLUME BAR +SCREENSHOTS
screen.blit(musicIcon,(295,17))
musicBuff=screen.subsurface(musicRect).copy()
draw.rect(screen,darkBlue,volBar)
volBuff=screen.subsurface(volRect).copy()
draw.rect(screen,white,volBar)
draw.rect(screen,white,volControl)
draw.rect(screen,darkBlue,volControl,2)

##################################################

#FUNCTIONS
#gets for rect only inside the canvas if user goes out of the canvas.
def rectIntersect(rect1, rect2):
    left = max(rect1.left, rect2.left)
    right = min(rect1.right, rect2.right)
    top = max(rect1.top, rect2.top)
    bottom = min(rect1.bottom, rect2.bottom)

    rect=Rect(left, top, right-left, bottom-top)
    return rect

##################################################

#__init__ FOR OBJECTS
ToolSelection = ToolSelection.ToolBox(darkBlue,lightBlue)
PencilTool = PencilTool.PencilTool(darkBlue,lightBlue,darkBlue,titleFont,darkBlue,ribbonFont2,RGBFont)
EraserTool = EraserTool.EraserTool(darkBlue,lightBlue,darkBlue,titleFont,darkBlue,ribbonFont2,RGBFont)
BrushTool = BrushTool.BrushTool(darkBlue,lightBlue,darkBlue,titleFont,darkBlue,ribbonFont2,RGBFont)
SprayTool = SprayTool.SprayTool(darkBlue,lightBlue,darkBlue,titleFont,darkBlue,ribbonFont2,RGBFont)
PenTool = PenTool.PenTool(darkBlue,lightBlue,darkBlue,titleFont,darkBlue,ribbonFont2,RGBFont,"Right Pen")
TextTool = TextTool.TextTool(white,darkBlue,darkBlue)
ShapeTool = ShapeTool.ShapeTool(darkBlue,lightBlue,darkBlue,titleFont,darkBlue,ribbonFont2,RGBFont,"Line")
CustomShape = CustomShape.CustomShape(screen)

##################################################

running = True

##################################################
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            sx,sy = evnt.pos
            if subTool!="Edit Clear" and subTool!="View Mode":#LINE
                canvasBuff=screen.subsurface(canvasRect).copy()
        if evnt.type == MOUSEBUTTONUP:
            ex,ey=evnt.pos
            leftClick=False

    ##################################################
        
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()

    keys=key.get_pressed()

    ##################################################
    #X AND Y
    #co-ordinates in the bottom left corner of the canvas
    if subTool=="None" :
        screen.blit(xyBuff,(450,770))
        if canvasRect.collidepoint(mx,my):
            xpos=xyFont.render(str(mx-447),True,white)
            ypos=xyFont.render(str(my-92),True,white)
            screen.blit(xpos,(465,770))
            screen.blit(ypos,(505,770))
    
    ##################################################

    #UNDO/REDO SCREENSHOTS
    if subTool=="None" and tool!="Stamp" and not custom and tool!="Cursor" and tool!="Palette" and not selected:
        if (mb[0]==1 and canvasRect.collidepoint(mx,my)):
            screenShot=False    #if click on canvas screenshot becomes False
        if mb[0]==0 and screenShot==False:   #when release mouse and screenshot false, program takes screenshot
            undoList.append(screen.subsurface(canvasRect).copy())
            screenShot=True
            if undid==True:
                del redoList[0:]    #deletes redoList if user uses undo
                undid=False

    ##################################################
    #BACKGROUND IMAGES
    if subTool!="View Mode":
        draw.rect(screen,darkBlue,[140,800,1015,160])
        draw.rect(screen,white,[160,805,975,150])
        draw.rect(screen,lightBlue,[140,800,1015,160],3)

        if backgroundPage==1:
            draw.polygon(screen,white,((1150,880),(1140,890),(1140,870)))
            if Rect(1140,870,10,20).collidepoint(mx,my):
                draw.polygon(screen,lightBlue,((1150,880),(1140,890),(1140,870)))
                if mb[0]==1:
                    backgroundPage=2
            
        elif backgroundPage==2:
            draw.polygon(screen,white,((145,880),(155,890),(155,870)))
            if Rect(145,870,10,20).collidepoint(mx,my):
                draw.polygon(screen,lightBlue,((145,880),(155,890),(155,870)))
                if mb[0]==1:
                    backgroundPage=1
        
        if backgroundPage==1:
            backgroundList=[spaceIcon1,spaceIcon2,spaceIcon3,spaceIcon4,spaceIcon5]
            for i in range(5):
                screen.blit(backgroundList[i],(170+200*i,812))
        elif backgroundPage==2:
            backgroundList=[spaceIcon6,spaceIcon7,spaceIcon8,spaceIcon9,spaceIcon10]
            for i in range(5):
                screen.blit(backgroundList[i],(170+200*i,812))

        for i in range(5):
            draw.rect(screen,darkBlue,[170+200*i,812,155,135],3)

        if subTool=="None":
            if Rect(170,812,155,135).collidepoint(mx,my):
                draw.rect(screen,lightBlue,[170,812,155,135],3)
                if mb[0]==1 and not leftClick:
                    if backgroundPage==1:
                        screen.blit(spaceImg1,(447,92))
                    elif backgroundPage==2:
                        screen.blit(spaceImg6,(447,92))
                    undoList.append(screen.subsurface(canvasRect).copy())
                    leftClick=True
                    
            if Rect(370,812,155,135).collidepoint(mx,my):
                draw.rect(screen,lightBlue,[370,812,155,135],3)
                if mb[0]==1 and not leftClick:
                    if backgroundPage==1:
                        screen.blit(spaceImg2,(447,92))
                    elif backgroundPage==2:
                        screen.blit(spaceImg7,(447,92))
                    undoList.append(screen.subsurface(canvasRect).copy())
                    leftClick=True
                    
            if Rect(570,812,155,135).collidepoint(mx,my):
                draw.rect(screen,lightBlue,[570,812,155,135],3)
                if mb[0]==1 and not leftClick:
                    if backgroundPage==1:
                        screen.blit(spaceImg3,(447,92))
                    elif backgroundPage==2:
                        screen.blit(spaceImg8,(447,92))
                    undoList.append(screen.subsurface(canvasRect).copy())
                    leftClick=True
                    
            if Rect(770,812,155,135).collidepoint(mx,my):
                draw.rect(screen,lightBlue,[770,812,155,135],3)
                if mb[0]==1 and not leftClick:
                    if backgroundPage==1:
                        screen.blit(spaceImg4,(447,92))
                    elif backgroundPage==2:
                        screen.blit(spaceImg9,(447,92))
                    undoList.append(screen.subsurface(canvasRect).copy())
                    leftClick=True
                    
            if Rect(970,812,155,135).collidepoint(mx,my):
                draw.rect(screen,lightBlue,[970,812,155,135],3)
                if mb[0]==1 and not leftClick:
                    if backgroundPage==1:
                        screen.blit(spaceImg5,(447,92))
                    elif backgroundPage==2:
                        screen.blit(spaceImg10,(447,92))
                    undoList.append(screen.subsurface(canvasRect).copy())
                    leftClick=True
        
    ##################################################
    #OPACITY
    TRANSPARENT = (255,0,255)

    #brush
    surf1 = Surface((200,200))
    surf1.fill(TRANSPARENT)
    surf1.set_colorkey(TRANSPARENT)
    draw.circle(surf1,col,(100,100),brushThick)
    surf1.set_alpha(int(brushOpacity/220*255/5))

    #eraser
    surf2 = Surface((200,200))
    surf2.fill(TRANSPARENT)
    surf2.set_colorkey(TRANSPARENT)
    draw.circle(surf2,white,(100,100),eraserThick)
    surf2.set_alpha(int(eraserOpacity/220*255/5))

    #right pen
    surf3 = Surface((200,200))
    surf3.fill(TRANSPARENT)
    surf3.set_colorkey(TRANSPARENT)
    draw.line(surf3,col,(100-penThick,100-penThick),(100+penThick,100+penThick),penThick)
    surf3.set_alpha(int(penOpacity/220*255/2))

    #left pen
    surf4 = Surface((200,200))
    surf4.fill(TRANSPARENT)
    surf4.set_colorkey(TRANSPARENT)
    draw.line(surf4,col,(100+penThick,100-penThick),(100-penThick,100+penThick),penThick)
    surf4.set_alpha(int(penOpacity/220*255/2))

    if brushOpacity==220:
        surf1.set_alpha(255)
    if 10>brushOpacity>0:
        surf1.set_alpha(int(brushOpacity/220*255))

    if eraserOpacity==220:
        surf2.set_alpha(255)
    if 10>eraserOpacity>0:
        surf2.set_alpha(int(eraserOpacity/220*255))

    if penOpacity==220:
        surf3.set_alpha(255)
        surf4.set_alpha(255)
    if 10>penOpacity>0:
        surf3.set_alpha(int(penOpacity/220*255))
        surf4.set_alpha(int(penOpacity/220*255))

    ##################################################
    #mixer.music.set_volume(0.0)
    #MUSIC
    if mixer.music.get_busy()==False:
        mixer.music.play()

    if currentStamp=="None" and subTool=="None":
        if (musicRect.collidepoint(mx,my) and subTool!="View Mode" and musicClick==False):
            if mb[0]==1:
                music=not music
                if not music:
                    screen.blit(noMusic,(295,17))
                    #mixer.music.pause()
                    
                    volume=0.0
                    mixer.music.set_volume(volume)
                    volControl=Rect(317,17,8,14)
                    screen.blit(volBuff,(317,17))
                    draw.rect(screen,white,volControl)
                    draw.rect(screen,darkBlue,volControl,2)
                    
                if music:
                    screen.blit(musicBuff,(295,17))
                    #mixer.music.unpause()
                    
                    volume=0.99
                    mixer.music.set_volume(volume)
                    volControl=Rect(386,17,8,14)
                    screen.blit(volBuff,(317,17))
                    volBar=Rect(320,22,70,4)
                    draw.rect(screen,white,volBar)
                    draw.rect(screen,white,volControl)
                    draw.rect(screen,darkBlue,volControl,2)
                    
                musicClick=True
        if mb[0]==0 and musicClick==True:
            musicClick=False

        if mb[0]==1 and volRect.collidepoint(mx,my) and 320<mx<390:
            volControl=Rect(mx-4,17,8,14)
            screen.blit(volBuff,(317,17))
            volBar=Rect(320,22,mx-320,4)
            draw.rect(screen,white,volBar)
            draw.rect(screen,white,volControl)
            draw.rect(screen,darkBlue,volControl,2)
            vmx=(volControl[0]+4)-317
            if vmx<=5:
                vmx=0.0
                screen.blit(noMusic,(295,17))
                #mixer.music.pause()
                music=False
            if vmx>5:
                screen.blit(musicBuff,(295,17))
                #mixer.music.unpause()
                music=True
            volume=vmx/70
            mixer.music.set_volume(volume)
            musicClick=True

    ##################################################        
    
    #POINTER
    screen.blit(pointerBuff,(35,80))
    #TOOL BOX
    draw.rect(screen,darkBlue,toolBox)
    draw.rect(screen,lightBlue,toolBox,3)

    #screen.blit(pointer,(80,newPos))
    draw.polygon(screen,lightBlue,((100,newPos),(130,newPos-13),(130,newPos+13)))
    draw.polygon(screen,darkBlue,((106,newPos),(132,newPos-10),(132,newPos+10)))
    
    ##################################################
    
    #RIBBON SELECTION
    draw.rect(screen,darkBlue,fileTab)
    draw.rect(screen,darkBlue,editTab)
    draw.rect(screen,darkBlue,viewTab)
    if currentStamp=="None" and subTool=="None":
        if fileTab.collidepoint(mx,my):
            if mb[0]==1:
                ribbon="File"
                
        if editTab.collidepoint(mx,my):
            if mb[0]==1:
                ribbon="Edit"
            
        if viewTab.collidepoint(mx,my):
            if mb[0]==1:
                ribbon="View"

    #RIBBON NAMES
    display.text=ribbonFont.render("FILE",True,white)
    screen.blit(display.text,(28,16))
    display.text=ribbonFont.render("EDIT",True,white)
    screen.blit(display.text,(123,16))
    display.text=ribbonFont.render("VIEW",True,white)
    screen.blit(display.text,(214,16))

    ##################################################
    
    #COLOUR SELECTION
    if subTool!="View Mode" and currentStamp=="None":
        if arrowRect.collidepoint(mx,my) and subTool=="None":
            screen.blit(arrowsReverse,(90,95))
        else:
            screen.blit(arrows,(90,95))
            switched=False
        if arrowRect.collidepoint(mx,my) and mb[0]==1 and not switched and subTool=="None":
            col,col2=col2,col
            switched=True
            col2Switch=not col2Switch
        if mb[0]==0:
            switched=False

    ##################################################

    #TOOL SELECTION
    ToolSelection.drawToolBackground(screen)

    screen.blit(colourIcon,(60,175))
    screen.blit(paletteIcon,(65,180))
    screen.blit(cursorIcon,(67,237))
    screen.blit(pencilIcon,(65,290))
    screen.blit(eraserIcon,(65,345))
    screen.blit(brushIcon,(65,400))
    screen.blit(sprayPaintIcon,(65,455))
    screen.blit(penIcon,(65,510))
    screen.blit(fillIcon,(65,565))
    screen.blit(textIcon,(67,622))
    screen.blit(shapeIcon,(67,677))
    screen.blit(stampIcon,(65,730))

    if currentStamp=="None" and subTool=="None":
        if (ToolSelection.getTool(1).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Palette" or keys[K_F1]:
            if tool!="Palette":
                prevTool,tool=tool,'Palette'
                if prevTool=="Stamp":
                    prevTool="stamp"
            newPos=palettePos
            tool = ToolSelection.selectTool(1)
                
        if (ToolSelection.getTool(2).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Cursor" or keys[K_F2]:
            tool = ToolSelection.selectTool(2)
            newPos=cursorPos
                
        if (ToolSelection.getTool(3).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Pencil" or keys[K_F3]:
            tool = ToolSelection.selectTool(3)
            newPos=pencilPos

        if (ToolSelection.getTool(4).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Eraser" or keys[K_F4]:
            tool = ToolSelection.selectTool(4)
            newPos=eraserPos

        if (ToolSelection.getTool(5).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Brush" or keys[K_F5]:
            tool = ToolSelection.selectTool(5)
            newPos=brushPos

        if (ToolSelection.getTool(6).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Spray" or keys[K_F6]:
            tool = ToolSelection.selectTool(6)
            newPos=sprayPos

        if (ToolSelection.getTool(7).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Pen" or keys[K_F7]:
            tool = ToolSelection.selectTool(7)
            newPos=penPos

        if (ToolSelection.getTool(8).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Fill" or keys[K_F8]:
            tool = ToolSelection.selectTool(8)
            newPos=fillPos

        if (ToolSelection.getTool(9).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Text" or keys[K_F9]:
            tool = ToolSelection.selectTool(9)
            newPos=textPos

        if (ToolSelection.getTool(10).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="Shape" or keys[K_F10]:
            tool = ToolSelection.selectTool(10)
            newPos=shapePos

        if (ToolSelection.getTool(11).mouseCollision(screen,mx,my) and mb[0]==1) or tool=="stamp" or keys[K_F11]:
            tool = ToolSelection.selectTool(11)
            newPos=stampPos

            stampPage=1

    ToolSelection.drawToolBorder(screen)
         
    draw.rect(screen,col2,colourRect2)
    draw.rect(screen,darkBlue,colourRect2,3)
    draw.rect(screen,col,colourRect1)
    draw.rect(screen,lightBlue,colourRect1,3)

    ##################################################
        
    #TOOL FEATURES
    if tool=='Palette':
        draw.rect(screen,white,smallToolBox)
        draw.line(screen,darkBlue,(150,150),(380,150),5)
        paletteTitle=titleFont.render("COLOUR PALETTE",True,darkBlue)
        screen.blit(paletteTitle,(151,115))
        display.text=ribbonFont2.render("Select a colour by clicking below or",True,darkBlue)
        screen.blit(display.text,(155,155))
        display.text=ribbonFont2.render("using the dropper tool.",True,darkBlue)
        screen.blit(display.text,(155,175))

        draw.rect(screen,(cyan),[145,200,240,500])
        screen.blit(pickColour,(152,210))

        display.text=RGBFont.render("Red:",True,white)
        screen.blit(display.text,(170,580))
        display.text=RGBFont.render("Green:",True,white)
        screen.blit(display.text,(170,620))
        display.text=RGBFont.render("Blue:",True,white)
        screen.blit(display.text,(170,660))

        draw.rect(screen,darkBlue,[310,580,50,30])
        draw.rect(screen,darkBlue,[310,620,50,30])
        draw.rect(screen,darkBlue,[310,660,50,30])
        
        display.text=RGBFont.render(str(col[0]),True,white)
        screen.blit(display.text,(315,580))
        display.text=RGBFont.render(str(col[1]),True,white)
        screen.blit(display.text,(315,620))
        display.text=RGBFont.render(str(col[2]),True,white)
        screen.blit(display.text,(315,660))

        #DONE BUTTON
        draw.rect(screen,darkBlue,doneColourRect)
        if doneColourRect.collidepoint(mx,my) and subTool=="None":
            rect=Surface((55,30), SRCALPHA, 32)
            rect.fill((230,230,230,50))
            screen.blit(rect,(320,715))
            if mb[0]==1 and not leftClick:
                tool=prevTool
            
        display.text=ribbonFont.render("OK",True,white)
        screen.blit(display.text,(332,719))
        draw.rect(screen,darkBlue,doneColourRect,3)

        #DROPPER
        draw.rect(screen,darkBlue,dropperRect)
        screen.blit(dropperIcon,(162,722))

        if dropperRect.collidepoint(mx,my) and subTool=="None":#dropper hover
            rect=Surface((30,30), SRCALPHA, 32)
            rect.fill((230,230,230,50))
            screen.blit(rect,(155,715))
            if evnt.type==MOUSEBUTTONDOWN:
                dropperCol=lightBlue
                subTool='Dropper'
        
        if subTool=='Dropper' and subTool=="None":
            if canvasRect.collidepoint(mx,my) and mb[0]==1:
                col=screen.get_at((mx,my))#FIX
                dropperCol=darkBlue
                subTool='None'

                colHisCol6=colHisCol5
                colHisCol5=colHisCol4
                colHisCol4=colHisCol3
                colHisCol3=colHisCol2
                colHisCol2=colHisCol1
                colHisCol1=col
        if dropperCol==lightBlue and mb[0]==1 and not dropperRect.collidepoint(mx,my):
            dropperCol=darkBlue
            subTool="None"
                
        draw.rect(screen,dropperCol,dropperRect,3)
        
        #DICE(RANDOMIZE COLOUR)
        draw.rect(screen,darkBlue,diceRect)
        screen.blit(diceIcon,(202,722))

        if diceRect.collidepoint(mx,my) and subTool=="None":#dropper hover
            rect=Surface((30,30), SRCALPHA, 32)
            rect.fill((230,230,230,50))
            screen.blit(rect,(195,715))
            if evnt.type==MOUSEBUTTONDOWN and leftClick==False:
                diceCol=lightBlue
                randCol=(randint(0,255),randint(0,255),randint(0,255))
                col=randCol
                leftClick=True

                colHisCol6=colHisCol5
                colHisCol5=colHisCol4
                colHisCol4=colHisCol3
                colHisCol3=colHisCol2
                colHisCol2=colHisCol1
                colHisCol1=col
                
        draw.rect(screen,diceCol,diceRect,3)
        if evnt.type==MOUSEBUTTONUP:
            diceCol=darkBlue
            

        #COLOUR HISTORY BOXES
        colourList=[colHisCol1,colHisCol2,colHisCol3,colHisCol4,colHisCol5,colHisCol6]
        for i in range(6):
            draw.rect(screen,colourList[i],(155+40*i,545,20,20))

        #HOVERING OVER COLOUR HISTORY BOXES AND CLICKING
        if subTool=="None":
            if colHisRect1.collidepoint(mx,my):
                rect=Surface((20,20), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(155,545))
                if mb[0]==1:
                    col=colHisCol1

            if colHisRect2.collidepoint(mx,my):
                rect=Surface((20,20), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(195,545))
                if mb[0]==1 and not leftClick:
                    col=colHisCol2
                    colHisCol2=colHisCol1
                    colHisCol1=col
                    leftClick=True

            if colHisRect3.collidepoint(mx,my):
                rect=Surface((20,20), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(235,545))
                if mb[0]==1 and not leftClick:
                    col=colHisCol3
                    colHisCol3=colHisCol2
                    colHisCol2=colHisCol1
                    colHisCol1=col
                    leftClick=True

            if colHisRect4.collidepoint(mx,my):
                rect=Surface((20,20), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(275,545))
                if mb[0]==1 and not leftClick:
                    col=colHisCol4
                    colHisCol4=colHisCol3
                    colHisCol3=colHisCol2
                    colHisCol2=colHisCol1
                    colHisCol1=col
                    leftClick=True

            if colHisRect5.collidepoint(mx,my):
                rect=Surface((20,20), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(315,545))
                if mb[0]==1 and not leftClick:
                    col=colHisCol5
                    colHisCol5=colHisCol4
                    colHisCol4=colHisCol3
                    colHisCol3=colHisCol2
                    colHisCol2=colHisCol1
                    colHisCol1=col
                    leftClick=True

            if colHisRect6.collidepoint(mx,my):
                rect=Surface((20,20), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(355,545))
                if mb[0]==1 and not leftClick:
                    col=colHisCol6
                    colHisCol6=colHisCol5
                    colHisCol5=colHisCol4
                    colHisCol4=colHisCol3
                    colHisCol3=colHisCol2
                    colHisCol2=colHisCol1
                    colHisCol1=col
                    leftClick=True

        #TINY BOX IN THE COLOUR SPECTRUM
        if col2Switch==False:   #COLOUR 1 (DEFAULT BLACK)
            screen.set_clip(pickColourRect2)#tiny box
            draw.rect(screen,black,[cmx1,cmy1,10,10],2)
            draw.rect(screen,white,[cmx1+1,cmy1+1,9,9],1)
            screen.set_clip(None)

            if subTool=="None":
                if pickColourRect.collidepoint(mx,my) and mb[0]==1 and not leftClick:
                    colPick=True
                    col=screen.get_at((mx,my))
                    cmx1=mx-5
                    cmy1=my-5

                if pickColourRect.collidepoint(mx,my) and mb[0]==0 and colPick==True:
                    colHisCol6=colHisCol5
                    colHisCol5=colHisCol4
                    colHisCol4=colHisCol3
                    colHisCol3=colHisCol2
                    colHisCol2=colHisCol1
                    colHisCol1=col
                    colPick=False

        if col2Switch==True:  #COLOUR 2 (DEFAULT WHITE)
            screen.set_clip(pickColourRect2)#tiny box
            draw.rect(screen,black,[cmx2,cmy2,10,10],2)
            draw.rect(screen,white,[cmx2+1,cmy2+1,9,9],1)
            screen.set_clip(None)

            if subTool=="None":
                if pickColourRect.collidepoint(mx,my) and mb[0]==1 and not leftClick:
                    colPick=True
                    col=screen.get_at((mx,my))
                    cmx2=mx-5
                    cmy2=my-5

                if pickColourRect.collidepoint(mx,my) and mb[0]==0 and colPick==True:
                    colHisCol6=colHisCol5
                    colHisCol5=colHisCol4
                    colHisCol4=colHisCol3
                    colHisCol3=colHisCol2
                    colHisCol2=colHisCol1
                    colHisCol1=col
                    colPick=False

        for i in range(153,354,40): #borders for colour history boxes
            draw.rect(screen,darkBlue,[i,543,24,24],3)
                
        draw.rect(screen,darkBlue,pickColourRect2,3)

    ##################################################

    if tool=='Cursor':
        draw.rect(screen,white,smallToolBox)
        draw.line(screen,darkBlue,(150,150),(380,150),5)
        cursorTitle=titleFont.render("SELECTION TOOL",True,darkBlue)
        screen.blit(cursorTitle,(155,115))
        display.text=ribbonFont2.render("Select an area on the canvas to",True,darkBlue)
        screen.blit(display.text,(165,155))

        nameList=["MOVE","COPY","PASTE"]
        iconList=[moveIcon,copyIcon,pasteIcon]
        for i in range(3):
            draw.rect(screen,darkBlue,[155+85*i,210,50,50],3)
            display.text=ribbonFont2.render(nameList[i],True,darkBlue)
            screen.blit(display.text,(158+85*i,265))
            screen.blit(iconList[i],(164+85*i,219))

        if Rect(155,210,50,50).collidepoint(mx,my) or moveArea:
            draw.rect(screen,lightBlue,[155,210,50,50],3)
            screen.blit(moveIcon2,(164,219))
            if mb[0]==1 and Rect(155,210,50,50).collidepoint(mx,my):
                moveArea=True
                copyArea=False
                pasteArea=False
        if moveArea:    
            descriptionPart2="move it. (*Left-click to place)"
            screen.blit(moveIcon2,(164,219))
            
        if Rect(240,210,50,50).collidepoint(mx,my) or copyArea:
            draw.rect(screen,lightBlue,[240,210,50,50],3)
            screen.blit(copyIcon2,(164+85,219))
            if mb[0]==1 and Rect(240,210,50,50).collidepoint(mx,my):
                copyArea=True
                pasteArea=False
                moveArea=False
        if copyArea:     
            descriptionPart2="copy it."
            screen.blit(copyIcon2,(164+85,219))
            
        if Rect(325,210,50,50).collidepoint(mx,my) or pasteArea:
            draw.rect(screen,lightBlue,[325,210,50,50],3)
            screen.blit(pasteIcon2,(164+85*2,219))
            if mb[0]==1 and Rect(325,210,50,50).collidepoint(mx,my):
                pasteArea=True
                copyArea=False
                moveArea=False
        if pasteArea:
            descriptionPart2="paste the copied area."
            screen.blit(pasteIcon2,(164+85*2,219))

        display.text=ribbonFont2.render(descriptionPart2,True,darkBlue)
        screen.blit(display.text,(165,175))
        

        if selected and mb[0]==0:
            screen.blit(selectBuff,(447,92))
            xStartVal=min(ex,sx)
            xEndVal=max(ex,sx)
            yStartVal=min(ey,sy)
            yEndVal=max(ey,sy)
            selectedRect=Rect(xStartVal,yStartVal,xEndVal-xStartVal,yEndVal-yStartVal)
            selectedRect=rectIntersect(selectedRect, canvasRect)
            copiedRect=screen.subsurface(selectedRect).copy()
            if moveArea:
                draw.rect(screen,white,selectedRect)
                moveSelected=True
            if copyArea:
                copyAreaRect=screen.subsurface(selectedRect).copy()
                copiedAnArea=True
            selectBuff=screen.subsurface(canvasRect).copy()
            selected=False


        if moveArea:
            if moveSelected:
                screen.blit(selectBuff,(447,92))
                screen.set_clip(canvasRect)
                screen.blit(copiedRect,(mx-(selectedRect.right-selectedRect.left)//2,my-(selectedRect.bottom-selectedRect.top)//2))
                draw.rect(screen,darkBlue,(mx-(selectedRect.right-selectedRect.left)//2,my-(selectedRect.bottom-selectedRect.top)//2,selectedRect.right-selectedRect.left,selectedRect.bottom-selectedRect.top),1)
                screen.set_clip(None)
                if mb[0]==1:
                    moveSelected=False
                    placeSelected=True
                    

            if placeSelected:
                moveSelected=False
                screen.blit(selectBuff,(447,92))
                screen.set_clip(canvasRect)
                screen.blit(copiedRect,(mx-(selectedRect.right-selectedRect.left)//2,my-(selectedRect.bottom-selectedRect.top)//2))
                draw.rect(screen,darkBlue,(mx-(selectedRect.right-selectedRect.left)//2,my-(selectedRect.bottom-selectedRect.top)//2,
                                          selectedRect.right-selectedRect.left,selectedRect.bottom-selectedRect.top),2)
                screen.set_clip(None)
                #canvasBuff=screen.subsurface(canvasRect).copy()
                if mb[0]==0:
                    placeSelected=False
                    screen.blit(selectBuff,(447,92))
                    screen.set_clip(canvasRect)
                    screen.blit(copiedRect,(mx-(selectedRect.right-selectedRect.left)//2,my-(selectedRect.bottom-selectedRect.top)//2))
                    screen.set_clip(None)
                    undoList.append(screen.subsurface(canvasRect).copy())

        if pasteArea:
            if copiedAnArea:
                if mb[0]==1 and mmode=="up" and canvasRect.collidepoint(mx,my):
                    selectBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"
                    
                if mb[0]==1 and mmode=="down":
                    screen.set_clip(canvasRect)
                    screen.blit(selectBuff,(447,92))
                    screen.blit(copyAreaRect,(mx-copyAreaRect.get_width()//2,my-copyAreaRect.get_height()//2))
                    draw.rect(screen,darkBlue,[mx-copyAreaRect.get_width()//2,my-copyAreaRect.get_height()//2,copyAreaRect.get_width(),copyAreaRect.get_height()],1)
                    screen.set_clip(None)
                    
                if mb[0]==0 and mmode=="down":
                    screen.set_clip(canvasRect)
                    screen.blit(selectBuff,(447,92))
                    screen.blit(copyAreaRect,(mx-copyAreaRect.get_width()//2,my-copyAreaRect.get_height()//2))
                    screen.set_clip(None)
                    undoList.append(screen.subsurface(canvasRect).copy())
                    mmode="up"
                    
            else:
                display.text=ribbonFont2.render("*No area has been copied yet.",True,darkBlue)
                screen.blit(display.text,(170,285))

        if not selected and not moveSelected and not placeSelected and not pasteArea:
            selectBuff=screen.subsurface(canvasRect).copy()

    if tool!="Cursor" and (selected or moveSelected):
        selected=False
        moveSelected=False
        screen.blit(undoList[-1],(447,92))

    ##################################################

    if tool=='Pencil':

        PencilTool.draw(screen)
        
        #SELECTING PENCIL
        if subTool=="None":
            if PencilTool.getPencil(1).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    pencilLineThick = PencilTool.selectPencil(1)

            if PencilTool.getPencil(2).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    pencilLineThick = PencilTool.selectPencil(2)

            if PencilTool.getPencil(3).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    pencilLineThick = PencilTool.selectPencil(3)

            if PencilTool.getPencil(4).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    pencilLineThick = PencilTool.selectPencil(4)

            if PencilTool.getPencil(5).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    pencilLineThick = PencilTool.selectPencil(5)

            if PencilTool.getPencil(6).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    pencilLineThick = PencilTool.selectPencil(6)

    ##################################################
        
    if tool=='Eraser':

        EraserTool.draw(screen)
        
        #SELECTING ERASER
        if subTool=="None":
            if EraserTool.getEraser(1).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(1)

            if EraserTool.getEraser(2).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(2)

            if EraserTool.getEraser(3).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(3)

            if EraserTool.getEraser(4).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(4)

            if EraserTool.getEraser(5).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(5)

            if EraserTool.getEraser(6).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(6)

            if EraserTool.getEraser(7).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(7)

            if EraserTool.getEraser(8).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(8)

            if EraserTool.getEraser(9).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(9)

            if EraserTool.getEraser(10).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(10)

            if EraserTool.getEraser(11).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(11)

            if EraserTool.getEraser(12).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(12)

            if EraserTool.getEraser(13).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(13)

            if EraserTool.getEraser(14).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    eraserThick = EraserTool.selectEraser(14)

        draw.rect(screen,darkBlue,[155,480,220,5])
        draw.rect(screen,white,[155,480,eraserOpacity,5])
        draw.polygon(screen,white,((155+eraserOpacity,475),(149+eraserOpacity,470),(149+eraserOpacity,460),
                                   (160+eraserOpacity,460),(160+eraserOpacity,471)))
        draw.polygon(screen,darkBlue,((155+eraserOpacity,475),(149+eraserOpacity,470),(149+eraserOpacity,460),
                                   (160+eraserOpacity,460),(160+eraserOpacity,471)),2)

        draw.rect(screen,darkBlue,[320,495,35,20])
        display.text=ribbonFont2.render("%",True,white)
        screen.blit(display.text,(358,495))
        display.text=ribbonFont2.render(str(int(eraserOpacity/220*100)),True,white)
        screen.blit(display.text,(325,495))

        if Rect(145,460,240,25).collidepoint(mx,my) and mb[0]==1 and not changeOpacity:
            changeOpacity=True

        if changeOpacity:
            if mb[0]==1:
                eraserOpacity=mx-155
                if eraserOpacity<=0:
                    eraserOpacity=0
                if eraserOpacity>220:
                    eraserOpacity=220
            elif mb[0]==0:
                changeOpacity=False

    ##################################################

    if tool=='Brush':

        BrushTool.draw(screen)

        #SELECTING BRUSH
        if subTool=="None":
            if BrushTool.getBrush(1).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(1)

            if BrushTool.getBrush(2).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(2)

            if BrushTool.getBrush(3).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(3)

            if BrushTool.getBrush(4).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(4)

            if BrushTool.getBrush(5).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(5)

            if BrushTool.getBrush(6).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(6)

            if BrushTool.getBrush(7).mouseCollision(screen,mx,my):
                    brushThick = BrushTool.selectBrush(7)

            if BrushTool.getBrush(8).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(8)

            if BrushTool.getBrush(9).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(9)

            if BrushTool.getBrush(10).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    brushThick = BrushTool.selectBrush(10)

        draw.rect(screen,darkBlue,[155,420,220,5])
        draw.rect(screen,white,[155,420,brushOpacity,5])
        draw.polygon(screen,white,((155+brushOpacity,415),(149+brushOpacity,410),(149+brushOpacity,400),
                                   (160+brushOpacity,400),(160+brushOpacity,411)))
        draw.polygon(screen,darkBlue,((155+brushOpacity,415),(149+brushOpacity,410),(149+brushOpacity,400),
                                   (160+brushOpacity,400),(160+brushOpacity,411)),2)

        draw.rect(screen,darkBlue,[320,435,35,20])
        display.text=ribbonFont2.render("%",True,white)
        screen.blit(display.text,(358,435))
        display.text=ribbonFont2.render(str(int(brushOpacity/220*100)),True,white)
        screen.blit(display.text,(325,435))

        if Rect(145,400,240,25).collidepoint(mx,my) and mb[0]==1 and not changeOpacity:
            changeOpacity=True

        if changeOpacity:
            if mb[0]==1:
                brushOpacity=mx-155
                if brushOpacity<=0:
                    brushOpacity=0
                if brushOpacity>220:
                    brushOpacity=220
            elif mb[0]==0:
                changeOpacity=False

    #######################################################3

    if tool=='Spray':

        SprayTool.draw(screen)
        
        #SPRAYPAINT ICONS
        screen.blit(spray1,(168,263))
        screen.blit(spray2,(212,262))
        screen.blit(spray3,(256,261))
        screen.blit(spray4,(300,260))
        screen.blit(spray5,(344,259))
        screen.blit(spray6,(162,308))
        screen.blit(spray7,(206,306))
        screen.blit(spray8,(250,305))
        screen.blit(spray9,(293,303))
        screen.blit(spray10,(337,302))

        #SELECTING SPRAYPAINT
        if subTool=="None":
            if SprayTool.getSpray(1).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(1)

            if SprayTool.getSpray(2).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(2)

            if SprayTool.getSpray(3).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(3)

            if SprayTool.getSpray(4).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(4)

            if SprayTool.getSpray(5).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(5)

            if SprayTool.getSpray(6).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(6)

            if SprayTool.getSpray(7).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(7)

            if SprayTool.getSpray(8).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(8)

            if SprayTool.getSpray(9).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(9)

            if SprayTool.getSpray(10).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    sprayThick = SprayTool.selectSpray(10)

        #SPRAY PAINT OPACITY
        #draw
        draw.rect(screen,darkBlue,[155,420,220,5])
        draw.rect(screen,white,[155,420,sprayOpacity,5])
        draw.polygon(screen,white,((155+sprayOpacity,415),(149+sprayOpacity,410),(149+sprayOpacity,400),
                                   (160+sprayOpacity,400),(160+sprayOpacity,411)))
        draw.polygon(screen,darkBlue,((155+sprayOpacity,415),(149+sprayOpacity,410),(149+sprayOpacity,400),
                                   (160+sprayOpacity,400),(160+sprayOpacity,411)),2)

        draw.rect(screen,darkBlue,[320,435,35,20])
        display.text=ribbonFont2.render("%",True,white)
        screen.blit(display.text,(358,435))
        display.text=ribbonFont2.render(str(int(sprayOpacity/220*100)),True,white)
        screen.blit(display.text,(325,435))

        #changing opacity
        if Rect(145,400,240,25).collidepoint(mx,my) and mb[0]==1 and not changeOpacity:
            changeOpacity=True

        if changeOpacity:
            if mb[0]==1:
                sprayOpacity=mx-155
                if sprayOpacity<=0:
                    sprayOpacity=0
                if sprayOpacity>220:
                    sprayOpacity=220
            elif mb[0]==0:
                changeOpacity=False

    ############################################

    ##################################################
    if tool=='Pen':

        PenTool.draw(screen)
        
        #PEN ICONS
        penIconList=[pen1,pen2,pen3,pen4,pen5,pen6,pen7,pen8,pen9,pen10]
        for i in range(10):
            if i<5:
                screen.blit(penIconList[i],(166+44*i,260-i))
            else:
                screen.blit(penIconList[i],(164+44*(i-5),315-i))

        #SELECTING PEN
        if subTool=="None":
            if PenTool.getPen(1).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(1)
                    penType = PenTool.getPenType(1)

            if PenTool.getPen(2).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(2)
                    penType = PenTool.getPenType(2)

            if PenTool.getPen(3).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(3)
                    penType = PenTool.getPenType(3)

            if PenTool.getPen(4).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(4)
                    penType = PenTool.getPenType(4)

            if PenTool.getPen(5).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(5)
                    penType = PenTool.getPenType(5)

            if PenTool.getPen(6).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(6)
                    penType = PenTool.getPenType(6)

            if PenTool.getPen(7).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(7)
                    penType = PenTool.getPenType(7)

            if PenTool.getPen(8).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(8)
                    penType = PenTool.getPenType(8)

            if PenTool.getPen(9).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(9)
                    penType = PenTool.getPenType(9)

            if PenTool.getPen(10).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    penThick = PenTool.selectPen(10)
                    penType = PenTool.getPenType(10)

        #PEN OPACITY
        #draw
        draw.rect(screen,darkBlue,[155,420,220,5])
        draw.rect(screen,white,[155,420,penOpacity,5])
        draw.polygon(screen,white,((155+penOpacity,415),(149+penOpacity,410),(149+penOpacity,400),
                                   (160+penOpacity,400),(160+penOpacity,411)))
        draw.polygon(screen,darkBlue,((155+penOpacity,415),(149+penOpacity,410),(149+penOpacity,400),
                                   (160+penOpacity,400),(160+penOpacity,411)),2)

        draw.rect(screen,darkBlue,[320,435,35,20])
        display.text=ribbonFont2.render("%",True,white)
        screen.blit(display.text,(358,435))
        display.text=ribbonFont2.render(str(int(penOpacity/220*100)),True,white)
        screen.blit(display.text,(325,435))

        #changing opacity
        if Rect(145,400,240,25).collidepoint(mx,my) and mb[0]==1 and not changeOpacity:
            changeOpacity=True

        if changeOpacity:
            if mb[0]==1:
                penOpacity=mx-155
                if penOpacity<=0:
                    penOpacity=0
                if penOpacity>220:
                    penOpacity=220
            elif mb[0]==0:
                changeOpacity=False

    #################################################

    if tool=='Fill':
        draw.rect(screen,white,smallToolBox)
        draw.line(screen,darkBlue,(150,150),(380,150),5)
        fillTitle=titleFont.render("FILL BUCKET",True,darkBlue)
        screen.blit(fillTitle,(184,115))
        display.text=ribbonFont2.render("Click and area on the canvas to fill",True,darkBlue)
        screen.blit(display.text,(160,155))
        display.text=ribbonFont2.render("using selected colour.",True,darkBlue)
        screen.blit(display.text,(160,175))

        draw.rect(screen,darkBlue,changeColRect)
        draw.rect(screen,darkBlue,fillCanvasRect)

        display.text=RGBFont.render("Choose Colour",True,white)
        screen.blit(display.text,(185,205))
        display.text=RGBFont.render("Fill Canvas",True,white)
        screen.blit(display.text,(205,255))

        if subTool=="None":
            if changeColRect.collidepoint(mx,my):
                rect=Surface((220,40), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(155,200))
                if mb[0]==1:
                    prevTool="Fill"
                    tool="Palette"
                    leftClick=True
                    
            if fillCanvasRect.collidepoint(mx,my):
                rect=Surface((220,40), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(155,250))
                if mb[0]==1 and not leftClick:
                    draw.rect(screen,col,canvasRect)
                    undoList.append(screen.subsurface(canvasRect).copy())
                    if undid==True:
                        del redoList[0:]
                        undid=False
                    leftClick=True
                
        draw.rect(screen,lightBlue,changeColRect,3)
        draw.rect(screen,lightBlue,fillCanvasRect,3)

    ##################################################

    if tool=='Text':
        draw.rect(screen,white,smallToolBox)
        draw.line(screen,darkBlue,(150,150),(380,150),5)
        textTitle=titleFont.render("TEXT BOX",True,darkBlue)
        screen.blit(textTitle,(204,115))
        display.text=ribbonFont2.render("Click an area on the canvas to start",True,darkBlue)
        screen.blit(display.text,(160,155))
        display.text=ribbonFont2.render("typing.",True,darkBlue)
        screen.blit(display.text,(160,175))

        draw.rect(screen,(57,96,128),[145,200,240,400])
        #display.text=RGBFont.render("T Y P E",True,white)
        #screen.blit(display.text,(225,210))

        display.text=ribbonFont2.render("*Tip: Press ENTER to finish typing.",True,darkBlue)
        screen.blit(display.text,(156,605))

        TextTool.draw(screen)
        
        ###SHOW RGB
        rgbList=["R:","G:","B:"]
        for i in range(3):
            display.text=ribbonFont2.render(rgbList[i],True,white)
            screen.blit(display.text,(240+50*i,320))
            display.text=ribbonFont2.render(str(textCol[i]),True,white)
            screen.blit(display.text,(255+50*i,320))

        #COLOUR STUFF
        draw.rect(screen,textCol,(160,315,30,30))
        draw.rect(screen,darkBlue,(160,315,30,30),2)#colour
        draw.rect(screen,darkBlue,(200,315,30,30))#colour
        screen.blit(diceIcon,(208,322))
        draw.rect(screen,darkBlue,(200,315,30,30),2)
        
        pickTextColourRect=Rect(150,358,230,224)
        draw.rect(screen,darkBlue,pickTextColourRect,3)
        pickTextColour=transform.scale(pickColourImg,(226,220))
        screen.blit(pickTextColour,(152,360))

        if subTool=="None":
            if Rect(152,360,226,220).collidepoint(mx,my) and mb[0]==1:
                textCol=screen.get_at((mx,my))
                
            if Rect(200,315,30,30).collidepoint(mx,my):
                rect=Surface((29,29), SRCALPHA, 32)
                rect.fill((230,230,230,50))
                screen.blit(rect,(200,315))
                draw.rect(screen,darkBlue,(200,315,30,30),2)
                if mb[0]==1 and not textClick:
                    textColRandom=True
                    tecColChange=False
                    
            if textColRandom:
                draw.rect(screen,lightBlue,(200,315,30,30),2)
                if textColChange==False:
                    textCol=randint(0,255),randint(0,255),randint(0,255)
                    textColChange=True
                
            if mb[0]==0 and textColRandom:
                textColRandom=False
                textColChange=False

            #CHECK IF BOLD/ITALICS/UNDERLINE/STIKE ARE IN USE
            if TextTool.getBold().mouseCollision(screen,mx,my) and not textClick:
                if mb[0]==1:
                    TextTool.getBold().select()
                    
            if TextTool.getItalics().mouseCollision(screen,mx,my) and not textClick:
                if mb[0]==1:
                    TextTool.getItalics().select()
                  

            if TextTool.getUnderline().mouseCollision(screen,mx,my) and not textClick:
                if mb[0]==1:
                    TextTool.getUnderline().select()
                    

            if TextTool.getStrike().mouseCollision(screen,mx,my) and not textClick:
                if mb[0]==1:
                    TextTool.getStrike().select()
        
        draw.rect(screen,darkBlue,(295,265,20,31))
        draw.polygon(screen,white,((300,277),(310,277),(305,282)))

        #draw dropdown
        if showDropDown and subTool=="None":
            draw.rect(screen,darkBlue,(155,265,160,31))
            TextTool.drawDropDown(screen)
            if TextTool.font(1).mouseCollision(screen,mx,my) and mb[0]==1:
                TextTool.deselect()
                TextTool.font(1).select()
                showDropDown=False
                
            if TextTool.font(2).mouseCollision(screen,mx,my) and mb[0]==1:
                TextTool.deselect()
                TextTool.font(2).select()
                showDropDown=False
            if TextTool.font(3).mouseCollision(screen,mx,my) and mb[0]==1:
                TextTool.deselect()
                TextTool.font(3).select()
                showDropDown=False
            if TextTool.font(4).mouseCollision(screen,mx,my) and mb[0]==1:
                TextTool.deselect()
                TextTool.font(4).select()
                showDropDown=False
        else:
            TextTool.hideDropDown(screen)
            
        if (Rect(295,265,20,31).collidepoint(mx,my) and mb[0]==1 and not textClick) or (not Rect(295,265,20,31).collidepoint(mx,my) and mb[0]==1 and showDropDown):
            showDropDown=not showDropDown #if click on drop down arrow itll hide or show the fonts

        if mb[0]==1 and not textClick:
            textClick=True
        
        if mb[0]==0 and textClick:
            textClick=False

        TextTool.getTextSize().draw(screen)
        draw.rect(screen,darkBlue,(155,265,160,31),2)#font
        
        if TextTool.getTextSize().mouseCollision(mx,my) and mb[0]==1 and subTool=="None":
            TextTool.getTextSize().changeSize(screen)
        draw.rect(screen,darkBlue,(330,265,40,30),2)#size

    ##################################################

    if tool=='Shape':

        ShapeTool.draw(screen,shape)
        ShapeTool.drawShapeIcons(screen,black)
        

        #SELECTING PEN
        if subTool=="None":
            if ShapeTool.getShape(1).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(1)
                    shape = ShapeTool.getShapeType(1)

            if ShapeTool.getShape(2).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(2)
                    shape = ShapeTool.getShapeType(2)

            if ShapeTool.getShape(3).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(3)
                    shape = ShapeTool.getShapeType(3)
                    
            if ShapeTool.getShape(4).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(4)
                    shape = ShapeTool.getShapeType(4)

            if ShapeTool.getShape(5).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(5)
                    shape = ShapeTool.getShapeType(5)

            if ShapeTool.getShape(6).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(6)
                    shape = ShapeTool.getShapeType(6)

            if ShapeTool.getShape(7).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(7)
                    shape = ShapeTool.getShapeType(7)

            if ShapeTool.getShape(8).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(8)
                    shape = ShapeTool.getShapeType(8)
        
            if ShapeTool.getShape(9).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(9)
                    shape = ShapeTool.getShapeType(9)
         
            if ShapeTool.getShape(10).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(10)
                    shape = ShapeTool.getShapeType(10)
                    customRadius=3
                  
            if ShapeTool.getShape(11).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(11)
                    shape = ShapeTool.getShapeType(11)
        
            if ShapeTool.getShape(12).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(12)
                    shape = ShapeTool.getShapeType(12)
           
            if ShapeTool.getShape(13).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(13)
                    shape = ShapeTool.getShapeType(13)

            if ShapeTool.getShape(14).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(14)
                    shape = ShapeTool.getShapeType(14)
               
            if ShapeTool.getShape(15).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(15)
                    shape = ShapeTool.getShapeType(15)
              
            if ShapeTool.getShape(16).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(16)
                    shape = ShapeTool.getShapeType(16)
             
            if ShapeTool.getShape(17).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(17)
                    shape = ShapeTool.getShapeType(17)
         
            if ShapeTool.getShape(18).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(18)
                    shape = ShapeTool.getShapeType(18)
            
            if ShapeTool.getShape(19).mouseCollision(screen,mx,my):
                if mb[0]==1:
                    radius = ShapeTool.selectShape(19)
                    shape = ShapeTool.getShapeType(19)
                    customRadius=0

    ##################################################

    if tool=='Stamp':
        
        
        if stampPage==1:
            draw.rect(screen,white,smallToolBox)
            draw.line(screen,darkBlue,(150,150),(380,150),5)
            stampTitle=titleFont.render("STAMPS",True,darkBlue)
            screen.blit(stampTitle,(216,115))
            display.text=ribbonFont2.render("Click and drag a stamp onto the",True,darkBlue)
            screen.blit(display.text,(165,155))
            display.text=ribbonFont2.render("canvas.",True,darkBlue)
            screen.blit(display.text,(165,175))

            draw.rect(screen,(cyan),[145,200,240,520])
            draw.polygon(screen,grayBlue,[(225,740),(235,730),(235,750)])
            draw.polygon(screen,darkBlue,[(305,740),(295,730),(295,750)])
            screen.blit(pageOne,(245,720))
            
            #STAMPS PAGE 1
            screen.blit(earth,(-50,30))
            screen.blit(mars,(75,20))
            screen.blit(uranus,(-50,130))
            screen.blit(venus,(75,135))
            screen.blit(saturn,(-20,220))
            screen.blit(shootStar,(-90,420))
            screen.blit(jupiter,(80,400))

            ##################################################

            if subTool=="None":
                if earthRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(earthWhite,(-50,30))
                    if mb[0]==1:
                        currentStamp="Earth"

                if marsRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(marsWhite,(75,20))
                    if mb[0]==1:
                        currentStamp="Mars"

                if uranusRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(uranusWhite,(-50,130))
                    if mb[0]==1:
                        currentStamp="Uranus"

                if venusRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(venusWhite,(75,135))
                    if mb[0]==1:
                        currentStamp="Venus"

                if saturnRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(saturnWhite,(-20,220))
                    if mb[0]==1:
                        currentStamp="Saturn"

                if shootStarRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(shootStarWhite,(-90,420))
                    if mb[0]==1:
                        currentStamp="Shooting Star"

                if jupiterRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(jupiterWhite,(80,400))
                    if mb[0]==1:
                        currentStamp="Jupiter"
                
                if pageRightRect.collidepoint(mx,my) and mmode=="up":
                    rect=Surface((15,25), SRCALPHA, 32)
                    rect.fill((255,255,255,70))
                    screen.blit(rect,(295,730))
                    if mb[0]==1 and currentStamp=="None":
                        stampPage=2

            ##################################################

            #USING STAMPS PAGE 1
            if currentStamp=="Earth":
                if mmode=="up" and mb[0]==1 and earthRect.collidepoint(mx,my):
                    stampBuff=screen.copy()
                    canvasBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"
                    
                if mmode=="down":
                    screen.blit(stampBuff,(0,0))
                    screen.blit(earth,(mx-250,my-230))
                    
                    if mb[0]==0:
                        if 390<ex<1273 and 34<ey<811:
                            undoList.append(screen.subsurface(canvasRect).copy())
                            if undid==True:
                                del redoList[0:]
                                undid=False
                        screen.blit(stampBuff,(0,0))
                        
                        screen.set_clip(canvasRect)
                        screen.blit(earth,(mx-250,my-230))
                        screen.set_clip(None)

                        mmode="up"
                        currentStamp="None"

            ##################################################
                    
            if currentStamp=="Mars":
                if mmode=="up" and mb[0]==1 and marsRect.collidepoint(mx,my):
                    stampBuff=screen.copy()
                    canvasBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"
                          
                if mmode=="down":
                    screen.blit(stampBuff,(0,0))
                    screen.blit(mars,(mx-250,my-250))
                    
                    if mb[0]==0:
                        if 394<ex<1272 and 42<ey<815:
                            undoList.append(screen.subsurface(canvasRect).copy())
                            if undid==True:
                                del redoList[0:]
                                undid=False
                        screen.blit(stampBuff,(0,0))
                        
                        screen.set_clip(canvasRect)
                        screen.blit(mars,(mx-250,my-250))
                        screen.set_clip(None)

                        mmode="up"
                        currentStamp="None"

            ##################################################

            if currentStamp=="Uranus":
                if mmode=="up" and mb[0]==1 and uranusRect.collidepoint(mx,my):
                    stampBuff=screen.copy()
                    canvasBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"       
                    
                if mmode=="down":
                    screen.blit(stampBuff,(0,0))
                    screen.blit(uranus,(mx-250,my-250))
                    
                    if mb[0]==0:
                        if 390<ex<1272 and 39<ey<816:
                            undoList.append(screen.subsurface(canvasRect).copy())
                            if undid==True:
                                del redoList[0:]
                                undid=False
                        screen.blit(stampBuff,(0,0))
                        
                        screen.set_clip(canvasRect)
                        screen.blit(uranus,(mx-250,my-250))
                        screen.set_clip(None)

                        mmode="up"
                        currentStamp="None"

            ##################################################

            if currentStamp=="Venus":
                if mmode=="up" and mb[0]==1 and venusRect.collidepoint(mx,my):
                    stampBuff=screen.copy()
                    canvasBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"
                    
                if mmode=="down":
                    screen.blit(stampBuff,(0,0))
                    screen.blit(venus,(mx-250,my-250))
                        
                    if mb[0]==0:
                        if 392<ex<1274 and 41<ey<819:
                            undoList.append(screen.subsurface(canvasRect).copy())
                            if undid==True:
                                del redoList[0:]
                                undid=False
                        screen.blit(stampBuff,(0,0))
      
                        screen.set_clip(canvasRect)
                        screen.blit(venus,(mx-250,my-250))
                        screen.set_clip(None)

                        mmode="up"
                        currentStamp="None"

            ##################################################
            
            if currentStamp=="Saturn":
                if mmode=="up" and mb[0]==1 and saturnRect.collidepoint(mx,my):
                    stampBuff=screen.copy()
                    canvasBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"         
                    
                if mmode=="down":
                    screen.blit(stampBuff,(0,0))
                    screen.blit(saturn,(mx-290,my-300))
                    
                    if mb[0]==0:
                        if 359<ex<1326 and 30<ey<827:
                            undoList.append(screen.subsurface(canvasRect).copy())
                            if undid==True:
                                del redoList[0:]
                                undid=False
                        screen.blit(stampBuff,(0,0))

                        screen.set_clip(canvasRect)
                        screen.blit(saturn,(mx-290,my-300))
                        screen.set_clip(None)

                        mmode="up"
                        currentStamp="None"

            ##################################################

            if currentStamp=="Shooting Star":
                if mmode=="up" and mb[0]==1 and shootStarRect.collidepoint(mx,my):
                    stampBuff=screen.copy()
                    canvasBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"
                    
                if mmode=="down":
                    screen.blit(stampBuff,(0,0))
                    screen.blit(shootStar,(mx-280,my-240))
                    
                    if mb[0]==0:
                        if 396<ex<1256 and 56<ey<813:
                            undoList.append(screen.subsurface(canvasRect).copy())
                            if undid==True:
                                del redoList[0:]
                                undid=False
                        screen.blit(stampBuff,(0,0))
                        
                        screen.set_clip(canvasRect)
                        screen.blit(shootStar,(mx-280,my-240))
                        screen.set_clip(None)

                        mmode="up"
                        currentStamp="None"

            ##################################################

            if currentStamp=="Jupiter":
                if mmode=="up" and mb[0]==1 and jupiterRect.collidepoint(mx,my):
                    stampBuff=screen.copy()
                    canvasBuff=screen.subsurface(canvasRect).copy()
                    mmode="down"

                if mmode=="down":
                    screen.blit(stampBuff,(0,0))
                    screen.blit(jupiter,(mx-250,my-250))
                    
                    if mb[0]==0:
                        if 399<ex<1282 and 39<ey<815:
                            undoList.append(screen.subsurface(canvasRect).copy())
                            if undid==True:
                                del redoList[0:]
                                undid=False
                        screen.blit(stampBuff,(0,0))
                        
                        screen.set_clip(canvasRect)
                        screen.blit(jupiter,(mx-250,my-250))
                        screen.set_clip(None)

                        mmode="up"
                        currentStamp="None"

        ##################################################
                    
        if stampPage==2:
            draw.rect(screen,white,smallToolBox)
            draw.line(screen,darkBlue,(150,150),(380,150),5)
            screen.blit(stampTitle,(216,115))

            draw.rect(screen,(cyan),[145,160,240,560])
            draw.polygon(screen,darkBlue,[(225,740),(235,730),(235,750)])
            draw.polygon(screen,grayBlue,[(305,740),(295,730),(295,750)])
            screen.blit(pageTwo,(245,720))
            
            #STAMPS PAGE 2
            screen.blit(sun,(65,-30))
            screen.blit(stars,(-90,-60))
            screen.blit(neptune,(-10,40))
            screen.blit(rocket,(-85,195))
            screen.blit(asteroid,(25,145))
            screen.blit(mercury,(40,250))
            screen.blit(ufo,(-40,370))

            ##################################################

            if subTool=="None":
                if sunRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(sunWhite,(65,-30))
                    if mb[0]==1:
                        currentStamp="Sun"

                if starsRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(starsWhite,(-90,-60))
                    if mb[0]==1:
                        currentStamp="Stars"

                if (neptuneRect.collidepoint(mx,my) or neptuneRect2.collidepoint(mx,my) or neptuneRect3.collidepoint(mx,my)) and mmode=="up":
                    screen.blit(neptuneWhite,(-10,40))
                    if mb[0]==1:
                        currentStamp="Neptune"

                if (rocketRect.collidepoint(mx,my) or rocketRect2.collidepoint(mx,my) or rocketRect3.collidepoint(mx,my)) and mmode=="up":
                    screen.blit(rocketWhite,(-85,195))
                    if mb[0]==1:
                        currentStamp="Rocket"

                if asteroidRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(asteroidWhite,(25,145))
                    if mb[0]==1:
                        currentStamp="Asteroid"

                if mercuryRect.collidepoint(mx,my) and mmode=="up":
                    screen.blit(mercuryWhite,(40,250))
                    if mb[0]==1:
                        currentStamp="Mercury"

                if (ufoRect.collidepoint(mx,my) or ufoRect2.collidepoint(mx,my)) and mmode=="up":
                    screen.blit(ufoWhite,(-40,370))
                    if mb[0]==1:
                        currentStamp="Ufo"
                
                if pageLeftRect.collidepoint(mx,my) and mmode=="up":
                    rect=Surface((15,25), SRCALPHA, 32)
                    rect.fill((255,255,255,70))
                    screen.blit(rect,(225,730))
                    if mb[0]==1 and currentStamp=="None":
                        stampPage=1

        ##################################################
                    
        #USING STAMPS PAGE 2
        if currentStamp=="Sun":
            if mmode=="up" and mb[0]==1 and sunRect.collidepoint(mx,my):
                stampBuff=screen.copy()
                canvasBuff=screen.subsurface(canvasRect).copy()
                mmode="down"
                
            if mmode=="down":
                screen.blit(stampBuff,(0,0))
                screen.blit(sun,(mx-250,my-250))
                
                if mb[0]==0:
                    if 387<ex<1277 and 38<ey<822:
                        undoList.append(screen.subsurface(canvasRect).copy())
                        if undid==True:
                            del redoList[0:]
                            undid=False
                    screen.blit(stampBuff,(0,0))
                    
                    screen.set_clip(canvasRect)
                    screen.blit(sun,(mx-250,my-250))
                    screen.set_clip(None)
                    
                    mmode="up"
                    currentStamp="None"

        ##################################################

        if currentStamp=="Stars":
            if mmode=="up" and mb[0]==1 and starsRect.collidepoint(mx,my):
                stampBuff=screen.copy()
                canvasBuff=screen.subsurface(canvasRect).copy()
                mmode="down"        

            if mmode=="down":
                screen.blit(stampBuff,(0,0))
                screen.blit(stars,(mx-300,my-300))
                
                if mb[0]==0:
                    if 413<ex<1281 and 46<ey<810:
                        undoList.append(screen.subsurface(canvasRect).copy())
                        if undid==True:
                            del redoList[0:]
                            undid=False
                    screen.blit(stampBuff,(0,0))
                    
                    screen.set_clip(canvasRect)
                    screen.blit(stars,(mx-300,my-300))
                    screen.set_clip(None)
                    
                    mmode="up"
                    currentStamp="None"

        ##################################################

        if currentStamp=="Neptune":
            if mmode=="up" and mb[0]==1 and (neptuneRect.collidepoint(mx,my) or neptuneRect2.collidepoint(mx,my) or neptuneRect3.collidepoint(mx,my)):
                stampBuff=screen.copy()
                canvasBuff=screen.subsurface(canvasRect).copy()
                mmode="down"

            if mmode=="down":
                screen.blit(stampBuff,(0,0))
                screen.blit(neptune,(mx-285,my-300))
                
                if mb[0]==0:
                    if 353<ex<1306 and 32<ey<817:
                        undoList.append(screen.subsurface(canvasRect).copy())
                        if undid==True:
                            del redoList[0:]
                            undid=False
                    screen.blit(stampBuff,(0,0))
                    
                    screen.set_clip(canvasRect)
                    screen.blit(neptune,(mx-285,my-300))
                    screen.set_clip(None)

                    mmode="up"
                    currentStamp="None"

        ##################################################
        
        if currentStamp=="Rocket":
            if mmode=="up" and mb[0]==1 and (rocketRect.collidepoint(mx,my) or rocketRect2.collidepoint(mx,my) or rocketRect3.collidepoint(mx,my)):
                stampBuff=screen.copy()
                canvasBuff=screen.subsurface(canvasRect).copy()
                mmode="down"

            if mmode=="down":
                screen.blit(stampBuff,(0,0))
                screen.blit(rocket,(mx-280,my-270))
                
                if mb[0]==0:
                    if 386<ex<1260 and ey<843:
                        undoList.append(screen.subsurface(canvasRect).copy())
                        if undid==True:
                            del redoList[0:]
                            undid=False
                    screen.blit(stampBuff,(0,0))
                    
                    screen.set_clip(canvasRect)
                    screen.blit(rocket,(mx-280,my-270))
                    screen.set_clip(None)

                    mmode="up"
                    currentStamp="None"

        ##################################################
    
        if currentStamp=="Asteroid":
            if mmode=="up" and mb[0]==1 and asteroidRect.collidepoint(mx,my):
                stampBuff=screen.copy()
                canvasBuff=screen.subsurface(canvasRect).copy()
                mmode="down"
            
            if mmode=="down":
                screen.blit(stampBuff,(0,0))
                screen.blit(asteroid,(mx-280,my-300))
                
                if mb[0]==0:
                    if 394<ex<1258 and 48<ey<804:
                        undoList.append(screen.subsurface(canvasRect).copy())
                        if undid==True:
                            del redoList[0:]
                            undid=False
                    screen.blit(stampBuff,(0,0))
                    
                    screen.set_clip(canvasRect)
                    screen.blit(asteroid,(mx-280,my-300))
                    screen.set_clip(None)

                    mmode="up"
                    currentStamp="None"

        ##################################################

        if currentStamp=="Mercury":
            if mmode=="up" and mb[0]==1 and mercuryRect.collidepoint(mx,my):
                stampBuff=screen.copy()
                canvasBuff=screen.subsurface(canvasRect).copy()
                mmode="down"

            if mmode=="down":
                screen.blit(stampBuff,(0,0))
                screen.blit(mercury,(mx-285,my-300))
                
                if mb[0]==0:
                    if 397<ex<1274 and 40<ey<817:
                        undoList.append(screen.subsurface(canvasRect).copy())
                        if undid==True:
                            del redoList[0:]
                            undid=False
                    screen.blit(stampBuff,(0,0))
                    
                    screen.blit(canvasBuff,(447,92))
                    screen.set_clip(canvasRect)
                    screen.blit(mercury,(mx-285,my-300))
                    screen.set_clip(None)

                    mmode="up"
                    currentStamp="None"

        ##################################################

        if currentStamp=="Ufo":
            if mmode=="up" and mb[0]==1 and (ufoRect.collidepoint(mx,my) or ufoRect2.collidepoint(mx,my)):
                stampBuff=screen.copy()
                canvasBuff=screen.subsurface(canvasRect).copy()
                mmode="down"

            if mmode=="down":
                screen.blit(stampBuff,(0,0))
                screen.blit(ufo,(mx-280,my-280))
                
                if mb[0]==0:
                    if 361<ex<1313 and 34<ey<822:
                        undoList.append(screen.subsurface(canvasRect).copy())
                        if undid==True:
                            del redoList[0:]
                            undid=False
                    screen.blit(stampBuff,(0,0))
                    
                    screen.blit(canvasBuff,(447,92))
                    screen.set_clip(canvasRect)
                    screen.blit(ufo,(mx-280,my-280))
                    screen.set_clip(None)

                    mmode="up"
                    currentStamp="None"

    ##################################################

    #USING THE TOOLS ON THE CANVAS
    if mb[0]==0:
        randNum=0 
            
    if mb[0]==1  and subTool=="None":
        if randNum==0:
            randNum=randint(1,1000)
            
        screen.set_clip(canvasRect)
        if tool=="Cursor" and not placeSelected and not pasteArea and canvasRect.collidepoint(mx,my):

            screen.blit(canvasBuff, (447,92))
            
            draw.rect(screen, darkBlue, (sx,sy,mx-sx,my-sy),1)
            selected=True
 
        if tool=='Pencil':
            draw.line(screen,col,(omx,omy),(mx,my),pencilLineThick)
            
        if tool=='Eraser':       
            if pRandNum==randNum: 
                dist=int(sqrt((mx-pmx)**2+(my-pmy)**2))
                for i in range(0,dist):
                    dotx=int(i*(mx-pmx)/dist+pmx)
                    doty=int(i*(my-pmy)/dist+pmy)
                    screen.blit(surf2, (dotx-surf2.get_width()//2,doty-surf2.get_height()//2))

            else:
                surf2.set_alpha(int(eraserOpacity/220*255))
                screen.blit(surf2, (mx-surf2.get_width()//2,my-surf2.get_height()//2))

        
        if tool=='Brush':    
            if pRandNum==randNum:
                dist=int(sqrt((mx-pmx)**2+(my-pmy)**2))
                for i in range(0,dist):
                    dotx=int(i*(mx-pmx)/dist+pmx)
                    doty=int(i*(my-pmy)/dist+pmy)
                    screen.blit(surf1, (dotx-surf1.get_width()//2,doty-surf1.get_height()//2))

            else:
                surf1.set_alpha(int(brushOpacity/220*255))
                screen.blit(surf1, (mx-surf1.get_width()//2,my-surf1.get_height()//2))
             
        if tool=="Spray":
            for i in range(int(sprayThick*1.2)):
                randx=randint(-1*sprayThick,sprayThick)
                randy=randint(-1*sprayThick,sprayThick)
                if randx**2+randy**2<sprayThick**2:
                    rect=Surface((2,2), SRCALPHA, 32)
                    rect.fill((col[0],col[1],col[2],int(sprayOpacity/220*255)))
                    screen.blit(rect,(mx+randx,my+randy))

        if tool=="Pen": 
            if penType=="Right Pen":
                if pRandNum==randNum:
                    dist=int(sqrt((mx-pmx)**2+(my-pmy)**2))
                    for i in range(0,dist):
                        dotx=int(i*(mx-pmx)/dist+pmx)
                        doty=int(i*(my-pmy)/dist+pmy)
                        screen.blit(surf3,(dotx-surf3.get_width()//2,doty-surf3.get_height()//2))
                else:
                    surf3.set_alpha(int(penOpacity/220*255))
                    screen.blit(surf3,(mx-surf3.get_width()//2,my-surf3.get_height()//2))
              
            if penType=="Left Pen":
                if pRandNum==randNum:
                    dist=int(sqrt((mx-pmx)**2+(my-pmy)**2))
                    for i in range(0,dist):
                        dotx=int(i*(mx-pmx)/dist+pmx)
                        doty=int(i*(my-pmy)/dist+pmy)
                       # draw.line(screen,col,(dotx+penThick,doty-penThick),(dotx-penThick,doty+penThick),3)
                        screen.blit(surf3,(dotx-surf3.get_width()//2,doty-surf3.get_height()//2))
                else:
                    #draw.line(screen,col,(mx+penThick,my-penThick),(mx-penThick,my+penThick),3)
                    surf4.set_alpha(int(penrOpacity/220*255))
                    screen.blit(surf3,(mx-surf3.get_width()//2,my-surf3.get_height()//2))

        pRandNum=randNum #pRandNum and randNum become equal if user holds the mouse down for a longer period of time
        pmx = mx
        pmy = my

        if tool=="Fill" and canvasRect.collidepoint(mx,my):
            spots=[]
            spots.append((sx,sy))
            fillCol = screen.get_at((sx,sy))
            if fillCol!=col:
                while len(spots)>0:
                    fx,fy = spots.pop()
                    if screen.get_at((fx,fy)) == fillCol and canvasRect.collidepoint(fx,fy):
                        screen.set_at((fx,fy),col)
                        spots+=[(fx,fy-1),(fx,fy+1),(fx-1,fy),(fx+1,fy)]


        if tool=="Text" and subTool=="None" and ribbon=="None" and canvasRect.collidepoint(mx,my):
            txt=TextInput.TextInput(screen,mx,my,canvasRect)
            txt.drawText(textCol,TextTool.getFont().getFontName(),TextTool.getTextSize().getSize(),TextTool.getBold().getSelected(),
                         TextTool.getItalics().getSelected(),TextTool.getUnderline().getSelected(),TextTool.getStrike().getSelected())
                
        screen.set_clip(None)
    omx=mx
    omy=my

    ####################################################################
    #SHAPES ON THE CANVAS

    if mb[0]==1 and subTool=="None":
        screen.set_clip(canvasRect)
        if tool=='Shape':
            if shape=="Line":
                screen.blit(canvasBuff, (447,92))
                
                if keys[K_LSHIFT] or keys[K_RSHIFT]:#STRAIGHT LINE (VER/HOR)
                    xDiff=sx-mx
                    yDiff=sy-my
                    if xDiff<0:
                        xDiff*=-1
                    if yDiff<0:
                        yDiff*=-1
                    if xDiff<=yDiff:
                        draw.line(screen, col, (sx,sy),(sx,my),3)
                    elif yDiff<=xDiff:
                        draw.line(screen, col, (sx,sy),(mx,sy),3)
                        
                else: #NORMAL LINE (ANY DIRECTION)
                    draw.line(screen, col, (sx,sy),(mx,my),3)
            
            if shape=="Rectangle":
                if keys[K_LSHIFT] or keys[K_RSHIFT]:#SQUARE
                    screen.blit(canvasBuff, (447,92))
                    rectMin=min(mx-sx,my-sy)
                    if mx<sx and my>sy:
                        draw.rect(screen,col,(sx,sy,rectMin,rectMin*-1),radius)
                    elif mx>sx and my<sy:
                        draw.rect(screen,col,(sx,sy,rectMin*-1,rectMin),radius)
                    elif mx>sx and my>sy:
                        draw.rect(screen,col,(sx,sy,rectMin,rectMin),radius)
                    elif mx<sx and my<sy:
                        rectMin=max(mx-sx,my-sy)
                        draw.rect(screen,col,(sx,sy,rectMin,rectMin),radius)
                    screenBuff=screen.copy()
                    
                else:#RECTANGLE
                    if evnt.type == MOUSEBUTTONUP:
                        screen.blit(canvasBuff, (447,92))
                        draw.rect(screen, col, (sx,sy,mx-sx,my-sy),radius)
                        screenBuff = screen.copy()

                    screen.blit(canvasBuff, (447,92))
                    if mb[0]==1:
                        draw.rect(screen, col, (sx,sy,mx-sx,my-sy),radius)
                    
            if shape=="Ellipse":
                if keys[K_LSHIFT] or keys[K_RSHIFT]:#CIRCLE

                    ellMin=min(mx-sx,my-sy)
                    if mx<sx and my>sy:
                        ellRect=Rect(sx,sy,ellMin,ellMin*-1)
                    elif mx>sx and my<sy:
                        ellRect=Rect(sx,sy,ellMin*-1,ellMin)
                    elif mx>sx and my>sy:
                        ellRect=Rect(sx,sy,ellMin,ellMin)
                    elif mx<sx and my<sy:
                        ellMin=max(mx-sx,my-sy)
                        ellRect=Rect(sx,sy,ellMin,ellMin)
                    
                    if evnt.type == MOUSEBUTTONUP:
                        screen.blit(canvasBuff, (447,92))
                        screenBuff = screen.copy()
                        
                    screen.blit(canvasBuff, (447,92))
                    
                    if mb[0]==1 and ((sx-mx)>5 or (sx-mx)<-5) and ((sy-my)>5 or (sy-my)<-5):
                        ellRect.normalize()
                        draw.ellipse(screen, col, ellRect,radius) #draw a new line
                        
                else:#ELLIPSE
                    ellRect=Rect(sx,sy,mx-sx,my-sy)
                    ellRect.normalize()
                    if evnt.type == MOUSEBUTTONUP:
                        screen.blit(canvasBuff, (447,92))
                        screenBuff = screen.copy()
                    screen.blit(canvasBuff, (447,92))
                    if mb[0]==1 and ((sx-mx)>5 or (sx-mx)<-5) and ((sy-my)>5 or (sy-my)<-5):
                        draw.ellipse(screen, col, ellRect,radius) #draw a new line
            
            if shape=="Triangle":
                if evnt.type == MOUSEBUTTONUP:
                    screen.blit(canvasBuff, (447,92))
                    if my>sy:
                        draw.polygon(screen,col,((sx+((mx-sx)//2),sy),(sx,my),(mx,my)),radius)
                    else:
                        draw.polygon(screen,col,((mx+((sx-mx)//2),my),(mx,sy),(sx,sy)),radius)
                    screenBuff = screen.copy()

                screen.blit(canvasBuff, (447,92))
                if mb[0]==1:
                    if my>sy:
                        draw.polygon(screen, col, ((sx+((mx-sx)//2),sy),(sx,my),(mx,my)),radius)
                    else:
                        draw.polygon(screen, col, ((mx+((sx-mx)//2),my),(mx,sy),(sx,sy)),radius)

            if shape=="Pentagon":
                if evnt.type == MOUSEBUTTONUP:
                    screen.blit(canvasBuff, (447,92))
                    if my>sy:
                        draw.polygon(screen, col, ((sx+((mx-sx)//2),sy),(sx,sy+(my-sy)//2),((sx+((mx-sx)//5)),my),((sx+((mx-sx)//5)*4),my),(mx,sy+(my-sy)//2)),radius)
                    else:
                        draw.polygon(screen, col, ((mx+((sx-mx)//2),my),(mx,my+(sy-my)//2),((mx+((sx-mx)//5)),sy),((mx+((sx-mx)//5)*4),sy),(sx,my+(sy-my)//2)),radius)
                    screenBuff = screen.copy()

                screen.blit(canvasBuff, (447,92))
                if mb[0]==1:
                    if my>sy:
                        draw.polygon(screen, col, ((sx+((mx-sx)//2),sy),(sx,sy+(my-sy)//2),((sx+((mx-sx)//5)),my),((sx+((mx-sx)//5)*4),my),(mx,sy+(my-sy)//2)),radius)
                    else:
                        draw.polygon(screen, col, ((mx+((sx-mx)//2),my),(mx,my+(sy-my)//2),((mx+((sx-mx)//5)),sy),((mx+((sx-mx)//5)*4),sy),(sx,my+(sy-my)//2)),radius)

            if shape=="Hexagon":
                if evnt.type == MOUSEBUTTONUP:
                    screen.blit(canvasBuff, (447,92))
                    draw.polygon(screen, col, (((sx+((mx-sx)//5)*4),sy),((sx+((mx-sx)//5)),sy),(sx,sy+(my-sy)//2),((sx+((mx-sx)//5)),my),((sx+((mx-sx)//5)*4),my),(mx,sy+(my-sy)//2)),radius)
                    screenBuff = screen.copy()

                screen.blit(canvasBuff, (447,92))
                if mb[0]==1:
                    draw.polygon(screen, col, (((sx+((mx-sx)//5)*4),sy),((sx+((mx-sx)//5)),sy),(sx,sy+(my-sy)//2),((sx+((mx-sx)//5)),my),((sx+((mx-sx)//5)*4),my),(mx,sy+(my-sy)//2)),radius)

            if shape=="Octogon":
                    if evnt.type == MOUSEBUTTONUP:
                        screen.blit(canvasBuff, (447,92))
                        draw.polygon(screen, col,((sx+(mx-sx)//4,sy),(sx+((mx-sx)//4)*3,sy),(mx,my-(my-sy)//4*3),(mx,my-(my-sy)//4),(mx-(mx-sx)//4,my),(mx-(mx-sx)//4*3,my),(sx,sy+(my-sy)//4*3),(sx,sy+(my-sy)//4)),radius)
                        screenBuff = screen.copy()

                    screen.blit(canvasBuff, (447,92))
                    if mb[0]==1:
                        draw.polygon(screen, col,((sx+(mx-sx)//4,sy),(sx+((mx-sx)//4)*3,sy),(mx,my-(my-sy)//4*3),(mx,my-(my-sy)//4),(mx-(mx-sx)//4,my),(mx-(mx-sx)//4*3,my),(sx,sy+(my-sy)//4*3),(sx,sy+(my-sy)//4)),radius)

            if shape=="Diamond":
                    if evnt.type == MOUSEBUTTONUP:
                        screen.blit(canvasBuff, (447,92))
                        draw.polygon(screen, col,((mx,sy+(my-sy)//2),(sx+(mx-sx)//2,my),(sx,sy+(my-sy)//2),(sx+(mx-sx)//2,sy)),radius)
                        screenBuff = screen.copy()

                    screen.blit(canvasBuff, (447,92))
                    if mb[0]==1:
                        draw.polygon(screen, col,((mx,sy+(my-sy)//2),(sx+(mx-sx)//2,my),(sx,sy+(my-sy)//2),(sx+(mx-sx)//2,sy)),radius)

            if shape=="Right Triangle": #right angle triangle
                    if evnt.type == MOUSEBUTTONUP:
                        screen.blit(canvasBuff, (447,92))
                        if my>sy:
                            draw.polygon(screen, col,((sx,sy),(sx,my),(mx,my)),radius)
                        else:
                            draw.polygon(screen, col,((sx,sy),(mx,sy),(mx,my)),radius)
                        screenBuff = screen.copy()

                    screen.blit(canvasBuff, (447,92))
                    if mb[0]==1:
                        if my>sy:
                            draw.polygon(screen, col,((sx,sy),(sx,my),(mx,my)),radius)
                        else:
                            draw.polygon(screen, col,((sx,sy),(mx,sy),(mx,my)),radius)

            #POLYGON TOOL
            if shape=="Custom" and canvasRect.collidepoint(mx,my):
                if custom==False and subTool!="Edit Clear" and subTool!="File New":
                    CustomShape.getScreenShot(Rect(447,92,776,676))
                CustomShape.drawLine(mx,my,col)
                custom=True
                
        screen.set_clip(None)

    if shape=="Custom" and custom:
        if keys[K_RETURN] or keys[K_KP_ENTER]:
                CustomShape.stopDrawing(col,customRadius)
                custom=False
                
    if custom and (shape!="Custom" or tool!="Shape" or ribbon!="None"):
        CustomShape.stopDrawing(col,customRadius)
        custom=False

    ##################################################

    #SCREENSHOT
    if ribbon=="None" and subTool!="View Mode":
        screenBuff=screen.copy()

    ##################################################
        
    #USING RIBBONS
    #FILE
    if ribbon=="File" and subTool!="View Mode":
        screen.blit(screenBuff,(0,0))
        draw.rect(screen,medBlue,fileTab)
        draw.rect(screen,white,[9,14,82,27])
        display.text=ribbonFont.render("FILE",True,darkBlue)
        screen.blit(display.text,(28,16))
        switched=True

        draw.rect(screen,medBlue,[5,41,170,128])
        draw.rect(screen,white,fileNewRect)
        draw.rect(screen,white,fileOpenRect)
        draw.rect(screen,white,fileSaveRect)
        draw.rect(screen,white,fileSaveAsRect)

        #NAME DISPLAY
        display.text=ribbonFont.render("New",True,darkBlue)
        screen.blit(display.text,(14,47))
        display.text=ribbonFont2.render("Ctrl+N",True,darkBlue)
        screen.blit(display.text,(123,50))
        
        display.text=ribbonFont.render("Open",True,darkBlue)
        screen.blit(display.text,(14,78))
        display.text=ribbonFont2.render("Ctrl+O",True,darkBlue)
        screen.blit(display.text,(123,81))
        
        display.text=ribbonFont.render("Save",True,darkBlue)
        screen.blit(display.text,(14,109))
        display.text=ribbonFont2.render("Ctrl+S",True,darkBlue)
        screen.blit(display.text,(123,112))
        
        display.text=ribbonFont.render("Save As",True,darkBlue)
        screen.blit(display.text,(14,140))
        display.text=ribbonFont2.render("Ctrl+Shft+S",True,darkBlue)
        screen.blit(display.text,(91,143))

        
        if fileNewRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,50))
            screen.blit(rect,(9,45))
            if mb[0]==1:
                subTool="File New"
                display.set_caption("Untitled")
                saved=False

        if fileOpenRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(9,76))
            if mb[0]==1:
                fName=filedialog.askopenfilename(filetypes=[("images",".png;*.bmp;*.jpg;*.jpeg")])
                del redoList[0:]
                del undoList[-1]
                subTool="File Open"

        if fileSaveRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(9,107))
            if mb[0]==1:
                if not saved:
                    fName=filedialog.asksaveasfilename(defaultextension=".png")
                    display.set_caption(fName)
                    saved=True
                if saved:
                    image.save(screen.subsurface(canvasRect),fName)

        if fileSaveAsRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(9,138))
            if mb[0]==1:
                fName=filedialog.asksaveasfilename(defaultextension=".png")
                display.set_caption(fName)
                saved=True
        
        if mb[0]==1 and not fileTab.collidepoint(mx,my):
            ribbon="None"
            screen.blit(screenBuff,(0,0))

    #FILE KEYBOARD ALTERNATIVES
    if subTool!="View Mode":
        if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_n]:#NEW
            subTool="File New"
            display.set_caption("Untitled")
            saved=False
                
        if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_o]:#OPEN
            fName=filedialog.askopenfilename(filetypes=[("images",".png;*.bmp;*.jpg;*.jpeg")])
            del redoList[0:]
            del undoList[-1]
            subTool="File Open"
            display.set_caption(fName)

        if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_s]:#SAVE
            if not saved:
                fName=filedialog.asksaveasfilename(defaultextension=".png")
                display.set_caption(fName)
                saved=True
            if saved:
                image.save(screen.subsurface(canvasRect),fName)

        if (keys[K_LCTRL] or keys[K_RCTRL]) and (keys[K_LSHIFT] or keys[K_RSHIFT]) and keys[K_s]:#SAVE AS
                fName=filedialog.asksaveasfilename(defaultextension=".png")
                display.set_caption(fName)
                saved=True

    ##################################################

    #EDIT
    if ribbon=="Edit" and subTool!="View Mode":
        screen.blit(screenBuff,(0,0))
        draw.rect(screen,medBlue,editTab)
        draw.rect(screen,white,[104,14,82,27])
        display.text=ribbonFont.render("EDIT",True,darkBlue)
        screen.blit(display.text,(123,16))
        switched=True
    
        draw.rect(screen,medBlue,[100,41,170,128])
        draw.rect(screen,white,editUndoRect)
        draw.rect(screen,white,editRedoRect)
        draw.rect(screen,white,editClearRect)
        draw.rect(screen,white,editTransformRect)

        #NAME DISPLAY
        display.text=ribbonFont.render("Undo",True,darkBlue)
        if len(undoList)<=2 or custom:
            display.text=ribbonFont.render("Undo",True,grayBlue)
        screen.blit(display.text,(109,47))
        display.text=ribbonFont2.render("Ctrl+Z",True,darkBlue)
        if len(undoList)<=2 or custom:
            display.text=ribbonFont2.render("Ctrl+Z",True,grayBlue)
        screen.blit(display.text,(218,50))
        
        display.text=ribbonFont.render("Redo",True,darkBlue)
        if len(redoList)==0 or custom:
            display.text=ribbonFont.render("Redo",True,grayBlue)
        screen.blit(display.text,(109,78))
        display.text=ribbonFont2.render("Ctrl+Y",True,darkBlue)
        if len(redoList)==0 or custom:
            display.text=ribbonFont2.render("Ctrl+Y",True,grayBlue)
        screen.blit(display.text,(218,81))
        
        display.text=ribbonFont.render("Clear",True,darkBlue)
        screen.blit(display.text,(108,109))

        display.text=ribbonFont.render("Transform",True,darkBlue)
        screen.blit(display.text,(108,140))
        draw.polygon(screen,darkBlue,((253,146),(253,156),(258,151)))

        if mb[0]==1 and not editTab.collidepoint(mx,my):
            ribbon="None"
            screen.blit(screenBuff,(0,0))

        if editUndoRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(104,45))
            if mb[0]==1 and len(undoList)>2 and undo==False:
                redoList.append(undoList[-1])
                del undoList[-1]
                screen.blit(undoList[-1],(447,92))
                undo=True
                undid=True
                
        if editRedoRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(104,76))
            if mb[0]==1 and len(redoList)>=1 and undo==False:
                screen.blit(redoList[-1],(447,92))
                undoList.append(redoList[-1])
                del redoList[-1]
                undo=True
                undid=True
        
        if editClearRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(104,107))
            if mb[0]==1:
                canvasBuff=screen.subsurface(canvasRect).copy()
                subTool="Edit Clear"

        if editTransformRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(104,138))
            transformTab=True

        if editTransformRect.collidepoint(mx,my) or transformRect.collidepoint(mx,my): #TRANSFORM CANVAS
            if transformTab:
                draw.rect(screen,medBlue,transformRect)
                draw.rect(screen,white,lRotateRect)
                draw.rect(screen,white,rRotateRect)
                draw.rect(screen,white,hFlipRect)
                draw.rect(screen,white,vFlipRect)

                display.text=ribbonFont.render("Rotate Left",True,darkBlue)
                screen.blit(display.text,(275,140))
                display.text=ribbonFont.render("Rotate Right",True,darkBlue)
                screen.blit(display.text,(275,171))
                display.text=ribbonFont.render("Horizontal Flip",True,darkBlue)
                screen.blit(display.text,(275,202))
                display.text=ribbonFont.render("Vertical Flip",True,darkBlue)
                screen.blit(display.text,(275,233))

                if lRotateRect.collidepoint(mx,my):
                    rect=Surface((162,27), SRCALPHA, 32)
                    rect.fill((200,200,200,70))
                    screen.blit(rect,(270,138))
                    if mb[0]==1:
                        canvasBuff=screen.subsurface(canvasRect).copy()
                        canvasBuff=transform.rotate(canvasBuff,90)
                        canvasBuff=transform.scale(canvasBuff,(776,676))

                        screen.blit(canvasBuff,(447,92))
                        undoList.append(screen.subsurface(canvasRect).copy())

                if rRotateRect.collidepoint(mx,my):
                    rect=Surface((162,27), SRCALPHA, 32)
                    rect.fill((200,200,200,70))
                    screen.blit(rect,(270,169))
                    if mb[0]==1:
                        canvasBuff=screen.subsurface(canvasRect).copy()
                        canvasBuff=transform.rotate(canvasBuff,270)
                        canvasBuff=transform.scale(canvasBuff,(776,676))

                        screen.blit(canvasBuff,(447,92))
                        undoList.append(screen.subsurface(canvasRect).copy())

                if hFlipRect.collidepoint(mx,my):
                    rect=Surface((162,27), SRCALPHA, 32)
                    rect.fill((200,200,200,70))
                    screen.blit(rect,(270,200))
                    if mb[0]==1:
                        canvasBuff=screen.subsurface(canvasRect).copy()
                        canvasBuff=transform.flip(canvasBuff,False,True)
                        canvasBuff=transform.scale(canvasBuff,(776,676))

                        screen.blit(canvasBuff,(447,92))
                        undoList.append(screen.subsurface(canvasRect).copy())

                if vFlipRect.collidepoint(mx,my):
                    rect=Surface((162,27), SRCALPHA, 32)
                    rect.fill((200,200,200,70))
                    screen.blit(rect,(270,231))
                    if mb[0]==1:
                        canvasBuff=screen.subsurface(canvasRect).copy()
                        canvasBuff=transform.flip(canvasBuff,True,False)
                        canvasBuff=transform.scale(canvasBuff,(776,676))

                        screen.blit(canvasBuff,(447,92))
                        undoList.append(screen.subsurface(canvasRect).copy())

        if not editTransformRect.collidepoint(mx,my) and not transformRect.collidepoint(mx,my):
            transformTab=False
                                
        if mb[0]==1 and not editTab.collidepoint(mx,my):
                ribbon="None"
                screen.blit(screenBuff,(0,0))
                screen.blit(undoList[-1],(447,92))

    ######################################################

    #EDIT ALT KEYS
    if subTool!="View Mode" and currentStamp=="None" and ribbon=="None" and not custom and not selected and not moveSelected and not placeSelected:
        if keys[K_LCTRL] and keys[K_z] and undo==False:
            if len(undoList)>2:
                redoList.append(undoList[-1])
                del undoList[-1]
                screen.blit(undoList[-1],(447,92))
                undid=True
            else:
                error.set_volume(0.1)
                error.play()
            undo=True
        
        if keys[K_LCTRL] and keys[K_y] and undo==False:
            if len(redoList)>=1:
                screen.blit(redoList[-1],(447,92))
                undoList.append(redoList[-1])
                del redoList[-1]
                undid=True
            else:
                error.set_volume(0.1)
                error.play()
            undo=True
        
        if not keys[K_y] and not keys[K_z]:
            undo=False

    ##################################################

    #VIEW
    if ribbon=="View":
        screen.blit(screenBuff,(0,0))
        draw.rect(screen,medBlue,viewTab)
        draw.rect(screen,white,[199,14,82,27])
        display.text=ribbonFont.render("VIEW",True,darkBlue)
        screen.blit(display.text,(214,16))
    
        draw.rect(screen,medBlue,[195,41,170,66])
        draw.rect(screen,white,viewModeRect)
        draw.rect(screen,white,viewShortcutRect)
        
        #NAME DISPLAY
        display.text=ribbonFont.render("Full Screen",True,darkBlue)
        screen.blit(display.text,(205,47))
        display.text=ribbonFont2.render("Ctrl+F",True,darkBlue)
        screen.blit(display.text,(315,50))
        display.text=ribbonFont.render("Shortcut Keys",True,darkBlue)
        screen.blit(display.text,(205,78))

        if viewModeRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(199,45))
            if mb[0]==1 and fullScreen==False:
                canvasBuff=screen.subsurface(canvasRect).copy()
                subTool="View Mode"

        if viewShortcutRect.collidepoint(mx,my):
            rect=Surface((162,27), SRCALPHA, 32)
            rect.fill((200,200,200,70))
            screen.blit(rect,(199,76))
            if mb[0]==1:
                menuBuff=screen.subsurface(canvasRect).copy()
                subTool="View Shortcut"

        if mb[0]==1 and not viewTab.collidepoint(mx,my):
            ribbon="None"
            screen.blit(screenBuff,(0,0))

    #VIEW ALT KEYS
    if (keys[K_LCTRL] or keys[K_RCTRL]) and keys[K_f] and fullScreen==False:
        canvasBuff=screen.subsurface(canvasRect).copy()
        subTool="View Mode"

    ##################################################
        
    ###SUBTOOLS
    if subTool=="File New":
        canvasBuff=screen.subsurface(canvasRect).copy()
        draw.rect(screen,darkBlue,[700,300,250,100])
        draw.rect(screen,lightBlue,[700,300,250,100],3)
        display.text=ribbonFont.render("Do you want to save?",True,white)
        screen.blit(display.text,(735,315))
        draw.rect(screen,lightBlue,yesClearRect,3)
        display.text=ribbonFont.render("Yes",True,white)
        screen.blit(display.text,(752,354))
        draw.rect(screen,lightBlue,noClearRect,3)
        display.text=ribbonFont.render("No",True,white)
        screen.blit(display.text,(862,354))

        if yesClearRect.collidepoint(mx,my):
            rect=Surface((80,30), SRCALPHA, 32)
            rect.fill((230,230,230,50))
            screen.blit(rect,(730,350))
            if evnt.type==MOUSEBUTTONUP:
                screen.blit(canvasBuff,(447,92))
                if not saved:
                    fName=filedialog.asksaveasfilename(defaultextension=".png")
                    saved=False
                if saved:
                    image.save(screen.subsurface(canvasRect),fName)

                del undoList[2:]
                del redoList[0:]
                draw.rect(screen,white,canvasRect)
                subTool="None"
                
        if noClearRect.collidepoint(mx,my):
            rect=Surface((80,30), SRCALPHA, 32)
            rect.fill((230,230,230,50))
            screen.blit(rect,(835,350))
            if evnt.type==MOUSEBUTTONUP:
                draw.rect(screen,white,canvasRect)
                del undoList[2:]
                del redoList[0:]
                subTool="None"
        
    if subTool=="File Open":
        if fName!="": #Opening a file
            fNameImg=image.load(fName)
            if fNameImg.get_width()>776 or fNameImg.get_height()>676:
                maxSide=max(fNameImg.get_width(),fNameImg.get_height())
                if maxSide==fNameImg.get_width():
                    openScale=776/fNameImg.get_width()
                    fNameImg=transform.scale(fNameImg,(776,int(fNameImg.get_height()*openScale)))
                elif maxSide==fNameImg.get_height():
                    openScale=676/fNameImg.get_height()
                    fNameImg=transform.scale(int(fNameImg.get_width()*openScale,676))

            undoList.append(screen.subsurface(canvasRect).copy())
            screen.blit(fNameImg,(447,92))
            undoList.append(screen.subsurface(canvasRect).copy())
            canvasBuff=screen.subsurface(canvasRect).copy()
            subTool="None"
        else:
            subTool="None"
    

    if subTool=="Edit Clear": #asks yes or no
        draw.rect(screen,darkBlue,[700,300,250,100])
        draw.rect(screen,lightBlue,[700,300,250,100],3)
        display.text=ribbonFont.render("Are you Sure?",True,white)
        screen.blit(display.text,(765,315))
        draw.rect(screen,lightBlue,yesClearRect,3)
        display.text=ribbonFont.render("Yes",True,white)
        screen.blit(display.text,(752,354))
        draw.rect(screen,lightBlue,noClearRect,3)
        display.text=ribbonFont.render("No",True,white)
        screen.blit(display.text,(862,354))
        
        if yesClearRect.collidepoint(mx,my):
            rect=Surface((80,30), SRCALPHA, 32)
            rect.fill((230,230,230,50))
            screen.blit(rect,(730,350))
            if evnt.type==MOUSEBUTTONUP:
                if undid==True:
                    del redoList[0:]
                    undid=False
                draw.rect(screen,white,canvasRect)
                undoList.append(screen.subsurface(canvasRect).copy())
                subTool="None"
            
        if noClearRect.collidepoint(mx,my):
            rect=Surface((80,30), SRCALPHA, 32)
            rect.fill((230,230,230,50))
            screen.blit(rect,(835,350))
            if evnt.type==MOUSEBUTTONUP:
                screen.blit(canvasBuff,(447,92))
                subTool="None"

    if subTool=="View Mode": #screen for full screen
        screen.fill((cyan))
        scale=height/676
        display.text=ribbonFont2.render("Press ESC to exit full screen",True,darkBlue)
        fullScreen=True
        
        fullCanvas=transform.scale(canvasBuff,(int(776*scale),height))
        screen.blit(fullCanvas,(int(width/2-(388*scale)),0))
        draw.rect(screen,white,[int(width/2-(388*scale))+5,5,185,30])
        draw.rect(screen,darkBlue,[int(width/2-(388*scale))+5,5,185,30],2)
        screen.blit(display.text,(int(width/2-(388*scale))+10,10))
        if keys[K_ESCAPE]:
            screen.blit(screenBuff,(0,0))
            subTool="None"
            fullScreen=False

    if subTool=="View Shortcut": #screen for all the shortcut keys
        ShortcutMenu.ShortcutMenu(titleFont,ribbonFont,ribbonFont2,darkBlue,screen)
        if keys[K_ESCAPE]:
            screen.blit(menuBuff,(447,92))
            subTool="None"

    ##################################################
            
    display.flip() 


quit()
