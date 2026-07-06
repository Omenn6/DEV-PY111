"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди: индекс 0
        Конец очереди: последний индекс списка
        """
        self._storage = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемента в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._storage.append(elem)  # TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self._storage:
            raise IndexError("Dequeue from an empty queue")
        return self._storage.pop(0)  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError("Index must be an integer")
        if not 0 <= ind < len(self._storage):
            raise IndexError("Queue index out of range")
        return self._storage[ind]  # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self._storage.clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self._storage) # TODO реализовать метод __len__


if __name__ == '__main__':
    # Создаем очередь
    q = Queue()

    # Добавляем элементы
    q.enqueue("Первый")
    q.enqueue("Второй")
    print(f"Длина очереди: {len(q)}")  # Ожидается: 2

    # Смотрим первый элемент без извлечения
    print(f"Первый в очереди: {q.peek(0)}")  # Ожидается: Первый

    # Извлекаем элементы
    print(f"Извлечено: {q.dequeue()}")  # Ожидается: Первый
    print(f"Извлечено: {q.dequeue()}")  # Ожидается: Второй
