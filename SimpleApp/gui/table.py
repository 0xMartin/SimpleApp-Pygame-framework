"""
Simple library for multiple views game aplication with pygame

File:       table.py
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
from SimpleApp.gui.vertical_scroll import VerticalScroll


class Table(GUIElement):
    def __init__(self, view, style, data, width=0, height=0, x=0, y=0):
        """
        Create Table element
        Parameters:
            view -> View where is element
            style -> more about style for this element in config/styles.json
            data -> Data of Table
            width -> Width of Table
            height -> Height of Table
            x -> X position
            y -> Y position
        """
        self.last_data = None
        self.body_offset = 0
        super().__init__(view, x, y, width, height, style)
        self.scroll = VerticalScroll(
            view,
            super().getStyle()["scroller"],
            super().getStyle()["body"]["scroller_width"]
        )
        self.scroll.setOnScrollEvt(self.tableScroll)
        self.refreshTable(data)

    def tableScroll(self, position):
        """
        Event for table body scroll
        Parameters:
            position -> position of table body (0.0 - 1.0)     
        """
        header_height = self.header_font.get_height() * 1.8
        total_body_data_height = header_height + self.body_font.get_height() * 1.2 * \
            len(self.body)
        self.body_offset = -max(
            0, (total_body_data_height - super().getHeight())) * position

    def refreshTable(self, data=None):
        if data is None:
            data = self.last_data
        self.last_data = data
        if data is None:
            return

        """
        Refresh table data
        Parameters:
            data -> {header: [], body: [[],[],[], ...]}
        """
        self.header_font = pygame.font.SysFont(
            super().getStyle()["header"]["font_name"],
            super().getStyle()["header"]["font_size"],
            bold=super().getStyle()["header"]["font_bold"]
        )
        self.body_font = pygame.font.SysFont(
            super().getStyle()["body"]["font_name"],
            super().getStyle()["body"]["font_size"],
            bold=super().getStyle()["body"]["font_bold"]
        )
        # build table header
        self.header = data["header"]
        # build table body
        self.body = data["body"]
        # scroller
        self.scroll.setX(super().getX() + super().getWidth() -
                         1 - super().getStyle()["body"]["scroller_width"])
        self.scroll.setY(super().getY())
        self.scroll.setWidth(super().getStyle()["body"]["scroller_width"])
        self.scroll.setHeight(super().getHeight())
        header_height = self.header_font.get_height() * 1.8
        total_body_data_height = header_height + self.body_font.get_height() * 1.2 * \
            len(self.body)
        self.scroll.setScrollerSize((1.0 - max(0, total_body_data_height - super(
        ).getHeight()) / total_body_data_height) * self.scroll.getHeight())

    @overrides(GUIElement)
    def updateViewRect(self):
        super().updateViewRect()
        # scroller
        self.refreshTable()

    @overrides(GUIElement)
    def draw(self, view, screen):
        screen.set_clip(super().getViewRect())
        # draw table body background
        w = super().getWidth() - super().getStyle()["body"]["scroller_width"]
        rect = pygame.Rect(
            super().getX(),
            super().getY(),
            w,
            super().getHeight()
        )
        pygame.draw.rect(
            screen,
            super().getStyle()["body"]["background_color"],
            rect
        )
        for i in range(len(self.header) - 1):
            pygame.draw.line(
                screen,
                colorChange(super().getStyle()[
                            "body"]["background_color"], -0.5),
                (super().getX() + w /
                 len(self.header) * (i + 1), super().getY()),
                (super().getX() + w /
                 len(self.header) * (i + 1), super().getY() + super().getHeight() - 4),
                2
            )
        # draw body data
        for j, row in enumerate(self.body):
            for i, cell in enumerate(row):
                if len(cell) != 0:
                    text = self.body_font.render(
                        cell, 1, super().getStyle()["body"]["foreground_color"])
                    header_offset = self.header_font.get_height() * 1.8
                    screen.blit(
                        text,
                        (
                            super().getX() + w / len(self.header) * i + 5,
                            super().getY() + header_offset +
                            self.body_font.get_height() * 1.2 * j + self.body_offset
                        )
                    )

        # draw table header
        if self.header is not None:
            pygame.draw.rect(
                screen,
                super().getStyle()["header"]["background_color"],
                pygame.Rect(
                    super().getX(),
                    super().getY(),
                    w,
                    self.header_font.get_height() * 1.8
                )
            )
            for i, col in enumerate(self.header):
                if len(col) != 0:
                    text = self.header_font.render(
                        col, 1, super().getStyle()["header"]["foreground_color"])
                    screen.blit(
                        text,
                        (
                            super().getX() + w / len(self.header) * i + 5,
                            super().getY() + self.header_font.get_height() * 0.4
                        )
                    )
        # draw scroll bar
        self.scroll.draw(view, screen)
        # draw outline
        pygame.draw.rect(
            screen,
            super().getStyle()["header"]["background_color"],
            rect,
            2
        )
        # reset clip
        screen.set_clip(None)

    @overrides(GUIElement)
    def processEvent(self, view, event):
        self.scroll.processEvent(view, event)

    @overrides(GUIElement)
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
