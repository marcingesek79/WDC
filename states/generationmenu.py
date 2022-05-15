import pygame
import tkinter
import tkinter.filedialog

from .base import BaseState
from things.button import Button
import things.colors as Colors
from things.helpers import draw_text
import key_generation as kg

def do_nothing(menu):
    pass

class GenerationMenu(BaseState):
    def __init__(self):
        super(GenerationMenu, self).__init__()
        self.font = pygame.font.SysFont("urwgothic", 24)

        space = 30

        bx = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "X", (870,40,40,40), self.switch_to("SIGNMENU"))
        b1 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, ".der", (480,250,180,40), do_nothing)
        b2 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, ".key", (270,250,180,40), do_nothing)
        b3 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, ".pem", (60,250,180,40), do_nothing)
        b4 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Usuń klucze", (60, 300, 600, 40), do_nothing)
        
        self.buttons = [bx,b1,b2,b3,b4]
        self.next_state = None

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.hover:
                    if button.text == ".der":
                        kg.delete_keys()
                        kg.generate_key_pair(".der")
                    elif button.text == ".key":
                        kg.delete_keys()
                        kg.generate_key_pair(".key")
                    elif button.text == ".pem":
                        kg.delete_keys()
                        kg.generate_key_pair(".pem")
                    elif button.text == "Usuń klucze":
                        kg.delete_keys()
                    else:
                        button.click(self)

    def update(self, dt):
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.hover = True
            else:
                button.hover = False

    def draw(self, surface):
        surface.fill(Colors.L_GREEN)
        for button in self.buttons:
            button.draw(surface)

        text_box = pygame.Rect(60,60,600,180)
        pygame.draw.rect(surface, Colors.D_GREEN, text_box)

        draw_text(surface, "Wybierz format kluczy", self.font, Colors.BLACK, text_box)
