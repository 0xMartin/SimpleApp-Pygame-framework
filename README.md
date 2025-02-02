# Pygame UI Lib
## About
This is simple UI library based on Pygame. It allows you to divide your game/application to more views and yous GUI elemnets (form controls). In views you can use defined GUI elements (like: TextInput, Button, CheckBox, Label, ...). You can simply implement your own view with GUI elements that you want to use. Also is there posibility of customizing elements or create new one. Each element has it own style and you can modifi it in code or in config of library where are stylesheets for all elements. Almost everything is stylizable and can by stored to .json stylesheet file and loaded using style manager.
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
Implement your own view:
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
        # assigns button to layout manager and set properties
        # [x_position, y_position, width, height]
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
In entry point of program create instance of Application, add your view, show some view and run app. For more detail usage of framework check main.py.
```python
view1 = View1()
view2 = View2()
app = Application([view1, view2], 30, 1, True)
app.init(640, 400, "Application", "")
app.showView(view1)
app.run()
```
&nbsp;
&nbsp;

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

&nbsp;
&nbsp;
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

&nbsp;
&nbsp;
## Style Manager
Provides style for each GUI element. Loading and preserves all application styles.

---
```python
def __init__(self, styles_path)
```
  * Create style manager
  * __Parameters__
    * __styles_path__: Path where is file with styles for all guil elements (type: ```string```)

---
```python
def init(self)
```
  * Init style manager

---
```python
def loadStyleSheet(self, styles_path)
```
  * Load stylesheet from file
  * __Parameters__
    * __styles_path__: Path where is file with styles for all guil elements (type: ```string```)

---
```python
def getStyleWithName(self, name)
```
  * Get style with specific name from stylsheet
  * __Parameters__
    * __name__: Name of style (type: ```string```)

---
```python
def getStyleWithName(self, name)
```
  * Get style with specific name from stylsheet
  * __Parameters__
    * __name__: Name of style (type: ```string```)

---
```python
def processStyle(self, name)
```
  * Some string values are replaced by an object if necessary
  * __Parameters__
    * __style__: Some style (type: ```dict```)


&nbsp;
&nbsp;
## GUI elements
### Base class
Base class for GUI elements

---
```python
def __init__(self, view, x, y, width, height, style, selected_cursor=pygame.SYSTEM_CURSOR_HAND)
```
  * Create GUIElement
  * __Parameters__
    * __x__: X position of Element (type: ```int```)
    * __y__: Y position of Element (type: ```int```)
    * __width__: Width position of Element (type: ```int```)
    * __height__: Height position of Element (type: ```int```)
    * __style__: Style of Element (type: ```dict```)
    * __selected_cursor__: The type of cursor that appears when this element is selected

---
```python
def setVisibility(self, visible)
```
  * Set visibility of element
  * __Parameters__
    * __visible__: True/False (type: ```boolean```)

---
```python
def isVisible(self)
```
  * Check if element is visible (type: ```boolean```)

---
```python
def setSelectCursor(self, cursor)
```
  * Set cursor type when this element is selected
  * __Parameters__
    * __cursor__: Type of cursor that appears when this element is selected (type: ```pygame cursor constant```)

---
```python
@final
def getSelectCursor(self)
```
  * Return cursor type when this element is selected (type: ```pygame cursor constant```)

---
```python
@final
def getView(self)
```
  * Get view to which the element belongs

---
```python
@final
def getX(self)
```
  * Get x position of this element (type: ```int```)

---
```python
@final
def getY(self)
```
  * Get y position of this element (type: ```int```)

---
```python
@final
def getWidth(self)
```
  * Get width of this element (type: ```int```)

---
```python
@final
def getHeight(self)
```
  * Get height of this element (type: ```int```)

---
```python
@final
def getStyle(self)
```
  * Get style of this element (type: ```dict```)

---
```python
def setX(self, x)
```
  * Set x position of this element
  * __Parameters__
    * __x__: New X position

---
```python
def setY(self, y)
```
  * Set y position of this element
  * __Parameters__
    * __y__: New Y position

---
```python
def setWidth(self, width)
```
  * Set width of this element
  * __Parameters__
    * __width__: New width of element

---
```python
def setHeight(self, height)
```
  * Set height of this element
  * __Parameters__
    * __height__: New height of element

---
```python
def setStyle(self, style)
```
  * Set style of this element
  * __Parameters__
    * __style__: New style of element

---
```python
def updateViewRect(self)
```
  * Update view rect of this element

---
```python
@final
def getViewRect(self)
```
  * Get view rect of this element (type: ```pygame.Rect```)

