import random
from brain_games.game_engine import game


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Формирование кортежа вопросов quest и кортежа правильных ответов answ
def get_questions():
    i = 0
    quest = ()
    answ = ()
    while i < 3:
        random_number = random.randint(1, 100)
        temp_quest = (random_number, )
        temp_answ = (get_right_answer(random_number), )
        quest = quest + temp_quest
        answ = answ + temp_answ
        i = i + 1
    return (quest, answ)


# Получение правильного ответа
def get_right_answer(number):
    dividers_count = 0
    divider = 2
    while divider <= number:
        if number % divider == 0:
            dividers_count = dividers_count + 1
        divider = divider + 1
    aswer = "yes" if dividers_count == 1 else "no"
    return aswer


# Запуск самой игры
def prime():
    (quest, rihgt_answ) = get_questions()
    game(rules, quest, rihgt_answ)
