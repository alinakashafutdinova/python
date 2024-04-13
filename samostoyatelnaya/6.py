import turtle

# Получаем радиус первого круга от пользователя
radius = float(input("Введите радиус первого круга (синего): "))

# Создаем экран и черепашку
screen = turtle.Screen()
t = turtle.Turtle()

t.speed(15)

colors = ["blue", "red", "green", "orange", "purple", "yellow"]
for i in range(1, 6):
    t.penup()
    t.goto(0, -radius * (i + 1))
    t.pendown()
    t.pencolor(colors[i-1])
    t.circle(radius * (i + 1), None, 100)  

# Закрываем черепашку по клику
screen.exitonclick()