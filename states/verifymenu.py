import pygame
import tkinter
import tkinter.filedialog
from .base import BaseState
from things.button import Button
import things.colors as Colors
from things.helpers import draw_text
import key_generation as kg

formats = (
    ("der", "*.der"),
    ("pem", "*.pem"),
    ("key", "*.key")
)

def do_nothing(menu):
    pass

def prompt_file():
    top = tkinter.Tk()
    top.withdraw()
    file_name = tkinter.filedialog.askopenfilename(parent=top)
    top.destroy()
    return file_name

def choose_file(menu):
    menu.chosen_file = prompt_file()

def prompt_key():
    top = tkinter.Tk()
    top.withdraw()
    key_name = tkinter.filedialog.askopenfilename(parent=top, filetypes=formats)

    if not key_name:
        return None

    for format in kg.FORMATS:
        if key_name.endswith(format):
            top.destroy()
            return key_name
    
    top.destroy()
    return None

def choose_key(menu):
    menu.chosen_key = prompt_key()

class VerifyMenu(BaseState):
    def __init__(self):
        super(VerifyMenu, self).__init__()
        self.font = pygame.font.SysFont("urwgothic", 24)

        bx = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "X", (870,40,40,40), self.switch_to("FIRSTMENU"))
        b1 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Wybierz plik", (300,250,180,40), choose_file)
        b2 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Wybierz klucz", (300,490,180,40), choose_key)

        b3 = Button(Colors.BTN_BASE, Colors.BTN_HOV, self.font, "Zweryfikuj", (600,490,240,40), do_nothing)
        self.buttons = [bx,b1,b2,b3]

        self.chosen_file = None
        self.chosen_key = None

        self.next_state = None

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.hover:
                    if button.text == "X":
                        self.chosen_file = None
                        self.chosen_key = None
                    button.click(self)

    def update(self, dt):
        for button in self.buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.hover = True
            else:
                button.hover = False

    def draw(self, surface):
        surface.fill(Colors.L_GREEN)
        for button in self.buttons:
            button.draw(surface)

        filebox = pygame.Rect(60,60,420,180)
        keybox = pygame.Rect(60,300,420,180)

        pygame.draw.rect(surface, Colors.D_GREEN, filebox)
        pygame.draw.rect(surface, Colors.D_GREEN, keybox)

        draw_text(surface, self.chosen_file if self.chosen_file else "Nie wybrano pliku", self.font, Colors.BLACK, filebox)
        draw_text(surface, self.chosen_key if self.chosen_key else "Nie wybrano klucza", self.font, Colors.BLACK, keybox)

        draw_text(surface, "Plik:", self.font, Colors.BLACK, pygame.Rect(60,60,100,50))
        draw_text(surface, "Publiczny klucz:", self.font, Colors.BLACK, pygame.Rect(100,300,100,50))
