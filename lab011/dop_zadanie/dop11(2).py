from turtle import *
shape("turtle")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
showturtle() 
speed(10)

for i in range(7):
    color(colors[i])
    circle((i + 1) * 15)

done()