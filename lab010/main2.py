import random

timeList = ["Сегодня", "Завтра", "Очень скоро"]
eventList = ["вы встретите", "с вами случится", "вы найдёте"]
objectList = ["что-то волшебное", "необычный инцидент", "большой сюрприз"]

while True:
    zodiac_sign = input("Введите знак Зодиака: ").capitalize()  # Приводим первую букву к верхнему регистру

    # Проверка корректности введенного знака Зодиака
    valid_zodiac_signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]
    if zodiac_sign not in valid_zodiac_signs:
        print("Пожалуйста, введите корректный знак Зодиака.")
        continue  # Переходим на следующую итерацию цикла

    time = timeList[random.randint(0, len(timeList) - 1)]
    event = eventList[random.randint(0, len(eventList) - 1)]
    obj = objectList[random.randint(0, len(objectList) - 1)]

    print(time + " " + event + " " + obj)

    next_input = input("Хотите попробовать ещё раз? (да/нет): ")
    if next_input.lower() != "да":
        break

print("Приходите ещё за новыми предсказаниями!")
