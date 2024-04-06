import turtle
side_length = int(input("Введите длину стороны квадрата: "))
t = turtle.Turtle()
t.speed(0) 
t.penup()
t.goto(-side_length/2, -side_length/2) 
t.pendown()
for _ in range(4):
    t.forward(side_length)
    t.right(90)
turtle.done()
