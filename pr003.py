#ПРОСТОЕ ОКНО
from turtle import *
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

def fill_rectangle(w, h, fill_color):
    """
    отрисовка прямоугольника длиной w и высотой h,
    закрашенного цветом fill_color
    """
    fillcolor(fill_color);
    begin_fill()
    rectangle(w, h)
    end_fill()


def window(w, h, d):
    """
    Рисуем окно
    Ширина окна w; высота окна h; толщина рамы d
    """
    x = xcor() #запомнить первоначальные координаты
    y = ycor() #x и y
    COLOR_WINDOW = "#aaaaff"
    pensize(1)
    pencolor("black")
    fill_rectangle(w, h, "#A17752")
    go_to(x+d, y-d)
    w1 = w - 2*d #размеры внутреннего прямоугольника
    h1 = h - 2*d
    fill_rectangle(w1, h1, "#b09975")
    w_ = (w1-3*d)//2 #размер стекла в окне
    h_ = (h1-3*d)//2
    go_to(x+2*d, y-2*d)
    fill_rectangle(w_, h_, COLOR_WINDOW)

    go_to(x+ w1 - w_, y-2*d)
    fill_rectangle(w_, h_, COLOR_WINDOW)

    go_to(x+2*d, y-h1+h_)
    fill_rectangle(w_, h_, COLOR_WINDOW)

    go_to(x+w1-w_, y-h1+h_)
    fill_rectangle(w_, h_, COLOR_WINDOW)

    go_to(x-2*d, y-h)
    fill_rectangle(w+4*d, 2*d, "#A17752")


# END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS
go_to(-300, 200)
window(200, 150, 10)
