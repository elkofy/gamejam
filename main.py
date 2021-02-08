import pygame
import colors
import globals
from pygame.locals import*
from globals import *
import player
from player import *
import level

globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
pygame.display.set_caption("Game Jam 2021");

player = Player()
    

def main():
    run = True
    globals.WIN.fill(colors.GREY)
    lvl = level.randomlvl()
    level.cli(lvl)
    level.show(lvl)
    player.load(4, 6)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                print("here")
                if event.type == K_w:
                    print("z")
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__" :
    main()