---
```python
@final
def select(self)
```
  * Select this element

---
```python
@final
def unSelect(self)
```
  * Unselect this element

---
```python
@final
def isSelected(self)
```
  * Check if element is selected (type: ```boolean```)

---
```python
@abc.abstractmethod
def draw(self, view, screen)
```
  * Draw element on screen
  * __Parameters__
    * __view__: View which is rendering this element
    * __scree__: Screen where element is rendered 

---
```python
@abc.abstractmethod
def processEvent(self, view, event)
```
  * Process event from view
  * __Parameters__
    * __view__: View which is sending event
    * __event__: Pygame event

---
```python
@abc.abstractmethod
def update(self, view)
```
  * Update element
  * __Parameters__
    * __view__: View which is updating this element


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

&nbsp;
&nbsp;
## Layout managers
### Base class
Base layout class mainly consists from list of layout elements and an abstract ```updateLayout``` function. The layout element consists of a reference to the GUI element and properies for a specific layout manager.
* __Layout element structure:__ ```{"element": value1, "propt": value2}```

---
```python
def __init__(self, view, register=True)
```
  * Base layout class, automatically register layout manager to view
  * __Parameters__
    * __screen__: Pygame surface
    * __view__: View for which the layout manager will register
    * __register__: False: disable registration of this layout manager

---
```python
@final
def getLayoutElements(self)
```
  * Return all elements from layout

---
```python
def setElements(self, layoutElements)
```
  * Set new layout element list
  * __Parameters__
    * __layoutElements__: Layout element list

---
```python
def addElement(self, element, propt=None)
```
  * Add new layout element to layout manager
  * __Parameters__
    * __element__: GUIElement (type: ```SimpleApp.guielement.GUIElement```)
    * __propt__: Property of element for layout manager (LEFT, RIGHT, CENTER, ...) values denpends on manager

---
```python
@abc.abstractmethod
def updateLayout(self, width, height)
```
  * Update layout of all GUI elements
  * __Parameters__
    * __width__: Width of view screen   (type: ```int```)
    * __height__: Height of view screen   (type: ```int```)

### Absolute Layout
It is possible to set absolute position or size of each GUI element. Values can be set in % or px. If the value is set in %, it is then recalculated to px (in overrided method ```Layout.updateLayout```). So it is possible to set the element to be constantly in a certain position or to have a certain size.

---
```python
def __init__(self, view)
```
  * Create Absolute Layout, addElement(el, propt) -> propt : {x, y, width, height} (x, y, ...) value type: number in px ('50', '4', ...) or % ('20%', '5%', ...)
  * __Parameters__
    * __view__: View for which the layout manager will register

__Examples:__

Position only:
```python
al = AbsoluteLayout(self)
label = Label(self, None, "Label 1", True)
# set position of labe on 50% in X axis of view screen
# and 5% in Y axis of view screen
al.addElement(label, ['50%', '5%'])
```
All attributes:
```python
canvas = Canvas(self, None)
# set positon on [3%, 15%] and width on 45% and height on 40% of view screen size
al.addElement(canvas, ['3%', '15%', '45%', '40%'])
```
Pixel value:
```python
btn = Button(self, custom_btn_style, "Go to view 2")
# height of button set on 40px
al.addElement(btn, ['25%', '60%', '50%', '40'])
```

### Relative Layout
For this layout manager are there two types of elements (parent and child). The layout manager does not affect the element that is defined as the "parent". All elements defined as "child" start stacking behind the parent element in a defined axis (horizontal or vertical).

---
```python
def __init__(self, view, horizontal)
```
  * Create Relative Layout, addElement(el, propt) -> "parent" (his position does not change), "child" (his position depends on the parent)
  * __Parameters__
    * __view__: View for which the layout manager will register
    * __horizontal__: True=elements will stacking in horizontal axis 

__Examples:__
```python
al = AbsoluteLayout(self)
rl = RelativeLayout(self, True)
checkbox1 = CheckBox(self, None, "Check box 1", True, 20)
# absolut layout can set positon of parent 
# (this work only if instance of AbsoluteLayout is created before RelativeLayout!!!!!!)
al.addElement(checkbox1, ['10%', '75%'])
# checkbox1 defined as parent
rl.addElement(checkbox1, "parent")
checkbox2 = CheckBox(self, None, "Check box 2", True, 20)
rl.addElement(checkbox2, "child")
checkbox3 = CheckBox(self, None, "Check box 3", True, 20)
rl.addElement(checkbox3, "child")
```
