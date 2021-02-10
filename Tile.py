import pygame
import globals
from sprites import sl

chars = {
    " " : "empty",
    "s" : "spawn",
    "b" : "bed",
    "@" : "wall",
    "t" : "tomato",
    "k" : "kiwi"
}

class Tile:
    x = None
    y = None
    rect = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(globals.calcX(x), globals.calcY(y), globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT)

    def updatePos(self):
        self.rect.x = globals.calcX(self.x) - globals.marginLeft
        self.rect.y = globals.calcY(self.y) - globals.marginTop

    def draw(self):
        globals.WIN.blit(sl['bg_tile'], self.rect)

class Wall(Tile):

    def __init__(self, x, y):
        self.sprites = []

        Tile.__init__(self, x, y)
        
        self.full = sl["wall_0"].copy()

        top = y == 0 or chars[globals.LVL[y-1][x]] != "wall"
        left = x == 0 or chars[globals.LVL[y][x-1]] != "wall"
        right = x == len(globals.LVL[y])-1 or chars[globals.LVL[y][x+1]] != "wall"
        bottom = y == len(globals.LVL)-1 or chars[globals.LVL[y+1][x]] != "wall"

        self.full.blit((sl["wall_1"] if top else sl["wall_2"]), (0, 0))
        self.full.blit((sl["wall_3"] if left else sl["wall_4"]), (0, 0))
        self.full.blit((sl["wall_5"] if right else sl["wall_6"]), (0, 0))
        self.full.blit((sl["wall_7"] if bottom else sl["wall_8"]), (0, 0))

        #CORNERS
        #top left
        if (top and left):
            self.full.blit(sl["wall_9"], (0, 0))
        elif (top and not left):
            self.full.blit(sl["wall_17"], (0, 0))
        elif (not top and left):
            self.full.blit(sl["wall_18"], (0, 0))
        else:
            self.full.blit((sl["wall_10"] if chars[globals.LVL[y-1][x-1]] == "wall" else sl["wall_25"]), (0, 0))

        #top right
        if (top and right):
            self.full.blit(sl["wall_11"], (0, 0))
        elif (top and not right):
            self.full.blit(sl["wall_19"], (0, 0))
        elif (not top and right):
            self.full.blit(sl["wall_20"], (0, 0))
        else:
            self.full.blit((sl["wall_12"] if chars[globals.LVL[y-1][x+1]] == "wall" else sl["wall_26"]), (0, 0))

        #bottom left
        if (bottom and left):
            self.full.blit(sl["wall_13"], (0, 0))
        elif (bottom and not left):
            self.full.blit(sl["wall_21"], (0, 0))
        elif (not bottom and left):
            self.full.blit(sl["wall_22"], (0, 0))
        else:
            self.full.blit((sl["wall_14"] if chars[globals.LVL[y+1][x-1]] == "wall" else sl["wall_27"]), (0, 0))

        #bottom right
        if (bottom and right):
            self.full.blit(sl["wall_15"], (0, 0))
        elif (bottom and not right):
            self.full.blit(sl["wall_23"], (0, 0))
        elif (not bottom and right):
            self.full.blit(sl["wall_24"], (0, 0))
        else:
            self.full.blit((sl["wall_16"] if chars[globals.LVL[y+1][x+1]] == "wall" else sl["wall_28"]), (0, 0))

    def draw(self):
        Tile.draw(self)
        globals.WIN.blit(self.full, self.rect)

class Spawn(Tile):
    def __init__(self, x, y):
        Tile.__init__(self, x, y)

    def draw(self):
        globals.WIN.blit(sl["spawn"], self.rect)

class Fruits(Tile):
    
    def __init__(self, x, y, sort):
        Tile.__init__(self, x, y)
        self.sort = sort

    def draw(self):
        Tile.draw(self)
        globals.WIN.blit(sl["f_" + self.sort], self.rect)

class Bed(Tile):
    def __init__(self, x, y):
        Tile.__init__(self, x, y)

    def draw(self):
        Tile.draw(self)
        globals.WIN.blit(sl["bed"], self.rect)


class Trap(Tile):
    None

