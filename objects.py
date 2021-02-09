import colors
import pygame
import globals

class object:
    def __init__(self, color):
        self.color = color

bg_tile = pygame.transform.scale(pygame.image.load('assets/decors/sol.png'), (globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT))

mur = object(colors.DARK_GREY)

a = object(colors.CYAN)
b = object(colors.RED)
c = object(colors.GREEN)
d = object(colors.YELLOW)
e = object(colors.BLUE)

objArr = [mur, a, b, c, d, e]

wallSprites = []

def loadSprites():
    global wallSprites
    for i in range(29):
        img = pygame.image.load("assets/wall/" + str(i) + ".png")
        img = pygame.transform.scale(img, (globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT))
        img.convert()
        wallSprites.append(img)


def draw(num, x, y):
    rect = pygame.Rect(globals.calcX(x) - globals.marginLeft, globals.calcY(y) - globals.marginTop, globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT)
    if (num == 0):
        globals.WIN.blit(wallSprites[0], rect)
        drawBorder(rect, x, y)
    else :
        pygame.draw.rect(globals.WIN, objArr[num].color, rect)

def drawBorder(rect, x, y):
    BD_WIDTH = int(globals.OBJECT_WIDTH/4)
    BD_COLOR = colors.GREEN
    
    top = y == 0 or not globals.LVL[y-1][x]
    left = x == 0 or not globals.LVL[y][x-1]
    right = x == len(globals.LVL[y])-1 or not globals.LVL[y][x+1]
    bottom = y == len(globals.LVL)-1 or not globals.LVL[y+1][x]

    #BORDERS
    #top
    if (top):
        globals.WIN.blit(wallSprites[1], rect)
    else:
        globals.WIN.blit(wallSprites[2], rect)
    #left
    if (left):
        globals.WIN.blit(wallSprites[3], rect)
    else:
        globals.WIN.blit(wallSprites[4], rect)
    #right
    if (right):
        globals.WIN.blit(wallSprites[5], rect)
    else:
        globals.WIN.blit(wallSprites[6], rect)
    #bottom
    if (bottom):
        globals.WIN.blit(wallSprites[7], rect)
    else:
        globals.WIN.blit(wallSprites[8], rect)

    #CORNERS
    #top left
    if (top and left):
        globals.WIN.blit(wallSprites[9], rect)
    elif (top and not left):
        globals.WIN.blit(wallSprites[17], rect)
    elif (not top and left):
        globals.WIN.blit(wallSprites[18], rect)
    else:
        if (globals.LVL[y-1][x-1]):
            globals.WIN.blit(wallSprites[10], rect)
        else :
            globals.WIN.blit(wallSprites[25], rect)

    #top right
    if (top and right):
        globals.WIN.blit(wallSprites[11], rect)
    elif (top and not right):
        globals.WIN.blit(wallSprites[19], rect)
    elif (not top and right):
        globals.WIN.blit(wallSprites[20], rect)
    else:
        if (globals.LVL[y-1][x+1]):
            globals.WIN.blit(wallSprites[12], rect)
        else:
            globals.WIN.blit(wallSprites[26], rect)

    #bottom left
    if (bottom and left):
        globals.WIN.blit(wallSprites[13], rect)
    elif (bottom and not left):
        globals.WIN.blit(wallSprites[21], rect)
    elif (not bottom and left):
        globals.WIN.blit(wallSprites[22], rect)
    else:
        if (globals.LVL[y+1][x-1]):
            globals.WIN.blit(wallSprites[14], rect)
        else:
            globals.WIN.blit(wallSprites[27], rect)

    #bottom right
    if (bottom and right):
        globals.WIN.blit(wallSprites[15], rect)
    elif (bottom and not right):
        globals.WIN.blit(wallSprites[23], rect)
    elif (not bottom and right):
        globals.WIN.blit(wallSprites[24], rect)
    else:
        if (globals.LVL[y+1][x+1]):
            globals.WIN.blit(wallSprites[16], rect)
        else:
            globals.WIN.blit(wallSprites[28], rect)

def drawBG():
    bg_tile.convert()
    for x in range(0,globals.GAME_WIDTH):
        for y in range(0,globals.GAME_HEIGHT):
            globals.WIN.blit(bg_tile, (globals.calcX(x), globals.calcY(y)))
