import os, sys
import pygame
from states.firstmenu import FirstMenu
from app import App

pygame.init()
screen = pygame.display.set_mode((960, 540))

states = {
    "FIRSTMENU": FirstMenu(),
}

app = App(screen, states, "FIRSTMENU")
app.run()

pygame.quit()
sys.exit()
