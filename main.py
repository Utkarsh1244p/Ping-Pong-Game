import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from dashed_line import DashedLine
import time


#Code for Window
screen = t.Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)


#Code for all objects created from respective classe
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Score()
middle_dashed_line = DashedLine()


#Key Binders Code
# screen.listen()
# screen.onkey(r_paddle.move_up, "Up")
# screen.onkey(r_paddle.move_down, "Down")
# screen.onkey(l_paddle.move_up, "w")
# screen.onkey(l_paddle.move_down, "s")


# Key Binders Code
screen.listen()
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")


#Loop for continuous movement of ball
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    score.update_scoreboard()


    # Checking collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    
    #Checking collision with paddle
    if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -350 and ball.distance(l_paddle) < 50):
        ball.bounce_x()


    #Checking that paddle missed ball 
    if ball.xcor() > 400:
        ball.reset_position()
        score.increase_l_score()

    if ball.xcor() < -400:
        ball.reset_position()
        score.increase_r_score()

 

screen.exitonclick()