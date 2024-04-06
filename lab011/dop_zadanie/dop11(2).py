from turtle import *

# Список цветов
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

hideturtle()
speed(10)

for i in range(7):
    color(colors[i])  # Выбираем цвет из списка
    circle((i+1)*15)

done()
