# Pong Arcade game written by Jason Jantzi

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor('black')
screen.title('Jason Pong')
screen.setup(width=800,height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0,0))
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
     time.sleep(ball.movespeed)
     screen.update()
     ball.move()

     # detect collison with the wall.
     if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()

    # detect collision with r_paddle
     if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        print ("right contact")
        
        ball.bouncex()

    # detect collision with l_paddle
     if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        print ("left contact")
        
        ball.bouncex()



    # detect when right paddle misses
     if ball.xcor() > 380:
         print ("left wins")
         scoreboard.rscore()
         ball.reset()

    # detect when left paddle misses   
     if ball.xcor() < -380:
         print ("right wins")
         scoreboard.lscore()
         ball.reset()     

screen.exitonclick()





