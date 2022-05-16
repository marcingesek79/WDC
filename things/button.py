import pygame
from .emptybox import EmptyBox
from .helpers import draw_text

class Button(EmptyBox):
    def __init__(self, colors, colors2, font, text, rect, click):
        super(Button, self).__init__(colors, font, text, rect)
        self.colors2 = colors2 #Alt Kolor kiedy hover == True

        self.hover = False
        self.click = click #Funkcja callback wywoływana jak klikniesz

    def draw(self, surface):
        #Rysuje guzik z wyśrodkowanym tekstem
        palette = self.colors if not self.hover else self.colors2

        pygame.draw.rect(surface, palette[0], self.rect)
        draw_text(surface, self.text, self.font, palette[1], self.rect)
