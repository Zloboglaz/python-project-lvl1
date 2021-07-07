import random
from brain_games.game_engine import game


rules = 'What is the result of the expression?'


# Формирование кортежа вопросов quest и кортежа правильных ответов answ
def question():
    math_operations = '+-*'
    i = 0
    quest = ()
    answ = ()
    while i < 3:
        rand_num_1 = random.randint(1, 100)
        rand_num_2 = random.randint(1, 100)
        rand_math = random.choice(math_operations)
        quest_str = "{} {} {}".format(rand_num_1, rand_math, rand_num_2)
        temp_quest = (quest_str, )
        temp_answ = (str(eval(quest_str)), )
        quest = quest + temp_quest
        answ = answ + temp_answ
        i = i + 1
    return (quest, answ)


# Запуск самой игры
def calc():
    (quest, rihgt_answ) = question()
    game(rules, quest, rihgt_answ)
