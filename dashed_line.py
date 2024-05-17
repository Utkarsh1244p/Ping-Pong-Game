from turtle import Turtle

class DashedLine(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.create_dashed_middle_line()

    def create_dashed_middle_line(self):
        self.up()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(20):
            self.down()
            self.forward(20)
            self.up()
            self.forward(10)        