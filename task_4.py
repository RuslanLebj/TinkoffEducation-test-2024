def rotate_matrix_operations(n, direction, matrix):
    operations = []

    # Функция для добавления операции
    def add_operation(x1, y1, x2, y2):
        operations.append(((x1, y1), (x2, y2)))
        # Свапаем элементы в матрице
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]

    # Вращение матрицы
    for i in range(n // 2):
        for j in range((n + 1) // 2):
            if direction == 'R':
                # Позиции для ротации вправо
                original = (i, j)
                positions = [
                    (j, n - 1 - i),
                    (n - 1 - i, n - 1 - j),
                    (n - 1 - j, i),
                    (i, j)
                ]
            else:
                # Позиции для ротации влево
                original = (i, j)
                positions = [
                    (n - 1 - j, i),
                    (n - 1 - i, n - 1 - j),
                    (j, n - 1 - i),
                    (i, j)
                ]

            # Выполняем цикл из 4 элементов
            # (i, j) -> (j, n-1-i) -> (n-1-i, n-1-j) -> (n-1-j, i) -> обратно в (i, j)
            pos1, pos2, pos3, pos4 = positions[0], positions[1], positions[2], positions[3]
            add_operation(*pos1, *pos2)
            add_operation(*pos1, *pos3)
            add_operation(*pos1, *pos4)

    return len(operations), operations


def read_matrix(n):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


def tuples_to_string(tuples_list):
    lines = []

    for tuple_pair in tuples_list:
        line = ' '.join(f'{x} {y}' for x, y in tuple_pair)
        lines.append(line)

    result = '\n'.join(lines)
    return result


n, direction = input().split()
n = int(n)
matrix = read_matrix(n)
opertaions = rotate_matrix_operations(n, direction, matrix)
f_output = f'{opertaions[0]}\n'
f_output += tuples_to_string(opertaions[1])
print(f_output)
