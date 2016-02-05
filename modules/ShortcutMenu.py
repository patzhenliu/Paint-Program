from pygame import *

def ShortcutMenu(titleFont,ribbonFont,ribbonFont2,darkBlue,screen):
    draw.rect(screen,(255,255,255),[650,180,380,465])
    draw.rect(screen,darkBlue,[650,180,380,465],3)
    display.text=titleFont.render("Shortcut Keys",True,darkBlue)
    screen.blit(display.text,(765,188))
    draw.line(screen,darkBlue,(660,220),(1020,220),4)
        
    nameList1=["New","Open","Save","Save As","Undo","Redo","Full Screen"]
    keyList1=["Ctrl+N","Ctrl+O","Ctrl+S","Ctrl+Shft+S","Ctrl+Z","Ctrl+Y","Ctrl+F"]
    for i in range(7):
        display.text=ribbonFont.render(nameList1[i],True,darkBlue)
        screen.blit(display.text,(675,230+20*i))
 
        display.text=ribbonFont.render(keyList1[i],True,darkBlue)
        screen.blit(display.text,(915,230+20*i))

    nameList2=["Palette","Cursor","Pencil","Eraser","Paint Brush","Spray Paint","Pen","Fill Bucket","Text Box","Shapes/Line","Stamps"]
    keyList2=["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11"]
    for i in range(11):
        display.text=ribbonFont.render(nameList2[i],True,darkBlue)
        screen.blit(display.text,(675,380+20*i))

        display.text=ribbonFont.render(keyList2[i],True,darkBlue)
        screen.blit(display.text,(915,380+20*i))

    display.text=ribbonFont2.render("Click ESC to exit",True,darkBlue)
    screen.blit(display.text,(775,620))
