import pygame
import globals
import fonts
import colors
pygame.init()
font = pygame.font.Font(None, 25)

DUREE_REP = 4000

class Replique():

    def __init__(self):
        self.lignes = []

    def addLigne(self, text):
        self.lignes.append(text)

class Dialogue():
   
    def __init__(self):
        self.done = False
        self.repliques = []
        self.i = 0
        self.animTime = 0

    def addReplique(self):
        self.repliques.append(Replique())

    def addLigne(self, text):
        self.repliques[len(self.repliques) - 1].addLigne(text)

    def draw(self):
        self.animTime += globals.LT
        if self.animTime >= DUREE_REP:
            self.animTime = 0
            self.i += 1
            if self.i > len(self.repliques) - 1:
                self.done = True
        
        pygame.draw.rect(globals.WIN, colors.BLACK, pygame.Rect(0, 0.75 * globals.HEIGHT, globals.WIDTH, 0.25 * globals.HEIGHT))

        for j in range(len(self.repliques[self.i].lignes)):
            img = fonts.pixel_font_30.render(self.repliques[self.i].lignes[j], True, colors.WHITE)
            globals.WIN.blit(img, ((globals.WIDTH - (img.get_size()[0]))/2,  (0.8 * globals.HEIGHT) + j * (0.05 * globals.HEIGHT)))

            0.8 * globals.HEIGHT