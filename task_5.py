def max_mushrooms(n, forest):
    # Используем список списков для dp таблицы
    dp = [[-float('inf')] * 3 for _ in range(n)]

    # Инициализация первой строки
    for j in range(3):
        if forest[0][j] == 'W':
            dp[0][j] = -float('inf')  # Непроходимые кусты
        elif forest[0][j] == 'C':
            dp[0][j] = 1  # Гриб
        else:
            dp[0][j] = 0  # Пустая клетка

    # Заполнение таблицы dp
    for i in range(n - 1):
        for j in range(3):
            if dp[i][j] != -float('inf'):  # Только если текущая клетка доступна
                # Смотрим три возможных клетки в следующей строке
                for dj in [-1, 0, 1]:  # Смещение по столбцам
                    nj = j + dj
                    if 0 <= nj < 3:  # Проверка на выход за границы
                        if forest[i + 1][nj] != 'W':  # Нельзя переместиться в кусты
                            mushrooms = dp[i][j] + (1 if forest[i + 1][nj] == 'C' else 0)
                            dp[i + 1][nj] = max(dp[i + 1][nj], mushrooms)

    # Ищем максимальное значение в последней строке
    max_gathered = max(dp[n - 1])

    # Если все значения -inf, значит лесник не смог начать свою прогулку
    return max_gathered if max_gathered != -float('inf') else 0


def read_forest(n):
    input_list = []
    for _ in range(n):
        input_list.append(input())
    return input_list


N = int(input())
forest = read_forest(N)

print(max_mushrooms(N, forest))
