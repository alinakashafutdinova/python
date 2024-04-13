import random
def generate_password(length):
    password = ''
    for _ in range(length):
        password += str(random.randint(0, 9)) #добавление случайной цифры к строке 
    return password

length = int(input("Введите длину пароля: "))
password = generate_password(length)
print(f"Сгенерированный пароль: {password}")