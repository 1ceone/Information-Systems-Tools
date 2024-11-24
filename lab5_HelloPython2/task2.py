# Создаем список для хранения строк матрицы
matrix = []

# Чтение строк до строки с "end"
while True:
    line = input()
    if line == "end":
        break
    matrix.append(list(map(int, line.split())))

# Проходим по каждой строке матрицы и находим минимальное значение
for row in matrix:
    print(min(row))