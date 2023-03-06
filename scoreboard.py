from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.gm = Turtle()
        self.gm.hideturtle()
        self.gm.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 16, 'normal'))

    # ScoreBoard
    def increase(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 16, 'normal'))
    # Game over Text
    def game_over(self):
        self.gm.write(f'Game Over.', move=False, align='center', font=('Arial', 16, 'normal'))