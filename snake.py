from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.build()
        self.head = self.snake[0]

    # Creating the Snake (using negatives to avoid start up crashes)
    def build(self):
        for x in range(2, -1, -1):
            body = Turtle()
            body.penup()
            body.color('white')
            body.shape('square')
            body.goto(20 * x, 0)
            self.snake.append(body)

    # Increasing the size of the snake
    def increase(self):
        size_increase = Turtle()
        size_increase.penup()
        size_increase.shape('square')
        size_increase.color('white')
        size_increase.goto(self.snake[-1].pos())
        self.snake.append(size_increase)

    # Moving using the goto function
    def move(self):
        for x in range(len(self.snake) - 1, -1, -1):
            if x == 0:
                self.snake[x].forward(20)
            else:
                self.snake[x].goto(self.snake[x - 1].position())

    def reset(self):
        for body in self.snake:
            body.goto(1000, 1000)
        self.snake.clear()
        self.build()
        self.head = self.snake[0]

    # Movements
    def turn_left(self):
        if self.snake[0].heading() == 0:
            pass
        else:
            self.snake[0].setheading(180)

    def turn_right(self):
        if self.snake[0].heading() == 180:
            pass
        else:
            self.snake[0].setheading(0)

    def turn_up(self):
        if self.snake[0].heading() == 270:
            pass
        else:
            self.snake[0].setheading(90)

    def turn_down(self):
        if self.snake[0].heading() == 90:
            pass
        else:
            self.snake[0].setheading(270)
