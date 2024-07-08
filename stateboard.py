from turtle import Turtle

FONT = ("Arial", 10, "normal")
ALIGNMENT = "left"


class StateGame(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_state_game(self, state_name, pos_x, pos_y):
        self.goto(pos_x, pos_y)
        self.write(state_name, align=ALIGNMENT, font=FONT)
