import pygame
from ..utils import *
from ..colors import *
from ..guielement import *
from ..application import *


class Button(GUIElement):
    def __init__(self, view, x, y, width, height, style, text):
        """
        Create button
        Parameters:
            x -> X position
            y -> Y position
            width -> Width of button
            height -> Height of button
            style -> Style of button {font_name, font_size, font_bold, b_color, f_color}
            text - Text of button
        """
        super().__init__(view, x, y, width, height, style)
        self.text = text
        self.callback = None
        self.hover = False
        self.font = pygame.font.SysFont(
            style["font_name"], style["font_size"], bold=style["font_bold"])

    def setClickEvt(self, callback):
        """
        Set button click event
        Parameters:
            callback -> callback function
        """
        self.callback = callback

    def draw(self, view, screen):
        # background
        if self.hover:
            pygame.draw.rect(screen, colorChange(
                super().getStyle()["b_color"], -0.6), super().getViewRect(), border_radius=10)
        else:
            pygame.draw.rect(screen, super().getStyle()[
                             "b_color"], super().getViewRect(), border_radius=10)
        # button text
        if len(self.text) != 0:
            text = self.font.render(
                self.text, 1, super().getStyle()["f_color"])
            screen.blit(text, (super().getX() + (super().getWidth() - text.get_width())/2,
                               super().getY() + (super().getHeight() - text.get_height())/2))

    def processEvent(self, view, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inRect(event.pos[0], event.pos[1], super().getViewRect()):
                if self.callback is not None:
                    self.callback(self)
        elif event.type == pygame.MOUSEMOTION:
            if inRect(event.pos[0], event.pos[1], super().getViewRect()):
                self.hover = True
            else:
                self.hover = False

    def update(self, view):
        pass
