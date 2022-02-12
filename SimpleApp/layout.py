"""
Simple library for multiple views game aplication with pygame

File:       layout.py
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
from .colors import *
from .guielement import *
from .application import *


class AbsoluteLayout(Layout):
    def __init__(self, view):
        """
        Create Absolute Layout
        addElement(el, propt) -> propt : {x, y, width, height}
        (x, y, ...) value type: number in px ('50', '4', ...) or % ('20%', '5%', ...)
        """
        super().__init__(view)

    @overrides(Layout)
    def updateLayout(self, width, height):
        for el in super().getLayoutElements():
            gui_el = el["element"]
            propts = el["propt"]
            if propts is not None:
                for i, propt in enumerate(propts):
                    if propt[-1] == '%':
                        val = float(propt[0:-1])
                        if i % 2 == 0:
                            val = val / 100.0 * width
                        else:
                            val = val / 100.0 * height
                    else:
                        val = float(propt)
                    if i == 0:
                        gui_el.setX(val)
                    elif i == 1:
                        gui_el.setY(val)
                    elif i == 2:
                        gui_el.setWidth(val)
                    else:
                        gui_el.setHeight(val)


class RelativeLayout(Layout):
    def __init__(self, view, horizontal):
        """
        Create Relative Layout
        addElement(el, propt) -> "parent" (his position does not change), "child" (his position depends on the parent)
        """
        super().__init__(view)
        self.horizontal = horizontal

    @overrides(Layout)
    def updateLayout(self, width, height):
        cnt = len(super().getLayoutElements())
        if cnt == 0:
            return

        parent = next((el for el in super().getLayoutElements()
                      if el["propt"] == "parent"), None)
        if parent is None:
            return
        parent = parent["element"]

        if self.horizontal:
            w_step = (width - parent.getX()) / (cnt)
            h_step = height / (cnt)
        else:
            w_step = width / (cnt)
            h_step = (height - parent.getY()) / (cnt)

        i = 1
        for el in super().getLayoutElements():
            if el["propt"] is not None:
                if el["propt"] == "child":
                    gui_el = el["element"]
                    if self.horizontal:
                        gui_el.setX(parent.getX() + i * w_step)
                        if gui_el != parent:
                            i = i + 1
                            gui_el.setY(parent.getY())
                    else:
                        if gui_el != parent:
                            i = i + 1
                            gui_el.setX(parent.getX())
                        gui_el.setY(parent.getY() + i * h_step)
