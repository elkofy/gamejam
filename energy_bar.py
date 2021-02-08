import pygame
import colors
import globals
#pixel_font = pygame.font.Font("assets/pixel_font.ttf", 26)


def draw_bar(energie):
    pixel_font = pygame.font.Font("assets/pixel_font.ttf", 24)
    rec = pygame.Rect(825, 25, 100*(energie/globals.MAX_ENERGY) , 20)
    pygame.draw.rect(globals.WIN, colors.BLUE, rec, 0)
    img = pixel_font.render(str(energie) + "/" + str(globals.MAX_ENERGY), True, colors.WHITE)
    globals.WIN.blit(img, (930, 24))