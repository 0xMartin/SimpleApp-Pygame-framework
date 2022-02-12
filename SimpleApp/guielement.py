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


class GUIElement(metaclass=abc.ABCMeta):
    def __init__(self, view, x, y, width, height, style, selected_cursor=pygame.SYSTEM_CURSOR_HAND):
        """
        Create GUIElement
        Parameters:
            x -> X position
            y -> Y position
            width -> Width of Element
            height -> Height of Element
            style -> Style of 
            selected_cursor -> The type of cursor that appears when this element is selected
        """
        self.view = view
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected_cursor = selected_cursor

        sm = view.getApp().getStyleManager()
        if style is None:
            self.style = sm.getStyle(self.__class__.__name__)
        else:
            self.style = style

        self.selected = False
        self.updateViewRect()

    def setSelectCursor(self, cursor):
        """
        Set cursor type when this element is selected
        Parameters:
            cursor -> The type of cursor that appears when this element is selected
        """
        self.selected_cursor = cursor

    @final
    def getSelectCursor(self):
        """
        Return cursor type when this element is selected
        """
        return self.selected_cursor

    @final
    def getView(self):
        """
        Get view of this element
        """
        return self.view

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
        
    def setStyle(self, style):
        """
        Set style of this element
        Parameters:
            style -> new style of element
        """
        self.style = style

    def setX(self, x):
        """
        Set x position of this element
        Parameters:
            x -> New X position
        """
        self.x = x
        self.updateViewRect()

    def setY(self, y):
        """
        Set y position of this element
        Parameters:
            y -> New Y position
        """
        self.y = y
        self.updateViewRect()

    def setWidth(self, width):
        """
        Set width of this element
        Parameters:
            width -> New width
        """
        self.width = width
        self.updateViewRect()

    def setHeight(self, height):
        """
        Set height of this element
        Parameters:
            height -> New height
        """
        self.height = height
        self.updateViewRect()

    def setStyle(self, style):
        """
        Set style of this element
        Parameters:
            style -> New style
        """
        self.style = style

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
        """
        Select element
        """
        self.selected = True

    @final
    def unSelect(self):
        """
        Unselect element
        """
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

class Container(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getChilds(self):
        pass