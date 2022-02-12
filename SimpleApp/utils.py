"""
Simple library for multiple views game aplication with pygame

File:       utils.py
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
from time import time
import os.path
import json
import math
import copy

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pylab


def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


def inRect(x, y, rect):
    """
    Check if x, y is in rect
    Parameters:
        x -> X position
        y -> Y position
        rect -> rectangle {left, top, width, height}
    """
    if x >= rect.left and y >= rect.top and x <= rect.left + rect.width and y <= rect.top + rect.height:
        return True
    else:
        return False


def generateSignal(ms_periode):
    """
    Genereta pariodic signal -> (ms_periode) True -> (ms_periode) False -> ...
    Parameters:
        ms_periode -> Half periode of signal in ms
    """
    return round((time() * 1000) / ms_periode) % 2 == 0


def loadImage(img_path):
    """
    Load image from File system
    Parameters:
        img_path -> Path of image
    """
    if os.path.isfile(img_path):
        return pygame.image.load(img_path)
    else:
        return None


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


def drawGraph(width, height, data):
    """
    Draw graph and print it to the image
    Parameters:
        width -> Width of graph
        height -> Height of graph
        data -> Data of graph
    """
    matplotlib.use("Agg")

    fig = pylab.figure(figsize=[width/100, height/100], dpi=100)
    fig.patch.set_alpha(0.0)

    ax = fig.gca()
    ax.plot(data)

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.buffer_rgba()

    return pygame.image.frombuffer(raw_data, canvas.get_width_height(), "RGBA")


def loadConfig(path):
    """
    Load config
    Parameters:
        path -> path to the file
    """
    if not os.path.isfile(path):
        return None
    f = open(path)
    data = json.load(f)
    f.close()
    return data

