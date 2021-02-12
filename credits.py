import pygame
import globals
import fonts
import colors

#globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
def credits():
  globals.WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT));
  alive= True
  while alive:
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        alive = False
    globals.WIN.fill(colors.GREY)
    title = fonts.pixel_font_title.render("Credits", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 50))

    title = fonts.pixel_font_30.render("Programmation :", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 150))
    
    title = fonts.pixel_font_24.render("- Clément G.", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 200))

    title = fonts.pixel_font_24.render("- Thomas D.", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 250))

    title = fonts.pixel_font_24.render("- Nassim D.", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 300))

    title = fonts.pixel_font_30.render("Graphisme :", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 400))

    title = fonts.pixel_font_24.render("- Nassim D.", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 450))

    title = fonts.pixel_font_24.render("- Thomas V.", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 500))

    title = fonts.pixel_font_30.render("Audio :", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 600))

    title = fonts.pixel_font_24.render("- Clément G.", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 650))

    title = fonts.pixel_font_24.render("- Thomas V.", True, colors.BLACK)
    globals.WIN.blit(title, (globals.WIDTH / 2 - 150, 700))


    
    pygame.display.flip()
 