# Считываем строку и приводим к нижнему регистру
s = input().lower()

# Разбиваем строку на отдельные слова
words = s.split()

# Создаем пустой словарь для подсчета слов
word_count = {}

# Подсчитываем количество каждого слова
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Выводим результат
for word, count in word_count.items():
    print(f"{word} : {count}")