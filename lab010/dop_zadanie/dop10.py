import random

# Заготовленные ответы для каждого из трех вопросов
answers = [
    ["да", "нет", "не знаю"],
    ["возможно", "интересно", "эх"],
    ["классно", "не обижай меня", "я так не думаю"]
]

# Функция для голосового помощника
def voice_assistant():
    for i in range(3):
        question = input("Задайте вопрос: ")
        if i == 0:
            answer = random.choice(answers[0])
        elif i == 1:
            answer = random.choice(answers[1])
        else:
            answer = random.choice(answers[2])
            
        print("Ответ:", answer)

voice_assistant()
