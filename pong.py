from turtle import Turtle, Screen
import time
speed = 12 #The higher this number, the faster the ball will move
ending_score = 3 #The number of points needed to win and end the game

class Ball(Turtle):
    
    #Defines the Ball class with its methods: 

    
    def __init__(self):
        
        """Initialisation of the ball"""
        
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xcorchanger = speed
        self.ycorchanger = speed
        
    def fly(self):
        
        """Regular movement of the ball across the screen"""
        
        old_x = self.xcor()
        old_y = self.ycor()
        self.goto(old_x + self.xcorchanger, old_y + self.ycorchanger)

    def wallbounce(self):
        
        """Bounce of the ball when hitting the upper and lower walls"""

        self.ycorchanger = self.ycorchanger*(-1)
        
    def paddlebounce(self):
        
        """Bounce of the ball when hitting a paddle"""
        
        self.xcorchanger = self.xcorchanger*(-1)
        
    def ball_reset_after_score(self):
        
        """Initialises a new ball after one player scores"""
        
        self.hideturtle()
        self.goto(0, 0)
        self.ycorchanger = speed
        self.showturtle()
        
    def leftplayerscores(self):
        
        """Ensures that after the left player scores, a new ball 
        is served"""
        
        self.xcorchanger = speed*(-1)
        self.ball_reset_after_score()
        
    def rightplayerscores(self):
        
        """Ensures that after the right player scores, a new ball 
        is served"""
        
        self.xcorchanger = speed
        self.ball_reset_after_score()


class Paddle(Turtle):
    
    # Defines the Paddle class with its methods
	
    def __init__(self, x_cor, y_cor):
        
        """Initialises a paddle"""
		
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.speed("fastest")
        self.setx(x_cor)
        self.sety(y_cor)
        self.showturtle()
		
    def paddle_up(self):
        """Moves the paddle upwards"""
        self.sety(self.ycor() + 20)
		
    def paddle_down(self):
        """Moves the paddle downwards"""
        self.sety(self.ycor() - 20)
        
class Scoring(Turtle):

    #The scoring system with its methods
    
    def __init__(self):
        
        """Initialises a scoreboard"""
        
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.writescore()
        
    def writescore(self):

        """Writes the score on the screen"""
        
        self.clear()
        self.goto(-100, 250)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 250)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def leftscores(self):
        
        """Updates the score when the left player scores"""
        
        self.l_score += 1
        self.writescore()
        
    def rightscores(self):
        
        """Updates the score when the right player scores"""
        
        self.r_score += 1
        self.writescore()

##Main program starts here

#Sets up the game screen
screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
gameplay = True

#Initialises a ball and two paddles, one for each player
rightpaddle = Paddle(350, 0)
leftpaddle = Paddle(-350, 0)
ball = Ball()

#Initialises the scoring system
scoring = Scoring()

#Defines the commands used to control the paddles
screen.onkey(rightpaddle.paddle_up, "Up")
screen.onkey(rightpaddle.paddle_down, "Down")
screen.onkey(leftpaddle.paddle_up, "w")
screen.onkey(leftpaddle.paddle_down, "s")


#The actual gameplay

while gameplay == True:
    ball.fly() #Keeps the ball moving while ball is live
    #One screen update every 0.04 seconds, to keep movements smooth
    time.sleep(0.04)
    screen.update()
     
    #Ensures that the ball bounces when hitting upper or lower wall
    if ball.ycor() >= 390 or ball.ycor() <= -390:
        ball.wallbounce()
    
    #Ensures that the ball bounces when hitting a paddle
    if ball.distance(rightpaddle) <= 50 and ball.xcor() >= 320 and ball.xcorchanger > 0:
        ball.paddlebounce()
    if ball.distance(leftpaddle) <= 50 and ball.xcor() <= -320 and ball.xcorchanger < 0:
        ball.paddlebounce()
        
    #Detects a missed ball, which is a point for the opposing player
    if ball.xcor() > 400:
        ball.leftplayerscores()
        scoring.leftscores()
    if ball.xcor() < -400:
        ball.rightplayerscores()
        scoring.rightscores()
    
    #Ends the game after one player scores predefined number of points
    if scoring.l_score == ending_score or scoring.r_score == ending_score:
        gameplay = False

screen.exitonclick()
