# TAPPING WITH THE TERRAPINS
#### Video Demo:  <https://youtu.be/lnPHP-HU-j0>
#### Description:

# What my project is
The project that I've coded is "Tapping with the Terrapins" which is my take on crossy road if you doused it in competition with a friend and a whole lot of visual stimulation/chaos. Why the name? Because you have to do a whole lot of keyboard mashing to win, you'll understand when you play it. And the inspiration behind it was me browsing through the final projects gallery and I saw a lot of snake games so I wanted to do something similar with games I played in the past but put my own spin on them.

# What each of the files I wrote for the project contains and does
I organised my files such that each component of the game has its class instantiated in its own file to keep the main project.py file as clean and concise as possible but I had trouble working around passing the return values of things like awarding players points once they hit a certain boundary or the interactions of collisions between players or player and object so I just found it easier for me to do that inside of the main project.py file.

## Car_manager.py
The car_manager.py file hosts the methods of creating cars and moving them. I wanted the cars to be constantly spawning with all different sorts of random attributes like speed, length, colour so that's why there's baked in random module functions inside of the class. The rest is mostly just standard settings like setheading(180) so that the cars will face and move from right to left. I also set the random spawn rate so that the frequency of which the cars are spawned can be controlled by the user so higher randint() upper boundary if you want less cars and a lower one if you want more.

## Scoreboard.py
The scoreboard.py file holds the ability for me to write text using the turtle.write() function and is mainly used to help me keep track of the score and to define methods of when to add or deduct points from the players which are called upon by the conditions in project.py. Ideally I would've settled all of the scoring rules and conditions here but once again I found it difficult to constantly need the cordinates of the players from other files interacting with this file in order to have the points added/deducted. It also has a method of stopping the game once one of the players hits 5 points and declares the winning player on the screen.

## Player.py
The player.py file has the Player class whereby I just set a lot of default turtle module settings. It also contains all of the player movement methods which consist of front, left and right. Initially I wanted to have the turtles visibly turn by using the turtle.setheading() function but found it hard for them to turn any other direction after that so I just stayed with them always facing the opposing side for simplicity sake. And if the players were to try and escape the playing zone or move out of bounds, the "if" conditions for the x boundaries reset them to their original state.

Project.py is where everything comes together from all the other modules. I split them up into 1 main() function and 3 other functions that capture each state of the game.

## Setup()
The first of which being setup() which sets the global scope for the variables of screen, car_manager, scoreboards and players since they will be accessed throughout the entirety of the functions and I don't think it's even possible for me to use return since my game will just end because it's a loop so this is the work around for that. Setup() contains the instantiation of all the components of the game I need and also holds the movement keys which are done using the onkeypress() and onkeyrelease() from the turtle/screen module so player 1 will play using the arrow keys while player 2 uses WASD minus the S since there's no going backwards. And screen.listen() is required there so as to track what key the player is pressing.

## Game_loop()
The second is game_loop() which holds what happens while the game is being played. When the game is started, the cars are slowly generated and start moving from the left to the right of the screen. Once again, this part of my code contains alot of the game rules and collision interactions which then call upon the methods from their respective objects/classes and they will do things like reset players when they hit certain x and y boundaries or award/deduct points when need be. It also keeps track of the scores of the two players and calls upon the display_winner() from the scoreboard class.

## Game_end()
Lastly, game_end() which is activated once a player hits 5 points and the game ends and game_is_on is set to false which is required because screen.exitonclick() needs a condition to be met in order to be "activated". I tried setting it in my loop at first because I could never exit when I clicked on the GUI but it just never worked and it's apparently because from what I understand, it's like using return in a loop so it goes through one time and then it just stops so my programme just breaks.

## Test_project.py
It was only after I finished my project that I realised I had a big problem when it came to my testing file because in the past, all of the tests that I did or was familiar with were functions that returned values or raised errors, those I knew how to do the assertion and all but it was a different case for this project. Because my game doesn't use any return values so I was quite stumped for abit on how to go about the tests but after doing some research I came across a way to test code that didn't end with returning values which was by using pytest-mock which creates a mock of the screen. From what I understand, it basically creates a fake sort of window of the GUI programme and interacts and checks whether the functions/calls that were made are actually doing what they are intended to. So mock.patch() creates a simulation of what is supposed to happen when setup() is called and then I use the assert() to check that the screen and players actually exist.

For test_game_loop, I'm doing the same by creating mocks of the components of the game to check against. And the difference between using mocker.patch() and variable = MagicMock() is that mocker.patch() is used when the function creates something like what is done in setup() while the latter is done when said variable already exists. Adding onto that, I also had to assign xcor() and ycor() return values because without it, it would keep giving me a TypeError between int and MagicMock, if not the comparison between the mock and true values would fail. And lastly I checked that while the game was running, car objects were being created and the move_all() method was being implemented.

And for test_game_end, I'm merely checking that once I click on the screen, it exits the programme.

# Debating certain design choices, explaining why you made them
At first, I wanted to just use onkeypress() for the player movements but then I ran into the issue of the players only being able to move one at a time with a significant delay between swapping movement so I had to incoporate onkeyrelease() as well so that the programme could register more than just one key at a time and both players could move simultaneously.




