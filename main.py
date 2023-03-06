from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_on = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(key='Left', fun=snake.turn_left)
screen.onkeypress(key='Right', fun=snake.turn_right)
screen.onkeypress(key='Up', fun=snake.turn_up)
screen.onkeypress(key='Down', fun=snake.turn_down)

while game_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    # Feed the snake
    if snake.head.distance(food) <= 20:
        scoreboard.increase()
        food.new_position()
        snake.increase()
    # Checking if it's hitting a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False
    # Checking if it's hitting its tail
    for x in snake.snake[1:]:
        if snake.head.distance(x) < 15:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
