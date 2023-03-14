from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.high_score_read()
        self.gm = Turtle()
        self.gm.hideturtle()
        self.gm.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.color('white')
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', move=False, align='center', font=('Arial', 16, 'normal'))

    # ScoreBoard
    def increase(self):
        self.score += 1
        self.update_scoreboard()

    # Game over Text
    def game_over(self):
        self.gm.write(f'Game Over.', move=False, align='center', font=('Arial', 16, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_write()
        self.score = 0
        self.update_scoreboard()

    def high_score_read(self):
        with open('highscore.txt', mode='r') as file:
            content = file.read()
            return int(content)

    def high_score_write(self):
        with open('highscore.txt', mode='w') as file:
            file.write(str(self.high_score))
