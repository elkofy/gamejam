import pygame
from pygame.locals import*
import colors
import globals
from globals import *

class Player:
    x = 0 #en unité jeu
    y = 0
    img = pygame.image.load('assets/player.png')
    rect = None
    speed = 5
    energie = MAX_ENERGY

    def load(self, x, y):
        self.img = pygame.transform.scale(self.img, (globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT))
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.move_ip(calcX(x) - globals.marginLeft, calcY(y) - globals.marginTop)

        self.x = x
        self.y = y

        globals.WIN.blit(self.img, self.rect)
    
    def draw(self):
        if self.energie <= 0:
            self.img = pygame.image.load('assets/player_dead.png')
            self.img = pygame.transform.scale(self.img, (globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT))
            self.img.convert()
        
        globals.WIN.blit(self.img, self.rect)
    
    def move(self, keypressed):
        if keypressed == K_w or keypressed == K_UP:
            if not isWall(self.x, self.y -1):
                self.y -= 1
                self.energie -=1
        elif keypressed == K_s or keypressed == K_DOWN:
            if not isWall(self.x, self.y +1):
                self.y += 1
                self.energie -=1
        elif keypressed == K_a or keypressed == K_LEFT:
            if not isWall(self.x -1, self.y):
                self.x -= 1
                self.energie -=1
        elif keypressed == K_d or keypressed == K_RIGHT:
            if not isWall(self.x + 1, self.y):
                self.x += 1     
                self.energie -=1