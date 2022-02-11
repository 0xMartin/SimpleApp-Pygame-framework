"""
Simple library for multiple views game aplication with pygame

File:       textinput.py
Date:       08.02.2022

Github:     https://github.com/0xMartin
Email:      martin.krcma1@gmail.com
 
Copyright (C) 2022 Martin Krcma
 
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:
 
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import pygame
import re
from ..utils import *
from ..colors import *
from ..guielement import *


class TextInput(GUIElement):
    def __init__(self, view, style, text, width=0, height=0, x=0, y=0):
        """
        Create TextInput element 
        Parameters:
            view -> View where is element
            style -> more about style for this element in config/styles.json
            text -> Text of TextInput
            width -> Width of TextInput
            height -> Height of TextInput
            x -> X position
            y -> Y position
        """
        super().__init__(view, x, y, width, height, style)
        self.callback = None
        self.filter_pattern = None
        self.text = text
        self.font = pygame.font.SysFont(
            super().getStyle()["font_name"], super().getStyle()["font_size"], bold=super().getStyle()["font_bold"])

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

    def setFilterPattern(self, pattern):
        """
        Set filter pattern
        Parameters:
            pattern -> pattern for text in this text input
        """
        # "^([A-Z][0-9]+)+$"
        self.filter_pattern = re.compile(pattern)

    @overrides(GUIElement)
    def draw(self, view, screen):
        # background
        if super().isSelected():
            c = super().getStyle()["background_color"]
            pygame.draw.rect(screen, colorChange(c, 0.4 if c[0] > 128 else 0.7), super().getViewRect(), border_radius=5)
        else:
            pygame.draw.rect(screen, super().getStyle()[
                             "background_color"], super().getViewRect(), border_radius=5)

        # create subsurface
        surface = screen.subsurface(super().getViewRect())
        offset = 0
        if len(self.text) != 0:
            text = self.font.render(
                self.text, 1, super().getStyle()["foreground_color"])
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
                             "foreground_color"], (x, y), (x, surface.get_height() - y), 2)

        # outline
        pygame.draw.rect(screen, super().getStyle()[
                         "outline_color"], super().getViewRect(), 2, border_radius=5)

    @overrides(GUIElement)
    def processEvent(self, view, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # select textinput
            if inRect(event.pos[0], event.pos[1], super().getViewRect()):
                super().select()
            else:
                super().unSelect()
                # text filter
                if self.filter_pattern is not None:
                    if not self.filter_pattern.match(self.text):
                        # delate text
                        self.text = ""  
        elif event.type == pygame.KEYDOWN:
            # text writing
            if super().isSelected():
                if self.callback is not None:
                    self.callback(self)
                if event.key == pygame.K_BACKSPACE:
                    # delate last char
                    if(len(self.text) <= 1):
                        self.text = ""
                    else:
                        self.text = self.text[0: -1]
                else:
                    # new char
                    if event.key >= 0 and event.key <= 127:
                        if event.mod & pygame.KMOD_SHIFT:
                            self.text += chr(event.key).upper()
                        else:
                            self.text += chr(event.key)

    @overrides(GUIElement)
    def update(self, view):
        pass
