from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return []

    max_val = container[0]
    for num in container:
        if num > max_val:
            max_val = num

    count_arr = [0] * (max_val + 1)

    for num in container:
        count_arr[num] += 1

    sorted_arr = []
    for num, count in enumerate(count_arr):
        sorted_arr.extend([num] * count)

    return sorted_arr  # TODO реализовать алгоритм сортировки подсчетами
