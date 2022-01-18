This repository is intended as a collection of classic arcade games rendered in Python. 
-------------------------------------------------
Invaders

The classic "space invaders" game. You control the spaceship at the bottom with the Left/Right arrow keys and can fire torpedos at the alien attackers with Space (appropriately!). Evade the yellow bombs which the alien ships drop in random intervals. 
The game ends when all alien ships are destroyed (victory for the player), the player runs out of lives (loss for the player), or at least one alien ship "breaks through" to the bottom edge (loss for the player).

To adjust the difficulty, change the following parameters:

MIN_TIME_SINCE_LAST_FIRE (default: 10). This determines how long you have to wait after firing a torpedo before you can fire the next one (the lower the number, the sooner you're ready to fire again --> Makes it easier).

ALIEN_SHIP_MOVE_DISTANCE (default: 2). This determines how fast the alien ships move sideways (the higher the number, the faster the move --> Makes it harder). Since the alien ships move down when they reach an edge, this indirectly also determines how fast they move down towards the player's spaceship.

TORPEDO_MOVE_DISTANCE (default: 30). This determines how fast the torpedos fired by the player move (the higher the number, the faster --> Makes it easier).

ALIEN_BOMB_FALL_DISTANCE (default: 3). This determines how fast the bombs dropped by the player move (the higher the number, the faster --> Makes it harder).

INTERVAL_OF_BOMB_DROPPING (default: 5). This determines the intervals at which, on average (not deterministically), an alien shop will drop a bomb
(the higher the number, the less frequent the bombs --> Makes it easier)

LIVES (default: 3). This determines the number of lives for the player; each hit by an alien bomb costs a life. Note that a "breakthrough" of the alien ships, i.e. when they reach the bottom edge, does not cost a life but rather ends the game (with a loss for the player).

The program imports the files "boom.gif", "spaceship.gif" and "space.gif" for graphics. The first two of these are provided in this repository, I designed them myself. The file "space.gif" isn't provided for copyright reasons (as the file I'm using on my machine was downloaded from the web). Just pick a space-themed image of your likin and save it in the same folder as the .py file, named "space.gif".

Version 1.1, January 2022


-------------------------------------------------
Pong

The classic ping-pong rendition, with two simple but elegant paddles bouncing a ball to each other. All in one file and with on-board Python tools.

To adjust the speed with which the ball flies across the screen, define the "speed" variable; to adjust the number of points needed to win and end the game, adjust the "ending_score" variable. Both are defined at the outset of the file.

The code is based on practice assignments from Angela Yu's (highly recommendable!) online Python course "100 Days of Code", but has numerous deviations and modifications compared to the code presented by Angela as a solution to the assignments. I leave it to you to decide whether they constitute an improvement.

Version 1.0, April 2021
