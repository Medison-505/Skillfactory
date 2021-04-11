import numpy as np


def game_core_v3(number):
    # Используем метод бинарного поиска.  Функция принимает загаданное число и возвращает число попыток.
    count = 1
    min_point = 1
    max_point = 101
    predict = (min_point + max_point) // 2

    while number != predict:
        count += 1

        if predict < number:
            min_point = predict
        else:
            max_point = predict
        predict = (min_point + max_point) // 2

    return count


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число.
    count_ls = []
    np.random.seed(1)  # Фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game(game_core_v3)


"""
Метод бинарного поиска показал себя наиболее эффективно при решении данной задачи.
 
Алгоритм вернул загаданное число за  попытки.
Против 101 и 33 попыток при использовании методов прямого перебора без условий и с условием соответственно.

"""
