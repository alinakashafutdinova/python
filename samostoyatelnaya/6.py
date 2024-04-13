import turtle

radius = float(input("Введите радиус первого круга (синего): "))

t = turtle.Turtle()

# Рисуем синий круг с указанным радиусом
t.color("blue")
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(radius)

colors = ["red", "green", "orange", "purple"]

# Рисуем остальные круги с разными цветами
for i in range(1, 5):
    t.penup()
    t.goto(0, -radius*(i+0.5))
    t.pendown()
    t.color(colors[i-1])
    t.circle(radius * (i+1))

turtle.done()

