from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.display_score()

    def calculate_score(self):
        self.score += 1

    def display_score(self):
        score_msg = "Score : " + str(self.score)
        self.clear()
        self.goto(0, 270)
        self.write(arg=score_msg, move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
