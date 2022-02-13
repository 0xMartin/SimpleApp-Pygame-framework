# SimpleApp framework
## About
This simple pygame-based framework allows you to divide your game/application to more views and yous GUI elemnets (form controls). In views you can use defined GUI elements (like: TextInput, Button, CheckBox, Label, ...). You can simply implement your own view with GUI elements that you want to use. Also is there posibility of customizing elements or create new one. Each element has it own style and you can modifi it in code or in config of library where are stylesheets for all elements. Almost everything is stylizable and can by stored to .json stylesheet file and loaded using style manager.
Almost everything is stylizable and can by stored to .json stylesheet file and loaded using style manager. The application basically offers two sets of style (light / dark) and it is possible to switch between them while the application is running (however, some changes will not be made until the application is restarted: typically fonts).

### Preview
> Light theme
<div>
  <img src="./doc/img1.png" width="48%">
  <img src="./doc/img2.png" width="48%">
</div>

> Dark theme
<img src="./doc/img3.png" width="48%">

## How to use
Implement your own view
```python
class View2(View):
    def __init__(self):
        # base contructor (set name and ID of view)
        super().__init__("View 2", VIEW2_ID)

    @overrides(View)
    def createEvt(self):
        # layout manager
        al = AbsoluteLayout(self)

        # button
        btn = Button(self, None, "Go to view 1")
        # assigns button to layout manager and set properties [x_position, y_position, width, height]
        al.addElement(btn, ['25%', '85%', '50%', '40'])
        # on button click navigate to view with ID {VIEW1_ID}
        btn.setClickEvt(lambda btn: self.app.showViewWithID(VIEW1_ID))

        # add button to view element list
        self.addGUIElements([btn])

    @overrides(View)
    def closeEvt(self):
        pass

    @overrides(View)
    def openEvt(self):
        pass

    @overrides(View)
    def hideEvt(self):
        pass
        
    @overrides(View)
    def reloadStyleEvt(self):
        pass
```
In entry point of program create instance of Application, add your view, show some view and run app
```python
view1 = View1()
view2 = View2()
app = Application([view1, view2], 30, 1, True)
app.init(640, 400, "Application", "")
app.showView(view1)
app.run()
```

## Application
The main component of the framework. Provides switched view work with them (rendering, events, updates, ...). Here I set the styles, icon, application name, window size, ...

---
```python
def __init__(self, views, fps=60, ups=60, dark=False)
```
  * Create instance of Application
  * __Parameters__
    * __views__: List with views (list element type: ```SimpleApp.application.View```)
    * __fps__: Rendering - Frame per second (type: ```int```)
    * __ups__: Updating - Updates per second (for example physics) (type: ```int```)
    * __dark__: If is "True" than load dark theme stylesheet (type: ```boolean```)
---

```python
def setFillColor(self, color)
```
  * Set default fill color for views of application
  * __Parameters__
    * __color__: Fill color (type: ```tuple```)

---
```python
def addView(self, view)
```
  * Add new view to application
  * __Parameters__
    * __view__: New view (type: ```SimpleApp.application.View```)

---
```python
def getStyleManager(self)
```
  * Get application style manager (type: ```SimpleApp.stylemanager.StyleManager ```)

---
```python
def reloadStyleSheet(self, styles_path)
```
  * Reload stylesheet
  * __Parameters__
    * __styles_path__: Path where is file with styles for all GUI elements  

---
```python
def reloadElementStyles(self)
```
  * Reload style of all elements (from all views of application)

---
```python
def removeView(self, view)
```
  * Remove view from application
  * __Parameters__
    * __view__: View to be removed (type: ```SimpleApp.application.View```)

---
```python
def getScreen(self)
```
  * Get screen of application (type: ```pygame.Surface```)

---
```python
def init(self, width, height, name, icon)
```
  * Init application
  * __Parameters__
    * __width__: Width of application window (type: ```int```)
    * __height__: Height of application window (type: ```int```)
    * __name__: Name of application (window title) (type: ```int```)
    * __icon__: Icon of application (type: ```int```)

---
```python
def run(self)
```
  * Run application loop (Returns False in case of fail) (type: ```boolean```)

---
```python
def close(self)
```
  * Close application

---
```python
def showView(self, view)
```
  * Close application
  * __Parameters__
    * __view__: View to be displayed in application
  * Return True in success (type: ```boolean```)

