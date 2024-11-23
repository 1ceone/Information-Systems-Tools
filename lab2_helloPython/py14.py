def spiral_matrix(n):
    # Создаем пустую матрицу размером n x n, заполненную нулями
    matrix = [[0] * n for _ in range(n)]

    # Определяем границы текущего слоя
    left, right, top, bottom = 0, n - 1, 0, n - 1
    num = 1  # Начальное число

    while left <= right and top <= bottom:
        # Заполняем верхнюю строку
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Заполняем правый столбец
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        if top <= bottom:
            # Заполняем нижнюю строку
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        if left <= right:
            # Заполняем левый столбец
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


# Чтение входных данных
n = int(input("Введите размер ковра (n): "))

# Получение матрицы с числами по спирали
result = spiral_matrix(n)

# Вывод матрицы
for row in result:
    print(" ".join(map(str, row)))