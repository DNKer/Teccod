"""Тестовое задание на вакансию "Fullstack-разработчик".

Программа, которая сортирует список строк по длине, сначала по
возрастанию, а затем по убыванию.
"""


from typing import List


def read_input() -> List[str]:
    """Cчитываем данные."""
    print("Введите строки для сортировки через пробел.")
    output = input().split()
    return output


def main() -> None:
    """Cортировка по длине строк."""
    input_strings = read_input()
    # Сортировка от меньшего к большему.
    input_strings.sort(key=len)
    print(f"Отсортированный список от меньшей длины к большей: "
          f"{' '.join(input_strings)}"
          )
    # Сортировка от большего к меньшему.
    sorted_strings = sorted(input_strings, key=len, reverse=True)
    print(f"Отсортированный список от большей длины к меньшей: "
          f"{' '.join(sorted_strings)}"
          )


if __name__ == '__main__':
    main()
