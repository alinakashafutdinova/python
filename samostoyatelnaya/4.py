import turtle

square = turtle.Turtle()
square.shape("turtle")

for i in range(180):
    square.speed(10)
    square.forward(i)
    square.left(91)
