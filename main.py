import pygame
import colors
import showLevel

WIN = pygame.display.set_mode((1024, 728));
pygame.display.set_caption("Game Jam 2021");

def main():
    run = True
    WIN.fill(colors.GREY)
    showLevel.show(1)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__" :
    main()