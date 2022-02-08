import random

import SimpleApp
from SimpleApp.colors import *
from SimpleApp.application import *
from SimpleApp.gui import *


# button and canvas style
style = {
    "f_color":      WHITE,
    "b_color":      GRAY,
    "font_name":    "Verdena",
    "font_size":    32,
    "font_bold":    False
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
        canvas = Canvas(self, 50, 150, 300, 200, style)
        canvas.setPaintEvt(self.paint)

        self.addGUIElements([btn, canvas])

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
        #button
        btn = Button(self, 50, 50, 160, 50, style, "Go to red")
        btn.setClickEvt(lambda btn: self.app.showViewWithID(RED_VIEW_ID))
        #text input
        txt = TextInput(self, 50, 150, 250, 50, style, "Text")
        self.addGUIElements([btn, txt])

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
    app.showView(view2)
    app.run()


if __name__ == "__main__":
    main()
