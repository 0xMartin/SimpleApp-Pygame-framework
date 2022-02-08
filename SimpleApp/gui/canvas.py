import pygame
from ..utils import *
from ..colors import *
from ..guielement import *
from ..application import *


class Canvas(GUIElement):
    def __init__(self, view, x, y, width, height, style):
        """
        Create button
        Parameters:
            x -> X position
            y -> Y position
            width -> Width of button
            height -> Height of button
            style -> Style of button {b_color, f_color}
        """
        super().__init__(view, x, y, width, height, style)
        self.callback = None

    def setPaintEvt(self, callback):
        """
        Set paint event
        Parameters:
            callback -> callback function
        """
        self.callback = callback

    def draw(self, view, screen):
        # background
        pygame.draw.rect(screen, super().getStyle()[
                         "b_color"], super().getViewRect())

        # create subsurface
        surface = screen.subsurface(super().getViewRect())
        # call paint callback
        if self.callback is not None:
            self.callback(surface)

        # outline
        pygame.draw.rect(screen, super().getStyle()[
                         "f_color"], super().getViewRect(), 2)

    def processEvent(self, view, event):
        pass

    def update(self, view):
        pass
