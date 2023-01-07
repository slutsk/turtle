from turtle import *
speed(0)               #максимально быстрая отрисовка
bgcolor('black')       #цвет фона

penup()                #поднять перо (не рисовать)
goto(-350, 0)          #переместиться в точку
pendown()              #опустить перо
#РИСУЕМ КВАДРАТ
pensize(5)             #размер пера
pencolor('yellow')     #цвет пера
forward(100)           #вперед
left(90)               #влево
forward(100)
left(90)
forward(100)
left(90)
forward(100)

penup()
goto(-200, 0)
pendown()
left(90)

# РИСУЕМ ЗАКРАШЕННЫЙ КВАДРАТ

fillcolor('blue')
pencolor('green')
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

penup()
goto(-50, 50)
pendown()

#РИСУЕМ ЗАКРАШЕННЫЙ КРУГ
fillcolor('red')
pencolor('white')
begin_fill()
circle(50)
end_fill()
