"""
Simple library for multiple views game aplication with pygame

File:       combobox.py
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

from SimpleApp.gui.checkbox import CheckBox
from SimpleApp.gui.label import Label
import pygame
from ..utils import *
from ..colors import *
from ..guielement import *
from ..application import *


class RadioButton(GUIElement):
    def __init__(self, view, x, y, style, text, group):
        """
        Create RadioButton element 
        Parameters:
            x -> X position
            y -> Y position
            style -> Style of TextInput {font_name, font_size, font_bold, b_color, f_color}
            text -> Text of TextInput
        """
        super().__init__(view, x, y, style["size"], style["size"], style)
        self.label = Label(view, x, y, style, text)
        self.group = group
        group.addRadioButton(self)
        self.checked = False
        self.callback = None
        self.hover = False
        self.font = pygame.font.SysFont(
            style["font_name"], style["font_size"], bold=style["font_bold"])

    def setText(self, text):
        """
        Set text of TextInput
        Parameters:
            text -> New text
        """
        if self.label is not None:
            self.label.setText(text)

    def setCheckedEvt(self, callback):
        """
        Set checkbox Checked event
        Parameters:
            callback -> callback function
        """
        self.callback = callback

    def setChecked(self, checked):
        """
        Set checked state of this check box
        Parameters:
            checked -> True = Is checked    
        """
        self.checked = checked

    def isChecked(self):
        """
        Return if this check box is checked
        """
        return self.checked

    def draw(self, view, screen):
        # lable
        if self.label is not None:
            self.label.setX(super().getX() + super().getWidth() + 5)
            text_height = self.font.size("W")[1]
            self.label.setY(super().getY() +
                            (super().getWidth() - text_height)/2)
            self.label.draw(view, screen)
        # radio box
        center = (
            super().getX() + super().getWidth()/2,
            super().getY() + super().getWidth()/2
        )
        if self.hover:
            pygame.draw.circle(screen, colorChange(super().getStyle()[
                "b_color"], -0.6), center, super().getWidth() / 2)
        else:
            pygame.draw.circle(screen, super().getStyle()[
                "b_color"], center, super().getWidth() / 2)
        pygame.draw.circle(screen, super().getStyle()[
            "f_color"], center, super().getWidth() / 2, 2)
        # check
        if self.checked:
            pygame.draw.circle(screen, super().getStyle()[
                "f_color"], center, super().getWidth() / 4)

    def processEvent(self, view, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if inRect(event.pos[0], event.pos[1], super().getViewRect()):
                if self.callback is not None:
                    self.callback(self)
                self.group.checkRadioButton(self)
        elif event.type == pygame.MOUSEMOTION:
            if inRect(event.pos[0], event.pos[1], super().getViewRect()):
                self.hover = True
            else:
                self.hover = False

    def update(self, view):
        pass


class RadioButtonGroup:
    def __init__(self, radiobtns):
        """
        Create RadioButton group
        Parameters:
            radiobtns -> list with radio buttons
        """
        self.radiobtns = []
        for r in radiobtns:
            if isinstance(r, RadioButton):
                self.radiobtns.append(r)

    def addRadioButton(self, radiobtn):
        """
        Add radio button to this group
        Parameters:
            radiobtn -> Combo box    
        """
        if isinstance(radiobtn, RadioButton):
            self.radiobtns.append(radiobtn)

    def removeRadioButton(self, radiobtn):
        """
        Remove radio button from this group
        Parameters:
            radiobtn -> Combo box    
        """
        self.radiobtns.remove(radiobtn)

    def getRadioButton(self):
        """
        Return checked radio button from group
        """
        for r in self.radiobtns:
            if r.isChecked():
                return r

    def checkRadioButton(self, radiobtn):
        """
        Check one radio button from this group
        Parameters:
            radiobtn -> combo box    
        """
        if isinstance(radiobtn, RadioButton):
            for r in self.radiobtns:
                if r != radiobtn:
                    r.setChecked(False)
                else:
                    r.setChecked(True)
