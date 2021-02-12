import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import pygame_menu
from main import main
import credits
import fonts

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
def menu():
    fonts.font_init()
    menu = pygame_menu.Menu( globals.HEIGHT,globals.WIDTH, 'Organic Future',
                       theme=pygame_menu.themes.THEME_DEFAULT)
    globals.NAME = menu.add_text_input('Nom :', default='lolo')
    menu.add_button('Jouer', main)
    menu.add_button('Credits', credits.credits)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(globals.WIN)


if __name__ == "__main__":
    menu()