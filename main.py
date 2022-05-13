import pygame
import os, sys

pygame.font.init()

mainClock = pygame.time.Clock()

WIDTH, HEIGHT = 960, 540
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stary kobasa")

WHITE = "#ffffff"
BLACK = "#000000"
GREY = "#c0c0c0"
L_GREEN = "#b4ffb4"
M_GREEN = "#82cd82"
D_GREEN = "#509b50"
YELLOW = "#ffee75"

font = pygame.font.SysFont("urwgothic", 36)
font_s = pygame.font.SysFont("urwgothic", 14)
font_es = pygame.font.SysFont("urwgothic", 10)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def menuDraw(selected):
    WINDOW.fill(L_GREEN)
    draw_text('New Game', font, GREY if selected == 0 else BLACK, WINDOW, 20, 20)
    draw_text('Load Game', font, GREY if selected == 1 else BLACK, WINDOW, 20, 80)
    draw_text('Quit', font, GREY if selected == 2 else BLACK, WINDOW, 20, 140)
    pygame.display.update()

def main():
    gameloop = True
    selected = 0
    while gameloop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_DOWN and selected < 2:
                    selected += 1
                if event.key == pygame.K_UP and selected > 0:
                    selected -= 1
                if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                    gameloop = False
                    [menuNew, menuLoad, gameQuit][selected]()

        menuDraw(selected)
        mainClock.tick(60)

    pygame.quit()

def menuNewDraw(text, selected, errtext):
    WINDOW.fill(D_GREEN)
    draw_text('Map width: '+text[0], font, GREY if selected == 0 else BLACK, WINDOW, 20, 20)
    draw_text('Map height: '+text[1], font, GREY if selected == 1 else BLACK, WINDOW, 20, 80)
    draw_text(errtext, font, BLACK, WINDOW, 20, 140)
    pygame.display.update()

def menuNew(errtext = ""):
    gameloop = True
    selected = 0
    text = ["",""]

    while gameloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key in (pygame.K_SPACE, pygame.K_RETURN) and text[selected]:
                    if selected != 1:
                        selected += 1
                    else:
                        gameloop = False
                elif event.key == pygame.K_BACKSPACE:
                    text[selected] = text[selected][:-1]
                elif event.unicode.isdigit():
                    text[selected] += event.unicode


        menuNewDraw(text, selected, errtext)
        mainClock.tick(60)

menuNew()
