import pygame
from pygame.locals import*
import globals


class Player:
    x = 0 #en unité jeu
    y = 0
    img = pygame.image.load('assets/player.png')
    rect = None
    speed = 5

    def load(self, x, y):
        self.img = pygame.transform.scale(self.img, (globals.OBJECT_WIDTH, globals.OBJECT_HEIGHT))
        self.img.convert()
        self.rect = pygame.Rect(globals.calcX(x), globals.calcY(y), globals.GAME_WIDTH, globals.GAME_HEIGHT)

        self.x = x
        self.y = y

        globals.WIN.blit(self.img, self.rect)
    
    def move(self, keypressed):
        if keypressed == K_w or keypressed == K_UP:
            self.rect.move(self.x, self.y + globals.OBJECT_HEIGHT)
        elif keypressed == K_s or keypressed == K_DOWN:
            print("move down")
        elif keypressed == K_a or keypressed == K_LEFT:
            print("left")
        elif keypressed == K_d or keypressed == K_RIGHT:
            print("move right")    