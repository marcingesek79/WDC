import pygame

class Button:
    def __init__(self, colors, colors2, font, text, rect, click):
        self.colors = colors #Kolor
        self.colors2 = colors2 #Alt Kolor kiedy hover == True
        self.text = text
        self.font = font

        self.rect = pygame.Rect(rect)

        self.hover = False
        self.click = click #Funkcja callback wywoływana jak klikniesz

    def draw(self, surface):
        #Rysuje guzik z wyśrodkowanym tekstem
        palette = self.colors if not self.hover else self.colors2

        pygame.draw.rect(surface, palette[0], self.rect)
        textobj = self.font.render(self.text, 1, palette[1])
        textrect = textobj.get_rect(center=self.rect.center);
        surface.blit(textobj, textrect)
