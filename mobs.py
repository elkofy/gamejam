import pygame
import globals
from globals import *
import tile
from tile import *
from enum import Enum
mobs = []
class Directions(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3
class Mob(tile.Tile):
    sort = None
    speed = 30
    walking = False
    walking_sound = None
    death_sound = None

    def __init__(self, x, y, sort, dir, nbS):
        global mobs
        Tile.__init__(self, x, y)
        self.animTime = 0
        self.walkTime = 0
        self.sort = sort
        self.setDir(dir)
        self.nbS = nbS
        self.endCheck = False
        self.walkRect = self.rect.copy()
        mobs.append(self)
        self.walking_sound = pygame.mixer.Sound("assets/sounds/mob1.wav")
        self.walking_sound.set_volume(0.2)
        self.death_sound = pygame.mixer.Sound("assets/sounds/mob2.wav")
        self.death_sound.set_volume(0.2)

    def setDir(self, dir):
        self.dir = dir
        if self.dir == "u":
            self.dirX = 0
            self.dirY = -1
        elif self.dir == "l":
            self.dirX = -1
            self.dirY = 0
        elif self.dir == "r":
            self.dirX = 1
            self.dirY = 0
        elif self.dir == "d":
            self.dirX = 0
            self.dirY = 1

    def draw(self):
        Tile.draw(self)

    def drawMob(self):
        globals.WIN.blit(sl["m_" + self.sort + "_" + self.dir + "_" + str(int(self.animTime/globals.TIME_MONSTER * self.nbS))], (self.walkRect if self.walking else self.rect))


    def move(self):
        if self.walkTime >= globals.TIME_WALK:
            self.walkTime = 0
            if type(globals.MAP[self.y + self.dirY][self.x + self.dirX]) is tile.Trap:
                self.death()
            else:
                if type(globals.MAP[self.y + self.dirY][self.x + self.dirX]) is Mob:
                    globals.MAP[self.y + self.dirY][self.x + self.dirX].death()
                globals.MAP[self.y][self.x] = tile.Tile(self.x, self.y)
                self.x = self.x + self.dirX
                self.y = self.y + self.dirY
                globals.MAP[self.y][self.x] = self
            
            self.endCheck = globals.isWall(self.x + self.dirX, self.y + self.dirY)
            self.walking = not self.endCheck
        else:
            self.walkTime += globals.LT
            self.walkRect.x = globals.calcX(self.x) - globals.marginLeft + self.dirX * (self.walkTime / globals.TIME_WALK * globals.OBJECT_WIDTH)
            self.walkRect.y = globals.calcY(self.y) - globals.marginTop + self.dirY * (self.walkTime / globals.TIME_WALK * globals.OBJECT_WIDTH)

    def act(self):
        self.animTime = (self.animTime + globals.LT) % globals.TIME_MONSTER

        if globals.PLAYER.getCurrentTile() == self:
            globals.PLAYER.death()

        if not self.endCheck:
            if self.walking:
                self.move()
            else:
                if self.isPlayerVisible():
                    self.walking = True
                    self.walking_sound.play()
                    
    def isPlayerVisible(self):
        x = self.x + self.dirX
        y = self.y + self.dirY
        
        while not globals.isWall(x, y):
            if x == globals.PLAYER.x and y == globals.PLAYER.y:
                return True
            else:
                x = x + self.dirX
                y = y + self.dirY

        return False
        
    def death(self):
        self.death_sound.play()
        mobs.remove(self)
        self = tile.Tile(self.x, self.y)