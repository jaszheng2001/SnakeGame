from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in STARTING_POS:
            snake_body = Turtle(shape="square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(pos)
            self.snake.append(snake_body)

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[index - 1].xcor()
            new_y = self.snake[index - 1].ycor()
            self.snake[index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_body(self, pos):
        snake_body = Turtle(shape="square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(pos)
        self.snake.append(snake_body)

    def extend(self):
        self.add_body(self.snake[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def reset(self):
        pass
