def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    brackets_map = {")": "(", "}": "{", "]": "["}
    stack = []  # TODO реализовать проверку скобочной группы

    for char in brackets_row:
        # Если скобка открывающая, кладем её в стек
        if char in brackets_map.values():
            stack.append(char)
        # Если скобка закрывающая
        elif char in brackets_map:
            # Если стек пуст или верхний элемент не совпадает — строка невалидна
            if not stack or stack.pop() != brackets_map[char]:
                return False

        # Если в конце стек пуст — все скобки закрылись правильно
    return len(stack) == 0

if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
