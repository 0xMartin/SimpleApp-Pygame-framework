"""
Simple library for multiple views game aplication with pygame

File:       application.py
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
import abc
import threading
from typing import final

from .guielement import *
from .colors import *
from .utils import *
from .stylemanager import *


# Application class, provides work with views
class Application:
    def __init__(self, views, fps):
        """
        Create Application
        Parameters:
            views -> List with views
        """
        self.fps = fps
        self.views = []
        self.visible_view = None
        self.inited = False
        self.stylemanager = StyleManager("SimpleApp/config/styles.json")
        self.setFillColor(WHITE)
        for v in views:
            if isinstance(v, View):
                v.setApplication(self)
                self.views.append(v)

    def setFillColor(self, color):
        self.fill_color = color

    def addView(self, view):
        """
        Add new view to application
        Parameters:
            view -> New view
        Returns False in case of fail
        """
        if(isinstance(view, View)):
            view.setApplication(self)
            self.views.append(view)
            return True
        else:
            return False

    def removeView(self, view):
        """
        Remove view from application
        Parameters:
            view -> View to be removed
        Returns False in case of fail
        """
        if(isinstance(view, View)):
            self.views.remove(view)
            return True
        else:
            return False

    def getScreen(self):
        """
        Get screen of application
        """
        return self.screen

    def init(self, width, height, name, icon):
        """
        Init window
        Parameters:
            name -> Name of application (window title)
            icon -> Icon of application 
        """
        self.width = max(width, 50)
        self.height = max(height, 50)
        self.name = name
        self.icon = icon

        self.stylemanager.init()

        pygame.init()
        self.default_font = pygame.font.SysFont("Verdana", 35, bold=True)
        pygame.display.set_caption(name)
        img = loadImage(self.icon)
        if img is not None:
            pygame.display.set_icon(img)
        self.screen = pygame.display.set_mode((width, height))
        self.inited = True

    def render_loop(self, arg):
        """
        Render loop
        """
        clock = pygame.time.Clock()
        while self.running:
            # clear screen
            if self.visible_view is not None:
                if self.visible_view.getFillColor() is None:
                    self.screen.fill(self.fill_color)
                else:
                    self.screen.fill(self.visible_view.getFillColor())
            # visible view proccess render
            if self.visible_view is not None:
                self.visible_view.render(self.screen)
            # render
            pygame.display.flip()
            clock.tick(self.fps)

    def update_loop(self, arg):
        """
        Update loop
        """
        clock = pygame.time.Clock()
        while self.running:
            if self.visible_view is not None:
                self.visible_view.update(self)
            clock.tick(self.fps)

    def run(self):
        """
        Run application loop
        Returns False in case of fail
        """
        if not self.inited:
            return False

        self.running = True

        # call start event for each view
        for view in self.views:
            view.createEvt_base(self.screen.get_width(),
                                self.screen.get_height())

        # threads for render and update loops
        render_thread = threading.Thread(target=self.render_loop, args=(1,))
        render_thread.start()
        update_thread = threading.Thread(target=self.update_loop, args=(1,))
        update_thread.start()

        # event loop
        clock = pygame.time.Clock()
        while self.running:
            # quit event
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                self.running = False
            # visible view proccess app events and render
            if self.visible_view is not None:
                self.visible_view.processEvt(event)
            clock.tick(60)

        # close
        pygame.quit()

        return True

    def close(self):
        """
        Close application
        """
        self.running = False
        # call close event for each view
        for view in self.views:
            view.closeEvt()
        self.views = []

    def showView(self, view):
        """
        Show view of aplication
        Parameters:
            view -> view to be displayed
        Return True in success
        """
        if view in self.views:
            # hide current visible view
            if self.visible_view is not None:
                self.visible_view.setVisibility(False)
                view.hideEvt()
            # show new view
            self.visible_view = view
            view.setVisibility(True)
            view.openEvt_base(self.screen.get_width(),
                              self.screen.get_height())
            # change window title
            if len(view.name) == 0:
                pygame.display.set_caption(self.name)
            else:
                pygame.display.set_caption(self.name + " - " + view.name)
            return True
        else:
            return False

    def showViewWithName(self, name):
        """
        Show view with specif name from list
        Parameters:
            name -> Name of view
        """
        for view in self.views:
            if view.name == name:
                self.showView(view)
                break

    def showViewWithID(self, id):
        """
        Show view with specif ID from list
        Parameters:
            id -> ID of view
        """
        for view in self.views:
            if view.ID == id:
                self.showView(view)
                break


# View class
class View(metaclass=abc.ABCMeta):
    def __init__(self, name, id):
        """
        Create view
        Parameters:
            name -> name of view (the name will be visible in the window title)
        """
        self.name = name
        self.ID = id
        self.visible = False
        self.fill_color = None
        self.GUIElements = []
        self.layout_manager_list = []

    def setID(self, id):
        self.ID = id

    def addGUIElements(self, elements):
        """
        Add gui elements to this view
        Parameters:
            elements -> List of GUIElement
        """
        for el in elements:
            if isinstance(el, GUIElement):
                self.GUIElements.append(el)

    def removeGUIElement(self, element):
        """
        Remove GUI element from this view
        Parameters:
            element -> Element to be removed
        """
        self.GUIElements.remove(element)

    @final
    def registerLayoutManager(self, layoutManager):
        """
        Register new layout manager
        Parameters:
            layoutManager -> New layout manager    
        """
        if isinstance(layoutManager, Layout):
            self.layout_manager_list.append(layoutManager)
            return True
        else:
            return False

    @final
    def unregisterLayoutManager(self, layoutManager):
        """
        Unregister layout manager
        Parameters:
            layoutManager -> layout manager    
        """
        self.layout_manager_list.remove(layoutManager)

    @final
    def getGUIElement(self):
        """
        Get list of GUIElements
        """
        return self.GUIElements

    def setFillColor(self, color):
        """
        Set fill color
        Parameters:
            color -> View fill color
        """
        self.fill_color = color

    @final
    def getFillColor(self):
        """
        Get fill color
        """
        return self.fill_color

    @final
    def setVisibility(self, visible):
        """
        Set visibility of view
        Parameters:
            visible -> visibility
        """
        self.visible = visible

    def setApplication(self, app):
        """
        Assigns an application to this view
        Parameters:
            app -> Application
        """
        if(isinstance(app, Application)):
            self.app = app
            return True
        else:
            return False

    @final
    def createEvt_base(self, width, height):
        """
        Create event + layout update
        """
        # call abstract def
        self.createEvt()
        # update layout managers
        for lm in self.layout_manager_list:
            lm.update(width, height)

    @abc.abstractmethod
    def createEvt(self):
        """
        Create event
        Called when the application starting
        """
        pass

    @abc.abstractmethod
    def closeEvt(self):
        """
        Close event
        Called when the application closing
        """
        pass

    @final
    def openEvt_base(self, width, height):
        """
        Open event + layout update
        """
        # update layout managers
        for lm in self.layout_manager_list:
            lm.update(width, height)
        # call abstract def
        self.openEvt()

    @abc.abstractmethod
    def openEvt(self):
        """
        Open event
        Called when the application show this view
        """
        pass

    @abc.abstractmethod
    def hideEvt(self):
        """
        Hide event
        Called when the application hide this view
        """
        pass

    @final
    def processEvt(self, event):
        """
        Process event from application
        Parameters:
            event -> Application event
        """
        # all events send to view elements
        if self.app is not None:
            for el in self.GUIElements:
                el.processEvent(self, event)

    @final
    def render(self, screen):
        """
        Render view
        """
        if self.app is not None:
            for el in self.GUIElements:
                el.draw(self, screen)

    @final
    def update(self, screen):
        """
        Update view
        """
        if self.app is not None:
            for el in self.GUIElements:
                el.update(self)

# base layout manager for view


class Layout(metaclass=abc.ABCMeta):
    def __init__(self, view):
        """
        Base layout class, automatically register layout manager to view
        Parameters:
            screen -> Pygame screen
            view -> Application view
        """
        if isinstance(view, View):
            self.view = view
        self.layoutElements = []
        # register
        view.registerLayoutManager(self)

    @final
    def getLayoutElements(self):
        """
        Return all elements in layout
        """
        return self.layoutElements

    @final
    def addElement(self, element, propt):
        """
        Add new element to layout
        Parameters:
            element -> GUIElement
            propt -> Property of element for layout manager (LEFT, RIGHT, CENTER, ...) denpends on manager
        """
        if isinstance(element, GUIElement):
            self.layoutElements.append({"element": element, "propt": propt})

    @abc.abstractmethod
    def update(self, width, height):
        """
        Update layout
        Parameters:
            width -> Width of view screen  
            height -> Height of view screen   
        """
        pass

    @final
    def getView(self):
        return self.view
