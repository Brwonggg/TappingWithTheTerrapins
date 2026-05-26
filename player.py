from turtle import Turtle

MOVE_DISTANCE = 10
FORWARD_DISTANCE = 20

class Player(Turtle):
    def __init__(self, starting_position, direction, colour):
        super().__init__()
        self.starting_position = starting_position
        self.direction = direction
        self.colour = colour
        self.shape("turtle")
        self.penup()
        self.goto(self.starting_position)
        self.setheading(self.direction)
        self.color(self.colour)

    def move_forward(self):
        self.forward(FORWARD_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(self.direction)

        if self.xcor() < -330:
            self.goto(self.starting_position)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(self.direction)

        if self.xcor() > 330:
            self.goto(self.starting_position)




