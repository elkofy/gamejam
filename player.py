import pygame
from pygame.locals import*
import colors
import globals
from globals import *
from enum import Enum

class Directions(Enum):
    Up = 0
    Down = 1
    Left = 2
    Right = 3

SCALE = (globals.OBJECT_WIDTH - 2 * int((1 - globals.PLAYER_SCALE)/2 * OBJECT_WIDTH), globals.OBJECT_WIDTH - 2 * int((1 - globals.PLAYER_SCALE)/2 * OBJECT_WIDTH))

player_down = pygame.transform.scale(pygame.image.load('assets/player_down.png'), SCALE)
player_up = pygame.transform.scale(pygame.image.load('assets/player_up.png'), SCALE)
player_left = pygame.transform.scale(pygame.image.load('assets/player_left.png'), SCALE)
player_right = pygame.transform.scale(pygame.image.load('assets/player_right.png'), SCALE)

class Player:
    x = 0 #en unité jeu
    y = 0
    img = player_up
    rect = None
    speed = 5
    energie = MAX_ENERGY
    walking_Cpt = 0
    def load(self, x, y):
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.move_ip(calcX(x) - globals.marginLeft + ((1 - globals.PLAYER_SCALE)/2 * globals.OBJECT_WIDTH), calcY(y) - globals.marginTop + ((1 - globals.PLAYER_SCALE)/2 * globals.OBJECT_HEIGHT))

        self.x = x
        self.y = y

        globals.WIN.blit(self.img, self.rect)
    
    def draw(self):
        if self.walking_Cpt >= 0:
            self.walking_Cpt -= 1
        if self.energie <= 0:
            #self.img = pygame.image.load('assets/player_dead.png')
            self.img = pygame.transform.scale(self.img, SCALE)
            self.img.convert()
        
        globals.WIN.blit(self.img, self.rect)
    
    def move(self):
        keys=pygame.key.get_pressed()
        if keys[K_w] or keys[K_UP]:
            if not isWall(self.x, self.y -1):
                self.y -= 1
                self.energie -=1
                self.img = player_up
                globals.changeView(self.x, self.y)
        if keys[K_s] or keys[K_DOWN]:
            if not isWall(self.x, self.y +1):
                self.y += 1
                self.energie -=1
                self.img = player_down
                globals.changeView(self.x, self.y)
        if keys[K_a] or keys[K_LEFT]:
            if not isWall(self.x -1, self.y):
                self.x -= 1
                self.energie -=1
                self.img = player_left
                globals.changeView(self.x, self.y)
        if keys[K_d] or keys[K_RIGHT]:
            if not isWall(self.x + 1, self.y):
                self.x += 1     
                self.energie -=1
                self.img = player_right
                globals.changeView(self.x, self.y)