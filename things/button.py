import pygame

class Button:
    def __init__(self, colors, colors2, font, text, left, top, width, height):
        self.colors = colors
        self.colors2 = colors2
        self.text = text
        self.font = font

        self.rect = pygame.Rect(left, top, width, height)
        self.hover = False

    def draw(self, surface):
        palette = self.colors if not self.hover else self.colors2

        pygame.draw.rect(surface, palette[0], self.rect)
        textobj = self.font.render(self.text, 1, palette[1])
        textrect = textobj.get_rect(center=self.rect.center);
        surface.blit(textobj, textrect)
