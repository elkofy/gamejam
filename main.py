import pygame
import colors

WIN = pygame.display.set_mode((1024, 728));
pygame.display.set_caption("Game Jam 2021");

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        WIN.fill(colors.GREY)
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__" :
    main()