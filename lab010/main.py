rightCounter = 0
questionsCounter = 0

questions = ["Сколько планет в Солнечной системе?", 
             "Как называется столица Франции?", 
             "Какой город является столицей Японии?"]
rightAnswers = ["8", "Париж", "Токио"]

while questionsCounter < len(questions):
    answer = input(questions[questionsCounter] + ": ")
    
    if answer.capitalize() == rightAnswers[questionsCounter]:
        print("Вы ответили верно!")
        rightCounter += 1
    else:
        print("Вы ответили неверно!")
    
    questionsCounter += 1

print(f"Вы набрали баллов: {rightCounter}")
