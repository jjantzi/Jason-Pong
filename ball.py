from turtle import Turtle, Screen

class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(1,1)
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.movespeed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bouncey(self):
        self.y_move *= -1
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move )    

    def bouncex(self):
        self.x_move *= -1
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move )
        self.movespeed *= 0.9    

    def reset(self): 
        self.movespeed = 0.1
        self.goto(0,0)
        self.bouncex()
        # self.x_move = 10
        # self.y_move = 10     