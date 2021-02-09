import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import pygame_menu
from main import main

pygame.init()
def menu():
    menu = pygame_menu.Menu( globals.HEIGHT,globals.WIDTH, 'Organic Future',
                       theme=pygame_menu.themes.THEME_DEFAULT)
    menu.add_text_input('Nom :', default='KIDZ')
    menu.add_button('Jouer', main)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(globals.WIN)

if __name__ == "__main__":
    menu()