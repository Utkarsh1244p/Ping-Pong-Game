from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed(0)
        self.up()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid= 4, stretch_len= 0.7)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 240:
            self.new_y = self.ycor() + 20
            self.goto(self.xcor(), self.new_y)

    def move_down(self):
        if self.ycor() > -240:
            self.new_y = self.ycor() - 20
            self.goto(self.xcor(), self.new_y)

