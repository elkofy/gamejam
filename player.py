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

    def load(self, x, y):
        self.img = pygame.transform.scale(self.img, (globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT))
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.move_ip(calcX(x), calcY(y))

        self.x = x
        self.y = y

        globals.WIN.blit(self.img, self.rect)
    
    def draw(self):
        globals.WIN.blit(self.img, self.rect)
    
    def move(self, keypressed):
        if keypressed == K_w or keypressed == K_UP:
            self.rect.move_ip(0, 0 - globals.OBJECT_HEIGHT)
            self.y -= 1
        elif keypressed == K_s or keypressed == K_DOWN:
            self.rect.move_ip(0, 0 + globals.OBJECT_HEIGHT)
            self.y += 1
        elif keypressed == K_a or keypressed == K_LEFT:
            self.rect.move_ip(0 - globals.OBJECT_WIDTH, 0)
            self.x -= 1
        elif keypressed == K_d or keypressed == K_RIGHT:
            self.rect.move_ip(0 + globals.OBJECT_WIDTH, 0)
            self.x += 1