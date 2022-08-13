'''
Игра "Угадай число!"
Компьютер сам загадывает и угадывает число.
'''

import numpy as np


def random_predict(number:int=1) -> int:
  '''
  Случайным образом угадываем число

  Args:
      number (int, optional): Загаданное число. По-умолчанию 1.

  Returns:
      int: Число попыток
  '''
  
  count = 0
  
  while True:
    count += 1
    predict_number = np.random.randint(1, 101)
    if number == predict_number:
      break
  
  return count


def score_game(random_predict) -> int:
  '''
  Оценивает за сколько попыток в среднем из 1000 подходов наш алгоритм
  угадывает загаданное число

  Args:
      random_predict (function): Функция угадывания, результатом выполнения
      которой является количество попыток

  Returns:
      int: _description_
  '''
  # Список для сохранения количеств попыток
  counts = list()
  # Фиксируем генератор случайных чисел для воспроизводимости
  np.random.seed(1)
  # Задаём 1000 случайных числел в пределах 1-100
  randoms = np.random.randint(1, 101, size=(1000))

  for number in randoms:
    counts.append(random_predict(number))
  
  score = int(np.mean(counts))
  
  print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')    
  return score


if __name__ == 'main':
  # Запуск
  score_game(random_predict)