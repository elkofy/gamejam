import pygame
import colors
import globals
#pixel_font = pygame.font.Font("assets/pixel_font.ttf", 26)


def draw_bar(energie):
    if globals.Jour:
        if energie > 0:
            length = 100*(energie/globals.MAX_ENERGY)
            pixel_font = pygame.font.Font("assets/pixel_font.ttf", 24)
            rec = pygame.Rect(915 - length, 25, length , 20)
            pygame.draw.rect(globals.WIN, colors.BLUE, rec, 0)
            rec = pygame.Rect(915 - length, 25, length , 20)
            pygame.draw.rect(globals.WIN, colors.WHITE, rec, 3)
            img = pixel_font.render(str(energie), True, colors.BLACK)
            globals.WIN.blit(img, (930, 24))
    else:
        length = 100
        pixel_font = pygame.font.Font("assets/pixel_font.ttf", 24)
        rec = pygame.Rect(915 - length, 25, length , 20)
        pygame.draw.rect(globals.WIN, colors.RED, rec, 0)
        rec = pygame.Rect(915 - length, 25, length , 20)
        pygame.draw.rect(globals.WIN, colors.WHITE, rec, 3)
        img = pixel_font.render("99999", True, colors.WHITE)
        globals.WIN.blit(img, (930, 24))
