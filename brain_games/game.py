import prompt
import random


welcome = "Welcome to the Brain Games!"
rules = 'Answer "yes" if the number is even, otherwise answer "no".'
wrong_answ = " is wrong answer ;(. Correct answer was "


# Проверка на чётность
def is_even(number):
    return "yes" if (number % 2) == 0 else "no"


def start_game():
    print(welcome)
    player_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(player_name))
    print(rules)
    count_of_questuon = 3
    count_of_right_answ = 0

    while count_of_questuon > 0:
        random_number = random.randint(1, 100)
        print('Question: {}'.format(random_number))
        player_answer = prompt.string('Your answer: ')
        true_answer = is_even(random_number)
        if player_answer.lower() != true_answer:
            print("'{}'{}'{}'.".format(player_answer, wrong_answ, true_answer))
            break
        else:
            print("Correct!")
            count_of_right_answ = count_of_right_answ + 1
            count_of_questuon = count_of_questuon - 1

    if count_of_right_answ == count_of_questuon:
        print("Congratulations, {}!".format(player_name))
    else:
        print("Let's try again, {}!".format(player_name))
