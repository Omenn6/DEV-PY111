from typing import List


def find_consensus_string(dna_strands: List[str]) -> str:
    """
    Поиск консенсус-строки из списка DNA ридов одинаковой длины
    """
    if not dna_strands:
        return ""

    # Все строки одинаковой длины, берем длину первой
    str_len = len(dna_strands[0])
    consensus_string = ""

    # Идем по каждому столбику букв слева направо
    for i in range(str_len):
        # Словарь для подсчета частоты букв в текущем столбике
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        # Считаем буквы в i-м столбике по всем строкам
        for strand in dna_strands:
            char = strand[i]
            if char in counts:
                counts[char] += 1

        # Выбираем букву, которая встретилась чаще всего
        max_char = max(counts, key=counts.get)
        consensus_string += max_char

    return consensus_string


if __name__ == '__main__':
    test_dna = [
        "ATTA",
        "ACTA",
        "AGCA",
        "ACAA"
    ]
    print(f"Консенсус-строка: {find_consensus_string(test_dna)}")  # Ожидается: ACTA
