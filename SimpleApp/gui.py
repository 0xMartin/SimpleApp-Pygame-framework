"""
Simple library for multiple views game aplication with pygame

File:       gui.py
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
from typing import final
import abc

from .colors import *
from .utils import *


class GUIElement(metaclass=abc.ABCMeta):
    def __init__(self, view, x, y, width, height, style):
        """
        Create GUIElement
        Parameters:
            x -> X position
            y -> Y position
            width -> Width of Element
            height -> Height of Element
            style -> Style of Element
        """
        self.view = view
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.style = style

        self.selected = False
        self.updateViewRect()

    @final
    def getX(self):
        """
        Get x position of this element
        """
        return self.x

    @final
    def getY(self):
        """
        Get y position of this element
        """
        return self.y

    @final
    def getWidth(self):
        """
        Get width of this element
        """
        return self.width

    @final
    def getHeight(self):
        """
        Get height of this element
        """
        return self.height

    @final
    def getStyle(self):
        """
        Get style of this element
        """
        return self.style

    @final
    def setX(self, x):
        """
        Set x position of this element
        Parameters:
            x -> New X position
        """
        self.x = x
        self.updateViewRect()

    @final
    def setY(self, y):
        """
        Set y position of this element
        Parameters:
            y -> New Y position
        """
        self.y = y
        self.updateViewRect()

    @final
    def setWidth(self, width):
        """
        Set width of this element
        Parameters:
            width -> New width
        """
        self.width = width
        self.updateViewRect()

    @final
    def setHeight(self, height):
        """
        Set height of this element
        Parameters:
            height -> New height
        """
        self.height = height
        self.updateViewRect()

    @final
    def setStyle(self, style):
        """
        Set style of this element
        Parameters:
            style -> New style
        """
        self.style = style

    @final
    def updateViewRect(self):
        """
        Update view rect of this element
        """
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    @final
    def getViewRect(self):
        """
        Get view rect of this element
        """
        return self.rect

    @final
    def select(self):
        self.selected = True

    @final
    def unSelect(self):
        self.selected = False

    @final
    def isSelected(self):
        return self.selected

    @abc.abstractmethod
    def draw(self, view, screen):
        """
        Draw element on screen
        """
        pass

    @abc.abstractmethod
    def processEvent(self, view, event):
        """
        Process event from view
        """
        pass

    @abc.abstractmethod
    def update(self, view):
        """
        Update element
        """
        pass


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

# TextInput


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
