import random
from tkinter import Label

from SimpleApp import *

# style
style = {
    "f_color":      WHITE,
    "b_color":      GRAY,
    "font_name":    "Verdena",
    "font_size":    32,
    "font_bold":    False,
    "size": 25
}

RED_VIEW_ID = 1
GREEN_VIEW_ID = 2

# red view


class RedView(View):
    def __init__(self):
        super().__init__("Red", RED_VIEW_ID)
        super().setFillColor(RED)

    def createEvt(self):
        # btn
        btn = Button(self, 50, 50, 160, 50, style, "Go to green")
        btn.setClickEvt(lambda btn: self.app.showViewWithID(GREEN_VIEW_ID))
        # canvas
        canvas = Canvas(self, 50, 150, 410, 200, style)
        canvas.setPaintEvt(self.paint)
        # label
        label = Label(self, 300, 50, style, "LABEL 1")
        # checkbox
        checkbox1 = CheckBox(self, 300, 80, style, "Check box 1", True)
        checkbox2 = CheckBox(self, 300, 110, style, "Check box 2", True)

        self.addGUIElements([btn, canvas, label, checkbox1, checkbox2])

    def closeEvt(self):
        pass

    def openEvt(self):
        pass

    def hideEvt(self):
        pass

    def paint(self, surface):
        for i in range(1, 100):
            pygame.draw.rect(
                surface,
                (random.randint(0, 255), random.randint(
                    0, 255), random.randint(0, 255)),
                pygame.Rect(
                    random.randint(-50, surface.get_width() - 50),
                    random.randint(-50, surface.get_height() - 50),
                    random.randint(40, 100),
                    random.randint(40, 100)
                ),
                2
            )

# green view


class GreenView(View):
    def __init__(self):
        super().__init__("Green", GREEN_VIEW_ID)
        super().setFillColor(GREEN)

    def createEvt(self):
        # button
        btn = Button(self, 50, 50, 160, 50, style, "Go to red")
        btn.setClickEvt(lambda btn: self.app.showViewWithID(RED_VIEW_ID))
        # text input
        txt = TextInput(self, 50, 150, 250, 50, style, "Text")

        #combo box
        group = RadioButtonGroup([])
        combobox1 = RadioButton(self, 300, 50, style, "Option 1", group)
        combobox2 = RadioButton(self, 300, 80, style, "Option 2", group)
        combobox3 = RadioButton(self, 300, 110, style, "Option 3", group)

        self.addGUIElements([btn, txt, combobox1, combobox2, combobox3])

    def closeEvt(self):
        pass

    def openEvt(self):
        pass

    def hideEvt(self):
        pass


def main():
    view1 = RedView()
    view2 = GreenView()
    app = Application([view1, view2], 60)
    app.init(640, 400, "Application", "")
    app.showView(view1)
    app.run()


if __name__ == "__main__":
    main()
