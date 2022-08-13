"""
Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


# Для воспроизводимости фиксируем генератор случайных чисел
np.random.seed = 101


def random_predict(number: int = 1) -> int:
    """
    Случайно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def half_search(number: int = 1, min_number: int = 1, max_number: int = 100) -> int:
    """
    Находит загаданное числом методом половинного поиска

    Args:
        number (int, optional): Загаданное число. По умолчанию 1.
        min_number (int, optional): Нижняя граница диапазона загадываемых чисел. По умолчанию 1.
        max_number (int, optional): Верхняя граница диапазона загадываемых чисел. По умолчанию 100.

    Returns:
        int: Количество попыток, затраченных на подбор загаданного числа
    """

    count = 0  # Начальная инициализация счетчика попыток

    while True:
        count += 1

        # Всегда предполагаем, что загаданное число находится
        # в середине возможного диапазона
        # Используем вычисления с плавающей запятой
        predict_number = (max_number + min_number) / 2.0

        # Если предсказанное число отстоит от загаданного меньше, чем на 0.5
        # (значения, необходимого для точного округления до целого, равного
        # загаданному числу), считаем, что нашли искомое
        if abs(predict_number - number) < 0.5:
            break

        # Если предсказанное число больше загаданного
        if predict_number > number:
            # Перемещаем верхнюю границу возможного
            # диапазона к предсказанному числу
            max_number = predict_number
        # Иначе, а именно если предсказанное число
        # меньше загаданного
        else:
            # Перемещаем нижнюю границу возможного
            # диапазона к предсказанному числу
            min_number = predict_number

    # Вычисляем целое предсказанное число
    # округлением встроенной функцией rand
    guessed_number = round(predict_number)

    # Тестируем на равенство загаданного
    # и предсказанного чисел
    assert number == guessed_number

    return count


def score_game(predictor) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predictor ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    count_ls = [predictor(number) for number in random_array]
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(half_search)
