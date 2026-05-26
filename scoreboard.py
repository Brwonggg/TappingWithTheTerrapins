from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position, text):
        super().__init__()
        self.position = position
        self.text = text
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.write(text, align="left", font=('Courier', 20, 'normal'))
        self.score1 = 0
        self.score2 = 0

    def update_score1(self):
        self.score1 += 1
        self.clear()
        self.write(f"Score:{self.score1}",align="left", font=('Courier', 20, 'normal'))
        return self.score1

    def update_score2(self):
        self.score2 += 1
        self.clear()
        self.write(f"Score:{self.score2}",align="left", font=('Courier', 20, 'normal'))
        return self.score2

    def deduct_score1(self):
        self.score1 -= 1
        self.clear()
        self.write(f"Score:{self.score1}",align="left", font=('Courier', 20, 'normal'))
        return self.score1

    def deduct_score2(self):
        self.score2 -= 1
        self.clear()
        self.write(f"Score:{self.score2}",align="left", font=('Courier', 20, 'normal'))
        return self.score2

    def display_winner(self, player):
        self.clear()
        self.goto(0, 0)
        self.write(f"Player {player} Wins!", align="center", font=("Courier", 30, "bold"))



