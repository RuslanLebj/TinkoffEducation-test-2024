def list_directories(input_data):
    from collections import defaultdict
    import sys

    # Вспомогательная функция для создания рекурсивного словаря
    def recursive_dd():
        return defaultdict(recursive_dd)

    # Чтение количества директорий
    n = int(input_data[0])
    paths = input_data[1:n+1]

    # Создание корня дерева директорий
    directory_tree = recursive_dd()

    # Заполнение дерева директорий
    for path in paths:
        parts = path.split('/')
        node = directory_tree
        for part in parts:
            node = node[part]

    # Вспомогательная функция для вывода структуры директорий
    def print_tree(node, depth=0):
        keys = sorted(node.keys())
        result = []
        for key in keys:
            result.append('  ' * depth + key)
            result.extend(print_tree(node[key], depth + 1))
        return result

    return print_tree(directory_tree)


def read_input(n):
    input_list = [n]
    for _ in range(n):
        input_list.append(input())
    return input_list


N = int(input())
tree_input = read_input(N)
output = list_directories(tree_input)
f_output = ''
for line in output:
    f_output += f"{line}\n"
print(f_output)

