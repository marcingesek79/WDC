import pygame
from .helpers import draw_text

class EmptyBox:
    def __init__(self, colors, font, text, rect):
        self.colors = colors #Kolor
        self.text = text
        self.font = font

        self.rect = pygame.Rect(rect)

    def draw(self, surface):
        #Rysuje guzik z wyśrodkowanym tekstem
        pygame.draw.rect(surface, self.colors[0], self.rect)
        draw_text(surface, self.text, self.font, self.colors[1], self.rect)
