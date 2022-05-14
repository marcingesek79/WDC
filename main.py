import os, sys
import pygame
from states.firstmenu import FirstMenu
from states.signmenu import SignMenu
from states.verifymenu import VerifyMenu
from app import App

pygame.init()
screen = pygame.display.set_mode((960, 540))

states = {
    "FIRSTMENU": FirstMenu(),
    "SIGNMENU": SignMenu(),
    "VERIFYMENU": VerifyMenu()
}

app = App(screen, states, "FIRSTMENU")
app.run()

pygame.quit()
sys.exit()
