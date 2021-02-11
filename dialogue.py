import pygame
import globals
pygame.init()
font = pygame.font.Font(None, 25)


def text_generator(text):
    tmp = " "
    for letter in text:
        tmp += letter
        yield tmp

def wipetext(text):
     tmp = ''
     for letter in text:
        tmp = ' '
        if letter != ' ':
            yield tmp      

class Dialogue(object):
   
    def __init__(self, font, text, pos, autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self._gen = text_generator(self.text)
        self.pos = pos
        self.autoreset = autoreset
        self.update()

    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def len(self):
        for letters in self.text:
            self.update()

    def erase(self):
        self._gen = wipetext(self.text)
        self.done = False

    
    def update(self):
        if not self.done:
            try: self.rendered = self.font.render(next(self._gen), True, (0, 0, 0))
            except StopIteration: 
                self.done = True
                if self.autoreset: self.reset()

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)


