import pygame as pg
import os, sys

pg.font.init()

mainClock = pg.time.Clock()

WIDTH, HEIGHT = 960, 540
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Stary kobasa")

WHITE = "#ffffff"
BLACK = "#000000"
GREY = "#c0c0c0"
L_GREEN = "#b4ffb4"
M_GREEN = "#82cd82"
D_GREEN = "#509b50"
YELLOW = "#ffee75"

font = pg.font.SysFont("urwgothic", 36)
font_m = pg.font.SysFont("urwgothic", 24)
font_s = pg.font.SysFont("urwgothic", 14)
font_es = pg.font.SysFont("urwgothic", 10)

base_color = (D_GREEN, BLACK)
base_hover = (M_GREEN, GREY)

class Button:
    def __init__(self, colors, colors2, text, left, top, width, height):
        self.colors = colors
        self.text = text
        self.colors2 = colors2
        self.loc = pg.Rect(left, top, width, height)
        self.hover = False

    def draw(self, surface):
        palette = self.colors if not self.hover else self.colors2

        pg.draw.rect(WINDOW, palette[0], self.loc)
        draw_text(self.text, font_m, palette[1], WINDOW, self.loc.left + self.loc.width * .15, self.loc.top + self.loc.height * .4)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def FirstMenu():
    loop = True;
    b1 = Button(base_color, base_hover, "Podpisz Dokument", 120, 100, 300, 200)
    b2 = Button(base_color, base_hover, "Zweryfikuj Dokument", 540,100,300,200)

    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if b1.hover:
                    SignMenu()
                if b2.hover:
                    VerifyMenu()

            for button in [b1,b2]:
                if button.loc.collidepoint(pg.mouse.get_pos()):
                    button.hover = True
                else:
                    button.hover = False

            WINDOW.fill(L_GREEN)

            b1.draw()
            b2.draw()

            pg.display.update()

def SignMenu():
    print("xddd")
    loop = True;
    b1 = Button(base_color, base_hover, "O KURWA TWOJA STARA", 540,100,300,700)

    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pass

        for button in [b1]:
            if button.loc.collidepoint(pg.mouse.get_pos()):
                button.hover = True
            else:
                button.hover = False

        WINDOW.fill(L_GREEN)

        b1.draw()

        pg.display.update()

def VerifyMenu():
    loop = True;
    b1 = Button(base_color, base_hover, "O KURWA TWÓJ STARY", 120, 100, 700, 200)

    while loop:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                pass

        for button in [b1]:
            if button.loc.collidepoint(pg.mouse.get_pos()):
                button.hover = True
            else:
                button.hover = False

        WINDOW.fill(L_GREEN)

        b1.draw()

        pg.display.update()

# def main():
#     gameloop = True
#     selected = 0
#     while gameloop:
#
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 sys.exit()
#             if event.type == pg.KEYDOWN:
#                 if event.key == pg.K_ESCAPE:
#                     pg.quit()
#                     sys.exit()
#                 if event.key == pg.K_DOWN and selected < 2:
#                     selected += 1
#                 if event.key == pg.K_UP and selected > 0:
#                     selected -= 1
#                 if event.key in (pg.K_SPACE, pg.K_RETURN):
#                     gameloop = False
#                     [menuNew, menuLoad, gameQuit][selected]()
#
#         menuDraw(selected)
#         mainClock.tick(60)
#
#     pg.quit()


# def menuNew(errtext = ""):
#     gameloop = True
#     selected = 0
#     text = ["",""]
#
#     while gameloop:
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 pg.quit()
#                 sys.exit()
#             if event.type == pg.KEYDOWN:
#                 if event.key == pg.K_ESCAPE:
#                     pg.quit()
#                     sys.exit()
#                 if event.key in (pg.K_SPACE, pg.K_RETURN) and text[selected]:
#                     if selected != 1:
#                         selected += 1
#                     else:
#                         gameloop = False
#                 elif event.key == pg.K_BACKSPACE:
#                     text[selected] = text[selected][:-1]
#                 elif event.unicode.isdigit():
#                     text[selected] += event.unicode
#
#
#         menuNewDraw(text, selected, errtext)
#         mainClock.tick(60)

if __name__ == '__main__':
    FirstMenu()
