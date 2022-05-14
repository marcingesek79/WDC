import pygame
from .base import BaseState
from things.button import Button
import things.colors as Colors
from things.helpers import draw_text

def do_nothing(menu):
    pass

class VerifyMenu(BaseState):
    def __init__(self):
        super(VerifyMenu, self).__init__()
        self.font = pygame.font.SysFont("urwgothic", 24)

        bx = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "X2", (870,40,40,40), self.switch_to("FIRSTMENU"))
        b1 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Wybierz plik", (300,250,180,40), do_nothing)
        b2 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Wybierz klucz", (300,490,180,40), do_nothing)

        b3 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Zweryfikuj", (600,490,240,40), do_nothing)
        self.buttons = [bx,b1,b2,b3]

        self.chosen_file = None
        self.chosen_key = None

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

        filebox = pygame.Rect(60,60,420,180)
        keybox = pygame.Rect(60,300,420,180)

        pygame.draw.rect(surface, Colors.D_GREEN, filebox)
        pygame.draw.rect(surface, Colors.D_GREEN, keybox)

        draw_text(surface, self.chosen_file if self.chosen_file else "Nie wybrano pliku", self.font, Colors.BLACK, filebox)
        draw_text(surface, self.chosen_key if self.chosen_key else "Nie wybrano klucza", self.font, Colors.BLACK, keybox)

        draw_text(surface, "Plik:", self.font, Colors.BLACK, pygame.Rect(60,60,100,50))
        draw_text(surface, "Klucz:", self.font, Colors.BLACK, pygame.Rect(60,300,100,50))
