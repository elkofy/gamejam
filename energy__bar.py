import pygame
import colors
import globals

def draw_bar(energie):
    rec = pygame.Rect(900, 25, 100*(energie/globals.MAX_ENERGY) , 20)
    pygame.draw.rect(globals.WIN, colors.BLUE, rec, 0)