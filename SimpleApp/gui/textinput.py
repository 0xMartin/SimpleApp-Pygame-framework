import pygame
from ..utils import *
from ..colors import *
from ..guielement import *
from ..application import *


class TextInput(GUIElement):
    def __init__(self, view, x, y, width, height, style, text):
        """
        Create TextInput element 
        Parameters:
            x -> X position
            y -> Y position
            width -> Width of TextInput
            height -> Height of TextInput
            style -> Style of TextInput {font_name, font_size, font_bold, b_color, f_color}
            text -> Text of TextInput
        """
        super().__init__(view, x, y, width, height, style)
        self.callback = None
        self.text = text
        self.font = pygame.font.SysFont(
            style["font_name"], style["font_size"], bold=style["font_bold"])

    def setText(self, text):
        """
        Set text of TextInput
        Parameters:
            text -> New text
        """
        self.text = text

    def setTextChangedEvt(self, callback):
        """
        Set text changed event
        Parameters:
            callback -> Event callback    
        """
        self.callback = callback

    def draw(self, view, screen):
        # background
        if super().isSelected():
            pygame.draw.rect(screen, colorChange(super().getStyle()[
                             "b_color"], 0.4), super().getViewRect(), border_radius=5)
        else:
            pygame.draw.rect(screen, super().getStyle()[
                             "b_color"], super().getViewRect(), border_radius=5)

        # create subsurface
        surface = screen.subsurface(super().getViewRect())
        offset = 0
        if len(self.text) != 0:
            text = self.font.render(
                self.text, 1, super().getStyle()["f_color"])
            offset = max(text.get_width() + 20 - super().getWidth(), 0)
            if not super().isSelected():
                offset = 0
            surface.blit(
                text, (5 - offset, (super().getHeight() - text.get_height())/2))

        # caret
        if super().isSelected() and generateSignal(400):
            x = 8 + (0 if (len(self.text) == 0) else text.get_width()) - offset
            y = surface.get_height() * 0.2
            pygame.draw.line(surface, super().getStyle()[
                             "f_color"], (x, y), (x, surface.get_height() - y), 2)

        # outline
        pygame.draw.rect(screen, super().getStyle()[
                         "f_color"], super().getViewRect(), 2, border_radius=5)

    def processEvent(self, view, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inRect(event.pos[0], event.pos[1], super().getViewRect()):
                super().select()
            else:
                super().unSelect()
        elif event.type == pygame.KEYDOWN:
            if super().isSelected():
                if self.callback is not None:
                    self.callback(self)
                if event.key == pygame.K_BACKSPACE:
                    if(len(self.text) <= 1):
                        self.text = ""
                    else:
                        self.text = self.text[0: -1]
                else:
                    if event.key >= 0 and event.key <= 127:
                        if event.mod & pygame.KMOD_SHIFT:
                            self.text += chr(event.key).upper()
                        else:
                            self.text += chr(event.key)

    def update(self, view):
        pass
