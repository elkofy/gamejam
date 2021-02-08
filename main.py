import pygame
import colors
import globals
from pygame.locals import*
from globals import *
import player
from player import *
import level
import energy_bar
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
pygame.display.set_caption("Game Jam 2021");

player = Player()
    
pygame.font.init()
def main():
    run = True
    # level.create(420)
    globals.LVL = level.load(2)
    # level.cli(globals.lvl)
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
        energy_bar.draw_bar(player.energie)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
