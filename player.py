import pygame
from pygame.locals import*
import colors
import globals
from globals import *
from enum import Enum
import sprites
import time
import tile
import gameover
NB_SPRITE = 16

class Directions(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3

SCALE = (globals.OBJECT_WIDTH - 2 * int((1 - globals.PLAYER_SCALE)/2 * OBJECT_WIDTH), globals.OBJECT_WIDTH - 2 * int((1 - globals.PLAYER_SCALE)/2 * OBJECT_WIDTH))

class Player:
    x = 0 #en unité jeu
    y = 0
    img = sprites.sl["pl_u_s"]
    rect = None
    speed = 5
    energie = MAX_ENERGY
    walking_Cpt = 0

    def resetPos(self):
        self.rect.x = calcX(self.x) - globals.marginLeft + ((1 - globals.PLAYER_SCALE)/2 * globals.OBJECT_WIDTH)
        self.rect.y = calcY(self.y) - globals.marginTop + ((1 - globals.PLAYER_SCALE)/2 * globals.OBJECT_HEIGHT)

    def load(self, x, y):
        self.moving = False
        self.dirr = None
        self.animTime = 0
        self.img.convert()
        self.rect = self.img.get_rect()

        self.x = x
        self.y = y

        self.resetPos()

        globals.WIN.blit(self.img, self.rect)
    
    def getCurrentTile(self):
        return globals.MAP[self.y][self.x]

    def hide(self, dirr):
        self.getCurrentTile().draw()
        if (dirr == "u"):
            globals.MAP[self.y - 1][self.x].draw()
        elif (dirr == "l"):
            globals.MAP[self.y][self.x - 1].draw()
        elif (dirr == "r"):
            globals.MAP[self.y][self.x + 1].draw()
        elif (dirr == "d"):
            globals.MAP[self.y + 1][self.x].draw()

    def draw(self):
        if self.walking_Cpt >= 0:
            self.walking_Cpt -= 1
        if self.energie <= 0:
            #self.img = pygame.image.load('assets/player_dead.png')
            self.img = pygame.transform.scale(self.img, (globals.PLAYER_WIDTH, globals.PLAYER_HEIGHT))
            self.img.convert()
        
        globals.WIN.blit(self.img, self.rect)
    
    def moveAnim(self, dirr):
        self.animTime += globals.LT

        if self.animTime >= globals.TIME_WALK:
            self.moving = False
            self.animTime = 0
            if dirr == "u":
                    self.y -= 1
            elif dirr == "l":
                    self.x -= 1
            elif dirr == "r":
                    self.x += 1
            elif dirr == "d":
                    self.y += 1
            self.img = sprites.sl["pl_" + dirr + "_s"]
            globals.changeView(self.x, self.y)
        else:
            if dirr == "u":
                globals.changeViewY(calcX(self.y) - (HEIGHT / 2) + OBJECT_HEIGHT / 2 - (self.animTime/globals.TIME_WALK * OBJECT_HEIGHT))
            elif dirr == "l":
                globals.changeViewX(calcX(self.x) - (WIDTH / 2) + OBJECT_WIDTH / 2 - (self.animTime/globals.TIME_WALK * OBJECT_WIDTH))
            elif dirr == "r":
                globals.changeViewX(calcX(self.x) - (WIDTH / 2) + OBJECT_WIDTH / 2 + (self.animTime/globals.TIME_WALK * OBJECT_WIDTH))
            elif dirr == "d":
                globals.changeViewY(calcX(self.y) - (HEIGHT / 2) + OBJECT_HEIGHT / 2 + (self.animTime/globals.TIME_WALK * OBJECT_HEIGHT))

            self.img = sprites.sl["pl_" + dirr + "_m_" + str(int((self.animTime/globals.TIME_WALK) * NB_SPRITE))]

    def move(self):
        keys=pygame.key.get_pressed()

        oldX = self.x
        oldY = self.y

        if not self.moving:
            if keys[K_z] or keys[K_UP]:
                if (globals.NOCLIP and self.y > 0) or not isWall(self.x, self.y -1):
                    self.moving = True
                    self.dirr = "u"
                    self.energie -= 1
                self.img = sprites.sl["pl_u_s"]
            elif keys[K_s] or keys[K_DOWN]:
                if(globals.NOCLIP and self.y < len(globals.LVL) - 1) or not isWall(self.x, self.y +1):
                    self.moving = True
                    self.dirr = "d"
                    self.moving = True
                    self.energie -= 1
                self.img = sprites.sl["pl_d_s"]
            elif keys[K_q] or keys[K_LEFT]:
                if (globals.NOCLIP and self.x > 0) or not isWall(self.x -1, self.y):
                    self.moving = True
                    self.dirr = "l"
                    self.moving = True
                    self.energie -= 1
                self.img = sprites.sl["pl_l_s"]
            elif keys[K_d] or keys[K_RIGHT]:
                if (globals.NOCLIP and self.x < len(globals.LVL[self.y]) - 1) or not isWall(self.x + 1, self.y):
                    self.moving = True
                    self.dirr = "r"
                    self.moving = True
                    self.energie -= 1
                self.img = sprites.sl["pl_r_s"]
        else:
            self.moveAnim(self.dirr)

        if self.x != oldX or self.y != oldY:
            if type(globals.MAP[self.y][self.x]) is tile.Fruits:
                self.energie += 10
                globals.MAP[self.y][self.x] = tile.Tile(self.x, self.y)
            if type(globals.MAP[self.y][self.x]) is tile.Bed:
                print(globals.Jour)
                if not globals.Jour:
                    if globals.NUM_LVL < globals.MAX_LEVEL:
                        globals.Jour = True
                        globals.LVL_CHANGED = True
                        globals.NUM_LVL += 1
                    else:
                        gameover.end_screen()
                else:
                    globals.Jour = False
                    globals.LVL_CHANGED = True

                self.energie = MAX_ENERGY

        
        if globals.Jour and self.energie <= 0:
            self.death()
    

    def death(self):
        globals.NB_MORTS += 1
        if not globals.Jour:
            globals.Jour = True
        globals.LVL_CHANGED = True
        self.energie = MAX_ENERGY
