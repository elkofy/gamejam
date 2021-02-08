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
    #level.create(420)
    globals.LVL = level.load(420)
    #level.cli(globals.lvl)
    player.load(4, 6)
    while run:
        globals.WIN.fill(colors.GREY)
        level.show(globals.LVL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                player.move(event.key)
        player.draw()
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__" :
    main()