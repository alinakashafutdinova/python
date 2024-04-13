import turtle

# Запрашиваем радиус первого круга у пользователя
radius = float(input("Введите радиус первого круга (синего): "))

# Создаем экземпляр черепахи
t = turtle.Turtle()

# Рисуем синий круг с указанным радиусом
t.color("blue")
t.circle(radius)

# Рисуем остальные круги только с контурами
for i in range(1, 5):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("red")
    t.circle(radius * (i+1))

# Завершаем работу черепахи
turtle.done()
