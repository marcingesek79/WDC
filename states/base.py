import pygame

class BaseState(object):
    def __init__(self):
        # Jeśli done == True to ten stan sie zamyka i otwiera sie next_state
        # quit == True zamyka apke
        # persist to słownik który jest przekazywany miedzy stanami więc sie dane zapisują

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

    #Generator funkcji które zmieniają stan na inny
    def switch_to(self, state):
        def switch(menu):
            menu.next_state = state
            menu.done = True
        return switch
