import random
from brain_games.game_engine import game


rules = 'Answer "yes" if the number is even, otherwise answer "no".'


# Формирование кортежа вопросов quest и кортежа правильных ответов answ
def question():
    i = 0
    quest = ()
    answ = ()
    while i < 3:
        random_number = random.randint(1, 100)
        temp_quest = (random_number, )
        temp_answ = (right_answer(random_number), )
        quest = quest + temp_quest
        answ = answ + temp_answ
        i = i + 1
    return (quest, answ)


# Получение правильного ответа
def right_answer(quest):
    aswer = "yes" if (quest % 2) == 0 else "no"
    return aswer


# Запуск самой игры
def even():
    (quest, rihgt_answ) = question()
    game(rules, quest, rihgt_answ)
