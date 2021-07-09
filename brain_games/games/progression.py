import random
from brain_games.game_engine import game


rules = 'What number is missing in the progression?'


# формирование прогрессии (вывод в кортеж)
# start - первый элемент
# step - шаг прогрессии
# lenth - количество элементов
def get_progression(start, step, lenth):
    next_element = start
    result = (start, )
    i = 1
    while i <= lenth:
        next_element = next_element + step
        i = i + 1
        result = result + (next_element, )
    return result


# формирование прогрессии с скрытым элементов и ответом, что скрыто (в кортеж)
# progression - прогрессия (в кортеже)
# hidden - номер скрытого элемента
def make_hidden_element(progression, hidden):
    lenth = len(progression)
    i = 1
    question = ''
    answer = str(progression[hidden - 1])
    while i <= lenth:
        if i == hidden:
            question = question + "... "
        else:
            question = question + "{} ".format(progression[i - 1])
        i = i + 1
    return (question, answer)


# формирование 3-х воросов с правильными ответами (вывод в кортеж)
def get_questions():
    i = 0
    quest = ()
    answ = ()
    while i < 3:
        prog_start = random.randint(1, 50)  # первый элемент
        prog_lenth = random.randint(5, 10)  # количество элементов
        prog_step = random.randint(1, 10)   # шаг
        hide_element = random.randint(1, prog_lenth)  # номер скрытого элем.
        progression = get_progression(prog_start, prog_step, prog_lenth)
        (temp_quest, temp_answ) = make_hidden_element(progression, hide_element)
        quest = quest + (temp_quest, )
        answ = answ + (temp_answ, )
        i = i + 1
    return (quest, answ)


# Запуск самой игры
def progression():
    (quest, rihgt_answ) = get_questions()
    game(rules, quest, rihgt_answ)
