from turtle import Turtle, Screen
import time, random

MIN_TIME_SINCE_LAST_FIRE = 10
ALIEN_SHIP_MOVE_DISTANCE = 2
TORPEDO_MOVE_DISTANCE = 30
ALIEN_BOMB_FALL_DISTANCE = 3
LIVES = 3
startingsetup = [-300, -200, -100, 0, 100, 200, 300]

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.bgpic("space.gif")
screen.listen()
screen.tracer()
alienship = "alienship.gif"
screen.addshape(alienship)
fighter = "spaceship.gif"
screen.addshape(fighter)
boom = "boom.gif"
screen.addshape(boom)
breakthrough = False



list_of_alien_ships = []
list_of_spaceships = []
list_of_alien_bombs = []
list_of_torpedos = []
game_on = True
time_since_last_fire = 11
cyclenumber = 0

class Spaceship(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape(fighter)
        self.shapesize(1, 1)
        self.penup()
        self.setposition(0, -300)
        self.showturtle()
        self.target_y = -274
        self.target_x_min = - 18
        self.target_x_max = + 18
        
    def goleft(self):
        self.setx(self.xcor()-10)
        self.target_x_min = self.xcor() - 18
        self.target_x_max = self.xcor() + 18
        
    def goright(self):
        self.setx(self.xcor()+10)
        self.target_x_min = self.xcor() - 18
        self.target_x_max = self.xcor() + 18
        
    def fire(self):
        global time_since_last_fire
        if time_since_last_fire >= MIN_TIME_SINCE_LAST_FIRE:
            new_torpedo = Torpedo(self.xcor(), self.ycor())
            list_of_torpedos.append(new_torpedo)
            time_since_last_fire = 0
        else:
            pass
        
    def routine_after_hit(self):
        time.sleep(1)
        self.hideturtle()
        self.shape(fighter)
        self.setposition(0, -300)
        self.showturtle()
        
class Torpedo(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color("deep sky blue")
        self.shapesize(0.1, 2)
        self.penup()
        self.setposition(x, y+20)
        self.setheading(90)
        self.showturtle()
        self.x = self.xcor()
        self.y_of_tip = y+40
        
    def move(self):
        self.forward(TORPEDO_MOVE_DISTANCE)
        if self.ycor() > 500:
            list_of_torpedos.remove(self)
        self.y_of_tip = self.ycor() + 20
            
    def detecthit(self):
        for alien_ship in list_of_alien_ships:
            if self.x > alien_ship.target_x_min and self.x < alien_ship.target_x_max and abs(self.y_of_tip - alien_ship.target_y) < 10:
                alien_ship.transformtoboom()
                self.hideturtle()
                list_of_torpedos.remove(self)

class Alien_Ship(Turtle):
    
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape(alienship)
        self.shapesize(1, 1)
        self.penup()
        self.setposition(x, y)
        self.showturtle()
        
    def move(self):
        
        ship.setx(ship.xcor() + ALIEN_SHIP_MOVE_DISTANCE)
        self.target_x_min = self.xcor() - 35
        self.target_x_max = self.xcor() + 35
        self.target_y = self.ycor() + 11
        
    def godown(self):
        self.sety(self.ycor() - 30)
        
    def transformtoboom(self):
        self.shape(boom)
        if len(list_of_alien_ships) == 0:
            game_on = False
        
        
    def linebreakdetector_left(self):
        global ALIEN_SHIP_MOVE_DISTANCE 
        if self.xcor() <= -374 and ALIEN_SHIP_MOVE_DISTANCE < 0:
            for ship in list_of_alien_ships:
                ship.godown()
            ALIEN_SHIP_MOVE_DISTANCE *= (-1)
            
    def linebreakdetector_right(self):
        global ALIEN_SHIP_MOVE_DISTANCE 
        if self.xcor() >= 374 and ALIEN_SHIP_MOVE_DISTANCE > 0:
            for ship in list_of_alien_ships:
                ship.godown()
            ALIEN_SHIP_MOVE_DISTANCE *= (-1)
        
            
    def randombombgenerator(self):
        
        # Drops at random a new bomb from an alien ship; on average one
        # bomb every 10 seconds per ship
        
        if random.randint(0,5) == 5:
            new_bomb = Alienbombs(self.xcor(), self.ycor())
            list_of_alien_bombs.append(new_bomb)
            
            
class Alienbombs(Turtle):
    
    def __init__(self, x, y):
        
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color("yellow")
        self.shapesize(0.4, 0.4)
        self.penup()
        self.setposition(x, y)
        list_of_alien_bombs.append(self)
        self.setheading(270)
        self.showturtle()
        
    def falls(self):
        self.forward(ALIEN_BOMB_FALL_DISTANCE)
        if self.ycor() < -500:
            list_of_alien_bombs.remove(self)
            
    def detect_hit_with_player(self):
        if self.xcor() > spaceship.target_x_min and self.xcor() < spaceship.target_x_max and abs(self.ycor() - spaceship.target_y) < 10:
            global list_of_alien_bombs
            list_of_alien_bombs.remove(self)
            self.hideturtle()
            self.sety(100)
            spaceship.shape(boom)
            whathappensifheshit()
                
class Livewriter(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300, -350)
        self.update()
        
    def update(self):
        self.clear()
        self.color("white")
        self.write(f"Lives: {LIVES}", font = ("Arial", "14", "bold"))
        
def whathappensifheshit():
    global LIVES
    LIVES -= 1
    livewriter.update()
    if LIVES > 0:
        spaceship.routine_after_hit()
        time.sleep(1)
    else:
        global game_on
        game_on = False
    
        
#Generates initial set-up of alien fleet

for i in startingsetup:
    new_ship = Alien_Ship(i, 350)
    new_ship.showturtle()
    list_of_alien_ships.append(new_ship)
    
spaceship = Spaceship()
list_of_spaceships.append(spaceship)
livewriter = Livewriter()

            
while game_on:
    #Makes alien bombs fall and alien ships move and drop new bombs at random
        
    if cyclenumber == 25:
        cyclenumber = 0
    for alienbomb in list_of_alien_bombs:
        alienbomb.falls()
    for ship in list_of_alien_ships:
        ship.move()
            
    if cyclenumber == 0:
        for ship in list_of_alien_ships:
            ship.randombombgenerator()

            
    #Makes player torpedoes move and detect hits with alien ships
    for torpedo in list_of_torpedos:
        torpedo.move()
        torpedo.detecthit()
            
    for alien_bomb in list_of_alien_bombs:
        alien_bomb.detect_hit_with_player()
            
    #Ends the game when all alien ships are destroyed
    if len(list_of_alien_ships) == 0:
        break
        
    #Line break when alien ships reach left or right edge of screen
    if cyclenumber == 16:
        list_of_alien_ships[0].linebreakdetector_left()
        list_of_alien_ships[-1].linebreakdetector_right()
        
    #Listen to payer commands, perform screen updates 
    screen.onkey(spaceship.goleft, "Left")
    screen.onkey(spaceship.goright, "Right")
    screen.onkey(spaceship.fire, "space")
    time.sleep(0.04)
    screen.update()
        
    #Removes alien ships once they have been hit by a torpedo

    for item in list_of_alien_ships:
        if item.shape() == boom:
            item.hideturtle()
            list_of_alien_ships.remove(item)
    
    if len(list_of_alien_ships) == 0:
        break
    
    if list_of_alien_ships[0].ycor() < -290:
        game_on = False
        breakthrough = True
        
        
    cyclenumber += 1
    time_since_last_fire += 1

#End-of-game message
if len(list_of_alien_ships) == 0:
    message = "You win!"
if lives == 0:
    message = "Game over"
if breakthrough:
    message = "Game over"
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.color("white")
writer.goto(-40, 0)
writer.write(message, font=("Arial", 24, "normal"))

screen.mainloop()
