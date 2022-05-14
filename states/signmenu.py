import pygame
from .base import BaseState
from things.button import Button
import things.colors as Colors

class SignMenu(BaseState):
    def __init__(self):
        super(SignMenu, self).__init__()
        self.font = pygame.font.SysFont("urwgothic", 24)

        bx = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "X", (850,50,80,40), self.switch_to("FIRSTMENU"))
        self.buttons = [bx]

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
