import pygame
from pygame.locals import*
import colors
import globals
from globals import *
from enum import Enum
import sprites
import time
import draw
import tile

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
        self.iSprite = 0
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
        if dirr == "u":
            self.rect.move_ip(0, - OBJECT_HEIGHT / 16)
        elif dirr == "l":
            self.rect.move_ip(- OBJECT_WIDTH / 16, 0)
        elif dirr == "r":
            self.rect.move_ip(OBJECT_WIDTH / 16, 0)
        elif dirr == "d":
            self.rect.move_ip(0, OBJECT_HEIGHT / 16)

        self.img = sprites.sl["pl_" + dirr + "_m_" + str(self.iSprite)]
        self.iSprite = (self.iSprite + 1) % 16

    def move(self):
        keys=pygame.key.get_pressed()

        oldX = self.x
        oldY = self.y

        if keys[K_z] or keys[K_UP]:
            if globals.NOCLIP or not isWall(self.x, self.y -1):
                draw.anim("u", self)
                self.energie -= 1
                self.y = oldY - 1
                globals.changeView(self.x, self.y)
            self.resetPos()
            oldX = self.x
            oldY = self.y
            self.img = sprites.sl["pl_u_s"]
        if keys[K_s] or keys[K_DOWN]:
            if globals.NOCLIP or not isWall(self.x, self.y +1):
                draw.anim("d", self)
                self.energie -= 1
                self.y = oldY + 1
                globals.changeView(self.x, self.y)
            self.resetPos()
            oldX = self.x
            oldY = self.y
            self.img = sprites.sl["pl_d_s"]
        if keys[K_q] or keys[K_LEFT]:
            if globals.NOCLIP or not isWall(self.x -1, self.y):
                draw.anim("l", self)
                self.energie -= 1
                self.x = oldX - 1
                globals.changeView(self.x, self.y)
            self.resetPos()
            oldX = self.x
            oldY = self.y
            self.img = sprites.sl["pl_l_s"]
        if keys[K_d] or keys[K_RIGHT]:
            if globals.NOCLIP or not isWall(self.x + 1, self.y):
                draw.anim("r", self)
                self.energie -= 1
                self.x = oldX + 1
                globals.changeView(self.x, self.y)
            self.resetPos()
            oldX = self.x
            oldY = self.y
            self.img = sprites.sl["pl_r_s"]

        if self.x != oldX or self.y != oldY:
            if type(self.getCurrentTile()) is tile.Bed:
                if globals.Jour :
                    globals.Jour = False
                    print("day end")
                else :
                    globals.Jour = True
                    print("night end")
