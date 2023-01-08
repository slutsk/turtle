#ПРОСТОЕ ОКНО
from turtle import *
speed(0)  # максимально быстрая отрисовка
bgcolor("black")

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
    setheading(0)
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

def brick_wall(wB, hB, br_in_ln, br_in_ht, brick_color = "red"):
    """
    wB - длина одного кирпича
    hB - высота одного кирпича
    br_in_ln - число кирпичей в длину
    br_in_ht - число кирпичей в высоту
    """
    x = xcor()
    y = ycor()

    brWidth = br_in_ln * wB
    brHight = br_in_ht * hB

    fill_rectangle(brWidth, brHight, brick_color)


    #Отрисовка горизонтальных линий. Координата yHor уменьшается
    #на высоту кирпича (hB)
    for yHor in range(y-hB, y-brHight, -hB):
        go_to(x, yHor)
        forward(brWidth)

    #Отрисовка вертикальных линий
    right(90)
    fH = 0
    for xVer in range(x+wB//2, brWidth + x, wB//2):
        fV = 0
        for yHor in range(y-hB, y-brHight-hB, -hB):
            if fH %2 == 0 and fV % 2 == 0:
                go_to(xVer, y - fV * hB)
                forward(hB)
            elif fH%2 == 1 and fV % 2 == 1:
                go_to(xVer, y - fV * hB)
                forward(hB)
            fV += 1
        fH +=1

# END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS
wallX = -350
wallY = 300
go_to(wallX, wallY)
pensize(3)
pencolor("#aaaaaa")
widt_brick = 60
height_brick = 30
cntWidth  = 10
cntHeight = 20
brick_wall(widt_brick, height_brick, cntWidth, cntHeight)

WIN_WIDTH = 400
WIN_HEIGHT = 500
D = 15
windowX = (widt_brick*cntWidth-WIN_WIDTH)//2 + wallX;
windowY = wallY - (height_brick*cntHeight-WIN_HEIGHT-D)//2;
go_to(windowX, windowY)


window(WIN_WIDTH, WIN_HEIGHT, D)

hideturtle()

