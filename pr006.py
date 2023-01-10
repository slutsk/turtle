#Бешеная черепаха
from turtle import *
import random
speed(0)  # максимально быстрая отрисовка
bgcolor("gray")

# FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS-FUNCTIONS
def go_to(x, y):
    """
    Черепаха поднимает перо;
    перемещается в координаты x, y;
    опускает перо.
    """
    penup()
    goto(x, y)
    pendown()

def draw_square(a, fc, pc):
    pensize(random.randint(1, 4))
    color(fc, pc)
    begin_fill()
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    end_fill()

def draw_triangle(a, fc, pc):
    pensize(random.randint(1, 4))
    color(fc, pc)
    begin_fill()
    forward(a)
    right(120)
    forward(a)
    right(120)
    forward(a)
    end_fill()

def random_color():
    return random.random(), random.random(), random.random()
# END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS

while(True):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    go_to(x, y)
    right(random.randint(0, 180))
    rnd = random.randint(1, 3)
    if rnd == 1:
        draw_square(random.randint(10, 100), random_color(), random_color())
    elif rnd == 2:
        draw_triangle(random.randint(10, 100), random_color(), random_color())
    else:
        color(random_color(), random_color())
        go_to(x, y)
        begin_fill()
        circle(random.randint(10, 50))
        end_fill()
