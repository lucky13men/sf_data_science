"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. По умолчанию кмопьютер
        выбирает случайное число в диапазоне от 1 до 100.

    Returns:
        int: Число попыток
    """

    count = 0
    min_pr_num = 1
    max_pr_num = 101
    predict_number = np.random.randint(min_pr_num, max_pr_num)
    check_ls = list(range(min_pr_num, max_pr_num))  # Список всех чисел

    while True:
        count += 1
        if len(check_ls) <= 2:
            if number == check_ls[0]:
                break
            else:
                count += 1
                break
        else:
            if number > predict_number:
                min_pr_num = predict_number
                predict_number = (min_pr_num+max_pr_num) // 2
            elif number < predict_number:
                max_pr_num = predict_number
                predict_number = (min_pr_num+max_pr_num) // 2
            else:
                break # выход из цикла, если угадали
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш
    алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости на другом 
    random_array = np.random.randint(1, 101, size=(1000)) # заг-ли список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


if __name__ == '__main__':
    score_game(random_predict)