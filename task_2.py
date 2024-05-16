def rotate_matrix_90_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])

    rotated = []
    # Создаём новую матрицу, где каждый новый ряд формируется из соответствующего столбца исходной матрицы,
    # взятого в обратном порядке.
    for j in range(m):
        new_row = []
        for i in range(n - 1, -1, -1):
            new_row.append(matrix[i][j])
        rotated.append(new_row)

    return rotated


def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix


n, m = map(int, input().split())
matrix = read_matrix(n, m)
rotated_matrix = rotate_matrix_90_clockwise(matrix)
f_output = ''
for row in rotated_matrix:
    f_output += f"{' '.join(map(str, row))}\n"
print(f_output)

