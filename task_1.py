def max_fives_in_sequence(numbers):
    n = len(numbers)
    max_fives = -1
    if n < 7:
        return -1
    # Перебор с использованием алгоритма скользящего окна
    for i in range(n - 6):
        segment = numbers[i:i + 7]
        if 2 in segment or 3 in segment:
            continue
        count_fives = segment.count(5)
        if count_fives > max_fives:
            max_fives = count_fives

    return max_fives


N = int(input())

sequence = list(map(int, input().strip().split()))[:N]

print(max_fives_in_sequence(sequence))
