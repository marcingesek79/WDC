import os, sys
import pygame
from states.firstmenu import FirstMenu
from states.signmenu import SignMenu
from states.verifymenu import VerifyMenu
from states.generationmenu import GenerationMenu
from app import App

# Nie patrz na to ani na app.py wgl bo tam nic ważnego nie ma
# Generalnie każda funkcja w states to osobne menu i tam jest wszystko ważne

pygame.init()
screen = pygame.display.set_mode((960, 540))

states = {
    "FIRSTMENU": FirstMenu(),
    "SIGNMENU": SignMenu(),
    "VERIFYMENU": VerifyMenu(),
    "GENERATIONMENU": GenerationMenu()
}

app = App(screen, states, "FIRSTMENU")
app.run()

pygame.quit()
sys.exit()
