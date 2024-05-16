from collections import deque


def min_moves_to_target(n, board):
    # Всевозможные ходы для коня
    horse_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    # Всевозможные ходы для короля
    king_moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Ищем начальные и конечные позиции
    start_pos = None
    finish_pos = None
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'S':
                start_pos = (i, j)
            elif board[i][j] == 'F':
                finish_pos = (i, j)

    # BFS - Алгоритм поиска в ширину
    queue = deque([(start_pos[0], start_pos[1], 'K', 0)])
    visited = {start_pos[0], start_pos[1], 'K'}

    while queue:
        x, y, piece, moves = queue.popleft()

        # Определяем набор ходов на основе текущей фигуры
        current_moves = horse_moves if piece == 'K' else king_moves

        # Исслелуем всевозможные ходы
        for dx, dy in current_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 'K':
                    new_piece = 'K'
                elif board[nx][ny] == 'G':
                    new_piece = 'G'
                else:
                    new_piece = piece

                # Проверяем дошли ли мы до финиша
                if (nx, ny) == finish_pos:
                    return moves + 1

                # Добавляем в очередь, если не посещали
                if (nx, ny, new_piece) not in visited:
                    visited.add((nx, ny, new_piece))
                    queue.append((nx, ny, new_piece, moves + 1))

    return -1


def read_board(n):
    input_list = []
    for _ in range(n):
        input_list.append(input())
    return input_list


N = int(input())
board = read_board(N)

print(min_moves_to_target(N, board))
