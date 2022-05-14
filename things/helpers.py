#Might be useful later
import pygame

def draw_text(surface, text, font, color, rect):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect(center=rect.center);
    surface.blit(textobj, textrect)
