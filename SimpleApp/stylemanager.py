"""
Simple library for multiple views game aplication with pygame

File:       stylemanager.py
Date:       09.02.2022

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

from .utils import *
from .gui import *


class StyleManager:
    def __init__(self, styles_path):
        """
        Create style manager
        Parameters:
            styles_path -> Path where is file with styles for all guil elements    
        """
        self.styles_path = styles_path

    def init(self):
        """
        Init style manager
        """
        self.styles = loadConfig(self.styles_path)

    def getStyleWithName(self, name):
        """
        Get all styles
        Parameters:
            name -> Name of style
        """
        if name not in self.styles.keys():
            return None
        else:
            return self.processStyle(self.styles[name])

    def getStyle(self, quielemnet):
        """
        Get style for specific gui element
        Parameters:
            quielemnet -> gui element
        """
        if self.styles is None:
            return None

        if isinstance(quielemnet, Button):
            return self.processStyle(self.styles["Button"])
        elif isinstance(quielemnet, Canvas):
            return self.processStyle(self.styles["Canvas"])
        elif isinstance(quielemnet, CheckBox):
            return self.processStyle(self.styles["CheckBox"])
        elif isinstance(quielemnet, Graph):
            return self.processStyle(self.styles["Graph"])
        elif isinstance(quielemnet, Image):
            return self.processStyle(self.styles["Image"])
        elif isinstance(quielemnet, Label):
            return self.processStyle(self.styles["Label"])
        elif isinstance(quielemnet, RadioButton):
            return self.processStyle(self.styles["RadioButton"])
        elif isinstance(quielemnet, Table):
            return self.processStyle(self.styles["Table"])
        elif isinstance(quielemnet, TextInput):
            return self.processStyle(self.styles["TextInput"])
        elif isinstance(quielemnet, VerticalScroll):
            return self.processStyle(self.styles["VerticalScroll"])

    def processStyle(self, style):
        # colors
        new_style = style.copy()
        for tag in new_style.keys():
            if "color" in tag:
                rgb = new_style[tag].split(",")
                new_style[tag] = tuple([int(rgb[0]), int(rgb[1]), int(rgb[2])])
            elif isinstance(new_style[tag], dict):
                new_style[tag] = self.processStyle(new_style[tag])   
        return new_style