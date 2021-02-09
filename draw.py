import pygame
import globals
import level
import player
import sprites
import colors
import energy_bar

def drawAll():
    globals.WIN.fill(colors.GREY)
    level.show(globals.MAP)
    globals.PLAYER.draw()
    if not globals.Jour:
        rect = pygame.Rect(0, 0, globals.WIDTH, globals.HEIGHT)
        globals.WIN.blit(sprites.sl["blind"], rect)
    energy_bar.draw_bar(globals.PLAYER.energie)
    pygame.display.flip()