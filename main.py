import pygame
import colors
import globals
from pygame.locals import*
from globals import *
import player
from player import *
import level
import energy_bar
import objects
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
objects.loadSprites()
pygame.display.set_caption("Game Jam 2021");

player = Player()
    
pygame.font.init()


def main():
    run = True
    globals.changeView(16, 18)
    globals.LVL = level.load(2)
    # level.cli(globals.lvl)
    player.load(16, 18)
    while run:
        objects.drawBG()
        level.show(globals.LVL)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == KEYDOWN:
                player.move(event.key)
                globals.changeView(player.x, player.y)
        player.draw()
        energy_bar.draw_bar(player.energie)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
