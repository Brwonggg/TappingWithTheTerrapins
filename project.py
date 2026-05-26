import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

game_is_on = True

def main():
    setup()
    game_loop()
    game_end()

def setup():
    global screen, car_manager, scoreboard1, scoreboard2, player1, player2

    screen = Screen()
    screen.title("Tapping with the Terrapins")
    screen.setup(width=700, height=700)
    screen.tracer(0)

    player1 = Player((0,-330),90, "blue")
    player2 = Player((0,330),270, "red")
    player1_score = 0
    player2_score = 0

    scoreboard1 = Scoreboard((230, -340), f"Score:{player1_score}")
    scoreboard2 = Scoreboard((-340, 320), f"Score:{player2_score}")

    car_manager = CarManager()

    #Player1 movement
    screen.onkeypress(player1.move_forward, "Up")
    screen.onkeyrelease(player1.move_forward, "Up")
    screen.onkeypress(player1.move_left, "Left")
    screen.onkeyrelease(player1.move_left, "Left")
    screen.onkeypress(player1.move_right, "Right")
    screen.onkeyrelease(player1.move_right, "Right")

    #Player2 movement
    screen.onkeypress(player2.move_forward, "w")
    screen.onkeyrelease(player2.move_forward, "w")
    screen.onkeypress(player2.move_left, "a")
    screen.onkeyrelease(player2.move_left, "a")
    screen.onkeypress(player2.move_right, "d")
    screen.onkeyrelease(player2.move_right, "d")
    screen.listen()

def game_loop():
    global game_is_on
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_all()

        #player-player collision > reset both to starting pos
        if abs(player2.ycor() - player1.ycor()) <= 30 and abs(player2.xcor() - player1.xcor()) <= 30:
            player1.goto(player1.starting_position)
            player2.goto(player2.starting_position)

        #player-car collision > reset hit player to starting pos and deduct point
        for car in car_manager.all_cars:
            if abs(player1.ycor() - car.ycor()) <= 25 and abs(player1.xcor() - car.xcor()) <= 30:
                player1.goto(player1.starting_position)
                scoreboard1.deduct_score1()

            elif abs(player2.ycor() - car.ycor()) <= 25 and abs(player2.xcor() - car.xcor()) <= 30:
                player2.goto(player2.starting_position)
                scoreboard2.deduct_score2()

        #reset position for player going outside of x boundaries/playing zone
        else:
            if player1.ycor() > 340:
                player1.goto(player1.starting_position)
                scoreboard1.update_score1()

            elif player2.ycor() < -340:
                player2.goto(player2.starting_position)
                scoreboard2.update_score2()

        #game ends + display winner once someone hits 5 points
        if scoreboard1.score1 == 5:
            scoreboard1.display_winner(1)
            game_is_on = False

        elif scoreboard2.score2 == 5:
            scoreboard2.display_winner(2)
            game_is_on = False

def game_end():
    screen.update()
    screen.exitonclick()

if __name__ == "__main__":
    main()
