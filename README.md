# SimpleApp framework
## About
...
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
## View

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
