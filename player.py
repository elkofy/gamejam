import pygame
import globals

class Player:
    x = 0
    y = 0
    img = pygame.image.load('assets/player.png')
    rect = None
    speed = 5

    def load(self, x, y):
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.img.convert()
        self.rect = self.img.get_rect()
        self.rect.center = x, y
        self.x = x
        self.y = y
        globals.WIN.blit(self.img, self.rect);
    