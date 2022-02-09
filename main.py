import random
from SimpleApp import *
from SimpleApp.gui import vertical_scroll

# style
style = {
    "f_color":      WHITE,
    "b_color":      GRAY,
    "font_name":    "Verdena",
    "font_size":    32,
    "font_bold":    False,
    "size": 25
}

# table style
h_style = {
    "f_color":      WHITE,
    "b_color":      BLACK,
    "font_name":    "Verdena",
    "font_size":    32,
    "font_bold":    True
}
b_style = {
    "f_color":      BLACK,
    "b_color":      WHITE,
    "s_color":      GRAY,
    "font_name":    "Verdena",
    "font_size":    22,
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
        rl = RelativeLayout(self)
        # label
        label = Label(self, style, "RED VIEW", True)
        rl.addElement(label, ['50%', '5%'])

        # canvas
        canvas = Canvas(self, style)
        rl.addElement(canvas, ['3%', '15%', '45%', '40%'])
        canvas.setPaintEvt(self.paint)

        # table
        data = {
            "header": ["Col 1", "Col 2", "Col 3", "Col 4"],
            "body": [
                ["A1", "B1", "C1", "D1"],
                ["A2", "B2", "C2", "D2"],
                ["A3", "B3", "C3", "D3"],
                ["A4", "B4", "C4", "D4"],
                ["A1", "B1", "C1", "D1"],
                ["A2", "B2", "C2", "D2"],
                ["A3", "B3", "C3", "D3"],
                ["A4", "B4", "C4", "D4"],
                ["A1", "B1", "C1", "D1"],
                ["A2", "B2", "C2", "D2"],
                ["A3", "B3", "C3", "D3"],
                ["A4", "B4", "C4", "D4"]
            ]
        }
        table = Table(self, h_style, b_style, data)
        rl.addElement(table, ['52%', '15%', '45%', '40%'])

        # btn
        btn = Button(self, style, "Go to green")
        rl.addElement(btn, ['25%', '60%', '50%', '40'])
        btn.setClickEvt(lambda btn: self.app.showViewWithID(GREEN_VIEW_ID))

        # checkbox
        checkbox1 = CheckBox(self, style, "Check box 1", True)
        rl.addElement(checkbox1, ['20%', '75%'])
        checkbox2 = CheckBox(self, style, "Check box 2", True)
        rl.addElement(checkbox2, ['55%', '75%'])

        self.addGUIElements([btn, canvas, table, label, checkbox1, checkbox2])

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
        rl = RelativeLayout(self)

        # button
        btn = Button(self, style, "Go to red")
        rl.addElement(btn, ['25%', '85%', '50%', '40'])
        btn.setClickEvt(lambda btn: self.app.showViewWithID(RED_VIEW_ID))

        # text input
        txt = TextInput(self, style, "Text")
        rl.addElement(txt, ['25%', '5%', '50%', '40'])

        # combo box
        group = RadioButtonGroup([])
        combobox1 = RadioButton(self, style, "Option 1", group)
        rl.addElement(combobox1, ['20%', '20%'])
        combobox2 = RadioButton(self, style, "Option 2", group)
        rl.addElement(combobox2, ['40%', '20%'])
        combobox3 = RadioButton(self, style, "Option 3", group)
        rl.addElement(combobox3, ['60%', '20%'])

        # image
        img = Image(self, "src/img1.jpg")
        rl.addElement(img, ['10%', '30%', '200', '200'])

        # graph
        data = buildGraphData([
            [1, 2, 4, 6],
            [3, 3, 4, 3],
            [6, 6, 5, 4]
        ])
        graph = Graph(self, data, 0, 0, 300, 240)
        rl.addElement(graph, ['40%', '23%'])

        self.addGUIElements(
            [btn, txt, combobox1, combobox2, combobox3, img, graph])

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
