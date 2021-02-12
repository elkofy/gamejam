import pygame
import globals
globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
import pygame_menu
from main import main
import help
import credits
import fonts

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()


menuTheme = pygame_menu.themes.Theme(background_color=(0, 0, 0, 255),
                title_shadow=True,
                title_background_color=(0, 0, 0),
                title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_SIMPLE,
                widget_font=pygame_menu.font.FONT_BEBAS)

def menu():
    fonts.font_init()
    menu = pygame_menu.Menu(globals.HEIGHT,globals.WIDTH, 'GameJam 2021',
                       theme=menuTheme)

    menu.add_image("assets/title.png")
    menu.add_vertical_margin(100)
    globals.NAME = menu.add_text_input('Nom : ', default='Player')
    menu.add_vertical_margin(100)
    menu.add_button('Jouer', main)
    menu.add_button('Aide', help.help)
    menu.add_button('Credits', credits.credits)
    menu.add_button('Quitter', pygame_menu.events.EXIT)
    menu.mainloop(globals.WIN)

if __name__ == "__main__":
    menu()