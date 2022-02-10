import random
from SimpleApp import *


VIEW1_ID = 1
VIEW2_ID = 2

custom_btn_style = {
    "foreground_color": (255, 255, 255),
    "background_color": (255, 120, 120),
    "font_name": "Verdena",
    "font_size": 32,
    "font_bold": False
}


class View1(View):
    def __init__(self):
        super().__init__("Red", VIEW1_ID)

    def createEvt(self):
        al = AbsoluteLayout(self)
        # label
        label = Label(self, None, "VIEW 1", True)
        al.addElement(label, ['50%', '5%'])

        # canvas
        canvas = Canvas(self, None)
        al.addElement(canvas, ['3%', '15%', '45%', '40%'])
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
        table = Table(self, None, data)
        al.addElement(table, ['52%', '15%', '45%', '40%'])

        # btn
        btn = Button(self, custom_btn_style, "Go to green")
        al.addElement(btn, ['25%', '60%', '50%', '40'])
        btn.setClickEvt(lambda btn: self.app.showViewWithID(VIEW2_ID))

        # checkbox
        checkbox1 = CheckBox(self, None, "Check box 1", True, 20)
        al.addElement(checkbox1, ['20%', '75%'])
        checkbox2 = CheckBox(self, None, "Check box 2", True, 20)
        al.addElement(checkbox2, ['55%', '75%'])

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


class View2(View):
    def __init__(self):
        super().__init__("Green", VIEW2_ID)

    def createEvt(self):
        al = AbsoluteLayout(self)

        # button
        btn = Button(self, None, "Go to red")
        al.addElement(btn, ['25%', '85%', '50%', '40'])
        btn.setClickEvt(lambda btn: self.app.showViewWithID(VIEW1_ID))

        # text input
        txt = TextInput(self, None, "A1B2")
        txt.setFilterPattern("^([A-Z][0-9]+)+$")
        al.addElement(txt, ['25%', '5%', '50%', '40'])

        # combo box
        group = RadioButtonGroup([])
        combobox1 = RadioButton(self, None, "Option 1", group, 20)
        al.addElement(combobox1, ['20%', '20%'])
        combobox2 = RadioButton(self, None, "Option 2", group, 20)
        al.addElement(combobox2, ['40%', '20%'])
        combobox3 = RadioButton(self, None, "Option 3", group, 20)
        al.addElement(combobox3, ['60%', '20%'])

        # image
        img = Image(self, "src/img1.jpg")
        al.addElement(img, ['10%', '30%', '200', '200'])

        # graph
        data = buildGraphData([
            [1, 2, 4, 6],
            [3, 3, 4, 3],
            [6, 6, 5, 4]
        ])
        graph = Graph(self, data)
        al.addElement(graph, ['40%', '23%', '300', '240'])

        self.addGUIElements(
            [btn, txt, combobox1, combobox2, combobox3, img, graph])

    def closeEvt(self):
        pass

    def openEvt(self):
        pass

    def hideEvt(self):
        pass


def main():
    view1 = View1()
    view2 = View2()
    app = Application([view1, view2], 30, 30)
    app.init(640, 400, "Application", "")
    app.showView(view1)
    app.run()


if __name__ == "__main__":
    main()
