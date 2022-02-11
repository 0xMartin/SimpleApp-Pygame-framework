"""
Simple library for multiple views game aplication with pygame

File:       label.py
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
from ..utils import *
from ..colors import *
from ..guielement import *


class Label(GUIElement):
    def __init__(self, view, style, text, h_centered=False, v_centered=False, x=0, y=0):
        """
        Create Label element 
        Parameters:
            view -> View where is element
            style -> More about style for this element in config/styles.json
            text -> Text of Label
            x -> X position
            y -> Y position
        """
        super().__init__(view, x, y, 0, 0, style)
        self.text = text
        self.h_centered = h_centered
        self.v_centered = v_centered
        self.font = pygame.font.SysFont(
            super().getStyle()["font_name"], super().getStyle()["font_size"], bold=super().getStyle()["font_bold"])

    def setCentered(self, centered):
        """
        Set label align centered
        Parameters:
            centered -> True: text will be aligned to the center of the coordinates
        """
        self.centered = centered

    def setText(self, text):
        """
        Set text of TextInput
        Parameters:
            text -> New text
        """
        self.text = text

    @overrides(GUIElement)
    def draw(self, view, screen):
        if len(self.text) != 0:
            text = self.font.render(
                self.text, 1, super().getStyle()["foreground_color"])
            x = super().getX()
            if self.h_centered:
                x -= text.get_width()/2
            y = super().getY()
            if self.v_centered:
                y -= text.get_height()/2
            screen.blit(text, (x, y))   

    @overrides(GUIElement)
    def processEvent(self, view, event):
        pass

    @overrides(GUIElement)
    def update(self, view):
        pass
