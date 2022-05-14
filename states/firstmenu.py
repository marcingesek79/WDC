import pygame
from .base import BaseState
from things.button import Button
import things.colors as Colors

class FirstMenu(BaseState):
    def __init__(self):
        super(FirstMenu, self).__init__()
        self.font = pygame.font.SysFont("urwgothic", 24)

        #Dwa guziki, jak klikniesz to odpala sie switch(state) [zwrócone przez switch_to]
        b1 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Podpisz Dokument", (120,100,300,200), self.switch_to("SIGNMENU"))
        b2 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Zweryfikuj Dokument", (540,100,300,200), self.switch_to("VERIFYMENU"))
        self.buttons = [b1,b2]

        self.next_state = None

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Jeżeli guzik naciśniety to wywołuje jego funkcje
            for button in self.buttons:
                if button.hover:
                    button.click(self)

    def update(self, dt):
        #Detekcja myszki nad guzikiem
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.hover = True
            else:
                button.hover = False

    def draw(self, surface):
        surface.fill(Colors.L_GREEN)
        for button in self.buttons:
            button.draw(surface)
