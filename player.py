import pygame
from pygame.locals import*
import colors
import globals
from globals import *
import objects

class Player:
    x = 0 #en unité jeu
    y = 0
    img = objects.sprites["pl_u"]
    rect = None
    speed = 5
    energie = MAX_ENERGY
    def load(self, x, y):
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.move_ip(calcX(x) - globals.marginLeft + ((1 - globals.PLAYER_SCALE)/2 * globals.OBJECT_WIDTH), calcY(y) - globals.marginTop + ((1 - globals.PLAYER_SCALE)/2 * globals.OBJECT_HEIGHT))

        self.x = x
        self.y = y

        globals.WIN.blit(self.img, self.rect)
    
    def draw(self):
        if self.energie <= 0:
            #self.img = pygame.image.load('assets/player_dead.png')
            self.img = pygame.transform.scale(self.img, (globals.PLAYER_WIDTH, globals.PLAYER_HEIGHT))
            self.img.convert()
        
        globals.WIN.blit(self.img, self.rect)
    
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[K_w] or keys[K_UP]:
            if not isWall(self.x, self.y -1):
                self.y -= 1
                self.energie -=1
                self.img = objects.sprites["pl_u"]
                globals.changeView(self.x, self.y)
        if keys[K_s] or keys[K_DOWN]:
            if not isWall(self.x, self.y +1):
                self.y += 1
                self.energie -=1
                self.img = objects.sprites["pl_d"]
                globals.changeView(self.x, self.y)
        if keys[K_a] or keys[K_LEFT]:
            if not isWall(self.x -1, self.y):
                self.x -= 1
                self.energie -=1
                self.img = objects.sprites["pl_l"]
                globals.changeView(self.x, self.y)
        if keys[K_d] or keys[K_RIGHT]:
            if not isWall(self.x + 1, self.y):
                self.x += 1     
                self.energie -=1
                self.img = objects.sprites["pl_r"]
                globals.changeView(self.x, self.y)