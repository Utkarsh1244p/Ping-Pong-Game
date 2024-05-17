from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.color("white")
        self.speed(0)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align= "center", font= ("Courier", 60, "normal") )
        self.goto(100, 200)
        self.write(f"{self.r_score}", align= "center", font= ("Courier", 60, "normal") )


    # def update_l_score(self):
    #     self.goto(-100, 200)
    #     self.clear()
    #     self.write(f"{self.l_score}", align= "center", font= ("Courier", 60, "normal") )

    # def update_r_score(self):
    #     self.goto(100, 200)
    #     self.clear()
    #     self.write(f"{self.r_score}", align= "center", font= ("Courier", 60, "normal") )