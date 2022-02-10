"""
Simple library for multiple views game aplication with pygame

File:       graph.py
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

import pygame
from ..utils import *
from ..colors import *
from ..guielement import *
from ..application import *


class Graph(GUIElement):
    def __init__(self, view, data, width=0, height=0, x=0, y=0):
        """
        Create Graph element
        Parameters:
            view -> View where is element
            data -> Data of graph
            width -> Width of image
            height -> Height of image
            x -> X position
            y -> Y position
        """
        self.data = data
        super().__init__(view, x, y, width, height, None)

    # overrides
    def setWidth(self, width):
        super().setWidth(width)
        self.refreshGraph(self.data)

    # override
    def setHeight(self, height):
        super().setHeight(height)
        self.refreshGraph(self.data)

    def refreshGraph(self, data):
        if data is not None and super().getWidth() > 50 and super().getHeight() > 50:
            self.graph = drawGraph(
                super().getWidth(), super().getHeight(), data)

    def draw(self, view, screen):
        if self.graph is not None:
            screen.blit(pygame.transform.scale(self.graph, (super().getWidth(
            ), super().getHeight())), (super().getX(), super().getY()))

    def processEvent(self, view, event):
        pass

    def update(self, view):
        pass


def buildGraphData(dataset_list):
    data = []
    l = len(dataset_list[0])
    for i in range(l):
        i_data = []
        for ds in dataset_list:
            if i < len(ds):
                i_data.append(ds[i])
            else:
                i_data.append(0)
        data.append(tuple(i_data))
    return data