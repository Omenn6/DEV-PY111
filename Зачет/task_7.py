from typing import List


def sort_rocket_data(arr: List[int]) -> List[int]:
    """
    Эффективная сортировка подсчетом за линейное время O(N)
    для массива из 10^6 элементов в диапазоне от 13 до 25.
    """
    if not arr:
        return []

    min_val = 13
    max_val = 25

    # Создаем массив счетчиков для 13 возможных чисел
    counts = [0] * (max_val - min_val + 1)

    # Подсчитываем, сколько раз встретилось каждое число
    for num in arr:
        counts[num - min_val] += 1

    # Восстанавливаем отсортированный массив обратно
    sorted_arr = []
    for i, count in enumerate(counts):
        actual_number = i + min_val
        sorted_arr.extend([actual_number] * count)

    return sorted_arr


if __name__ == '__main__':
    test_data = [25, 13, 14, 25, 13, 14, 15, 20]
    print("Результат сортировки:", sort_rocket_data(test_data))  # Ожидается: [13, 13, 14, 14, 15, 20, 25, 25]
