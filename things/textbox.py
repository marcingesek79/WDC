import pygame
from .button import Button
from .helpers import draw_text

class Textbox(Button):
    def __init__(self, colors, colors2, font, text, rect, max_len):
        super(Textbox, self).__init__(colors, colors2, font, text, rect, self.select)
        self.selected = False
        self.max_len = max_len

    def draw(self, surface):
        #Rysuje guzik z wyśrodkowanym tekstem
        palette = self.colors if not self.selected else self.colors2

        pygame.draw.rect(surface, palette[0], self.rect)
        draw_text(surface, self.text, self.font, palette[1], self.rect)

    def select(self, menu):
        menu.selected_textbox = self
        self.selected = True
