import turtle

square = turtle.Turtle()
square.shape("turtle")

for i in range(180):
    square.speed(100)
    square.forward(i)
    square.left(91)

input("Press the Enter key to continue: ")