from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# initializing screen obj and setting attributes
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title("Snake Game")

# initializing score obj
score = Score()

# initializing snake obj
snake = Snake()

# initializing food obj
food = Food()

# creating even listening
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

# checking if the game is On and moving the snake
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # checking if the snake has touched the food
    if snake.head.distance(food) < 15:
        score.calculate_score()
        score.display_score()
        food.refresh()
        snake.extend_snake()

    # Checking if the snake touches the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    # checking if the snake touches itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
