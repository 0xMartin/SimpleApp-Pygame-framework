"""
Simple library for multiple views game aplication with pygame

File:       slider.py
Date:       10.02.2022

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


class Slider(GUIElement):
    def __init__(self, view, style, width=0, height=0, x=0, y=0):
        """
        Create Slider
        Parameters:
            view -> View where is element
            style -> More about style for this element in config/styles.json
            width -> Width of button
            height -> Height of button
            x -> X position
            y -> Y position
        """
        super().__init__(view, x, y, width, height, style)
        self.callback = None

    def setOnValueChange(self, callback):
        """
        Set on value change event callback
        Parameters:
            callback -> callback function
        """
        self.callback = callback

    def draw(self, view, screen):
        pass

    def processEvent(self, view, event):
        pass

    def update(self, view):
        pass
