import pygame
import player
from player import *
import objects
import globals
class Mob(Player):
    img = objects.sprites["m_tomato"]
    speed = 5

    def draw(self):
        print(self.rect.y)
        print(globals.calcY(self.x))
        if self.rect.y != globals.calcY(self.y):
            self.rect.move_ip(0, self.speed)
            
        else:
            None
        globals.WIN.blit(self.img, self.rect)

    def move(self):
        if not globals.isWall(self.x, self.y +1):
            self.y += 1
        else:
            print("wall")
