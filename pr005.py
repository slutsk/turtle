#Шахматная доска
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

def draw_square(a, fill_color = 'white'):
    fillcolor(fill_color)
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


# END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS-END FUNCTIONS

SIDE_OF_SQUARE    = 60   # размеры одной клетки квадрата (длина квадрата)
START_COR_X       = -300 # стартовые координаты по Х
START_COR_Y       = 250  #                      по Y
BORDER            = 50   # граница вокруг шахматной доски
SIZE_BORD         =  8*SIDE_OF_SQUARE + 2*BORDER # размер шахматной доски
FONT_SIZE         = 20

go_to(START_COR_X - BORDER, START_COR_Y + BORDER)
draw_square(SIZE_BORD, "#aaaaff")

go_to(START_COR_X, START_COR_Y);

for horisont in range(8):
    for vertical in range(8):
        go_to(horisont*SIDE_OF_SQUARE + START_COR_X, START_COR_Y - vertical*SIDE_OF_SQUARE)
        if (horisont + vertical)%2==1:
            draw_square(SIDE_OF_SQUARE, 'black')
        else:
            draw_square(SIDE_OF_SQUARE, 'white')

#отрисовка чисел на доске
for num in range(8):
    go_to(START_COR_X-SIDE_OF_SQUARE//2, START_COR_Y - SIDE_OF_SQUARE//5*4 - num * SIDE_OF_SQUARE)
    write(str(num+1), font=('Arial', FONT_SIZE))

#отрисовка букв на доске
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(8):
    go_to(START_COR_X + SIDE_OF_SQUARE//7*3  + SIDE_OF_SQUARE*i, START_COR_Y - 8*SIDE_OF_SQUARE - BORDER//4*3)
    write( abc[i], font=('Arial', FONT_SIZE))
