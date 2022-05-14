import pygame

WHITE = "#ffffff"
BLACK = "#000000"
GREY = "#c0c0c0"
L_GREEN = "#b4ffb4"
M_GREEN = "#82cd82"
D_GREEN = "#509b50"
YELLOW = "#ffee75"

base_color = (D_GREEN, BLACK)
base_hover = (M_GREEN, GREY)

class BaseState(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_state = None
        self.screen_rect = pygame.display.get_surface().get_rect()
        self.persist = {}
        self.font = pygame.font.Font(None, 24)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass

    def switch_to(self, state):
        def switch(menu):
            menu.next_state = state
            menu.done = True
        return switch
