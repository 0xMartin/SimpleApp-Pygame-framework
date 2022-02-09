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
from ..application import *


class Label(GUIElement):
    def __init__(self, view, x, y, style, text):
        """
        Create Label element 
        Parameters:
            x -> X position
            y -> Y position
            style -> Style of TextInput {font_name, font_size, font_bold, b_color, f_color}
            text -> Text of TextInput
        """
        super().__init__(view, x, y, 0, 0, style)
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

    def draw(self, view, screen):
        if len(self.text) != 0:
            text = self.font.render(
                self.text, 1, super().getStyle()["f_color"])
            screen.blit(text, (super().getX(), super().getY()))

    def processEvent(self, view, event):
        pass

    def update(self, view):
        pass