---
```python
def showViewWithName(self, name)
```
  * Show view with specific name
  * __Parameters__
    * __name__: Name of view (type: ```string```)

---
```python
def showViewWithID(self, id)
```
  * Show view with specif ID
  * __Parameters__
    * __id__: ID of view (type: ```int```)

## View
View represents the content/page of the application window that the user sees and with which he can interact.
```python
def __init__(self, name, id)
```
  * Create instance of Application
  * __Parameters__
    * __name__: Name of view (the name will be visible in the window title) (list element type: ```string```)
    * __id__: ID of view (can be used for navigation) (type: ```int```)

---
```python
def setID(self, id)
```
  * Set view ID
  * __Parameters__
    * __id__: New ID for view (type: ```int```)

---
```python
def addGUIElements(self, elements)
```
  * Add GUI elements to this view
  * __Parameters__
    * __elements__: List with GUI elements (list element type: ```SimpleApp.guielement.GUIElement```)

---
```python
def removeGUIElement(self, element)
```
  * Remove GUI element from view
  * __Parameters__
    * __element__: GUI element to be removed (type: ```SimpleApp.guielement.GUIElement```)

---
```python
@final 
def getApp(self)
```
  * Get reference on app (type: ```SimpleApp.application.Application```)

---
```python
def registerLayoutManager(self, layoutManager)
```
  * Register new layout manager
  * __Parameters__
    * __layoutManager__: New layout manager (type: ```SimpleApp.application.Layout```)

---
```python
def unregisterLayoutManager(self, layoutManager)
```
  * Unregister layout manager
  * __Parameters__
    * __layoutManager__: Layout manager (type: ```SimpleApp.application.Layout```)

---
```python
@final 
def getGUIElement(self)
```
  * Get list of GUIElements (list element type: ```SimpleApp.guielement.GUIElement```)

---
```python
def setDefaultCursor(self, cursor=pygame.SYSTEM_CURSOR_ARROW)
```
  * Set default cursor for view
  * __Parameters__
    * __cursor__: Default cursor (type: ```pygame.cursor constant```)

---
```python
def setFillColor(self, color)
```
  * Set view fill color
  * __Parameters__
    * __color__: View fill color (type: ```tuple```)

---
```python
@final 
def getFillColor(self)
```
  * Get view fill color (type: ```tuple```)

---
```python
def setVisibility(self, visible)
```
  * Set visibility of view
  * __Parameters__
    * __visible__: True=view is visible (type: ```boolean```)

---
```python
def setApplication(self, app)
```
  * Assigns application to this view
  * __Parameters__
    * __app__: Application (type: ```SimpleApp.application.Application```)

---
```python
@final 
def reloadElementStyle(self, list=None)
```
  * Reload style of all GUI elements from list (do not set "list" if you want all view elements)
  * __Parameters__
    * __list__: List with GUI elements (list element type: ```SimpleApp.guielement.GUIElement```)

---
```python
@abc.abstractmethod 
def createEvt(self)
```
  * Create event - when the application starting

---
```python
@abc.abstractmethod 
def closeEvt(self)
```
  * Close event - when the application closing

---
```python
@abc.abstractmethod 
def openEvt(self)
```
  * Open event - when the application show this view

---
```python
@abc.abstractmethod 
def hideEvt(self)
```
  * Hide event - when the application hide this view

---
```python
@abc.abstractmethod 
def reloadStyleEvt(self)
```
  * Reload style event - when the application reloading styles of view

---
```python
@abc.abstractmethod 
def findElement(self, list, procces_function=None)
```
  * Find element in "list of GUI elements" for which procces function return True
  * __Parameters__
    * __list__: List with GUI elements (list element type: ```SimpleApp.guielement.GUIElement```)
    * __procces_function__: True/False function, return first element for which return True

---
```python
@abc.abstractmethod 
def findElement(self, list, procces_function=None)
```
  * Find element in "list of GUI elements" for which procces function return True
  * __Parameters__
    * __list__: List with GUI elements (list element type: ```SimpleApp.guielement.GUIElement```)
    * __procces_function__: True/False function, return first element for which return True

## GUI elements
### Base class
### Label
### Image
### Button
### Canvas
### Checkbox
### Radiobutton
### Slider
### Togglebutton
### Textinput
### Graph
### Vertical scrollbar
### Table
### Panel

### Tab Panel
## Layout managers
### Absolute Layout
### Relative Layout
