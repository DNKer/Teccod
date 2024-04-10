"""Тестовое задание на вакансию "Fullstack-разработчик"."""


def get_unique_numbers(numbers: list[int]) -> list[int]:
    """Получить уникальные значения списка."""
    return list(set(numbers))


def get_a_prime_numbers(first_number: int, second_number: int) -> list[int]:
    """Получить список всех простых чисел в заданном диапазоне."""
    result: list[int] = []
    if first_number > second_number:
        second_number_temp = first_number
        first_number = second_number
        second_number = second_number_temp
    for number in range(first_number, second_number + 1):
        if (number > 1):
            for divider in range(2, number):
                if (number % divider == 0):
                    break
            else:
                result.append(number)
    return result
