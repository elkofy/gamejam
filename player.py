import pygame
import globals

class Player:
    x = 0
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
    
    def move(self, x, y):
        None
    