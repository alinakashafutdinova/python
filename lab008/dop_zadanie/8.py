text = input("Введите текст: ")
word = input("Введите слово для поиска: ")

# Разделяем текст на слова и сохраняем их позиции
words = text.split()
found = False

for i, w in enumerate(words):
    if w == word or w == word.capitalize() or w == word.upper() or w == word.lower():
        found = True
        print(f"Слово '{word}' найдено в позиции {i}")
        break

if not found:
    print(f"Слово '{word}' не найдено в тексте")