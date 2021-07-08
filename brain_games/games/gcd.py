import random
from brain_games.game_engine import game


rules = 'Find the greatest common divisor of given numbers.'


# Расчёт делителей (вывод в кортеж)
def get_divider(number):
    divider = 1
    result = ()
    while divider <= number:
        if (number % divider == 0):
            result = result + (divider, )
        divider = divider + 1
    return result


# Поиск НОД 2-х чисел
def get_gsd(num1, num2):
    num1_dividers = get_divider(num1)
    num2_dividers = get_divider(num2)
    dividers_1_lenth = len(num1_dividers)
    dividers_2_lenth = len(num2_dividers)
    result = 1
    if dividers_1_lenth <= dividers_2_lenth:
        i = 0
        while i < dividers_1_lenth:
            if num2_dividers.count(num1_dividers[i]) != 0:
                result = num1_dividers[i]
            i = i + 1
    else:
        i = 0
        while i < dividers_2_lenth:
            if num1_dividers.count(num2_dividers[i]) != 0:
                result = num2_dividers[i]
            i = i + 1
    return result


# Формирование кортежа вопросов quest и кортежа правильных ответов answ
def get_question():
    i = 0
    quest = ()
    answ = ()
    while i < 3:
        rand_num_1 = random.randint(1, 100)
        rand_num_2 = random.randint(1, 100)
        quest_str = "{} {}".format(rand_num_1, rand_num_2)
        temp_quest = (quest_str, )
        temp_answ_str = str(get_gsd(rand_num_1, rand_num_2))
        temp_answ = (temp_answ_str, )
        quest = quest + temp_quest
        answ = answ + temp_answ
        i = i + 1
    return (quest, answ)


# Запуск самой игры
def gcd():
    (quest, rihgt_answ) = get_question()
    game(rules, quest, rihgt_answ)
