from turtle import *
speed(0)  # максимально быстрая отрисовка
bgcolor("black")
hideturtle()
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

def rectangle(w, h):
    """
    отрисовка прямоугольника длиной w и высотой h
    """

    forward(w)
    right(90)
    forward(h)
    right(90)
    forward(w)
    right(90)
    forward(h)
    right(90)

def filled_rectangle(w, h, fill_color):
    """
    отрисовка прямоугольника длиной w и высотой h,
    закрашенного цветом fill_color
    """
    fillcolor(fill_color);
    begin_fill()
    rectangle(w, h)
    end_fill()

def square(a):
    """
    рисует квадрат со стороной a
    """
    rectangle(a, a)

def fill_square(a, color):
    """
    рисует квадрат со стороной a и цветом color
    """
    fillcolor(color);
    begin_fill()
    square(a)
    end_fill()

# END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS

go_to(-300, -200)

# РИСУЕМ КВАДРАТ
pensize(3)
pencolor("yellow")
fill_square(100, "#250379")
go_to(-180, -100)
pencolor("#aaffff")
fill_square(200, "#affa00")
go_to(40, 0)
pencolor("yellow")
fill_square(300, "#5050ff")

go_to(-300, 200)
pencolor("red")
filled_rectangle(640, 180, "#00ff00")

go_to(-300, 0)
pencolor('purple')
rectangle(320, 80)

go_to(-300, -100)
pencolor('#0000ff')
rectangle(100, 80)
heading("false")
