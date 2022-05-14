import pygame
from .base import BaseState
from things.button import Button

WHITE = "#ffffff"
BLACK = "#000000"
GREY = "#c0c0c0"
L_GREEN = "#b4ffb4"
M_GREEN = "#82cd82"
D_GREEN = "#509b50"
YELLOW = "#ffee75"

base_color = (D_GREEN, BLACK)
base_hover = (M_GREEN, GREY)

class FirstMenu(BaseState):
    def __init__(self):
        super(FirstMenu, self).__init__()
        self.font = pygame.font.SysFont("urwgothic", 24)

        b1 = Button(base_color, base_hover, self.font, "Podpisz Dokument", 120, 100, 300, 200)
        b2 = Button(base_color, base_hover, self.font, "Zweryfikuj Dokument", 540,100,300,200)
        self.buttons = [b1,b2]

        self.next_state = None


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

    def update(self, dt):
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.hover = True
            else:
                button.hover = False

    def draw(self, surface):
        surface.fill(L_GREEN)
        for button in self.buttons:
            button.draw(surface)
