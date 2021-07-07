import prompt


welcome = "Welcome to the Brain Games!"
wrong_answ = " is wrong answer ;(. Correct answer was "


def game(rules, questions, answers):
    print(welcome)
    player_name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(player_name))
    print(rules)
    count_of_question = 0
    count_of_right_answ = 0

    while count_of_question < 3:
        q = questions[count_of_question]
        a = answers[count_of_question]
        print('Question: {}'.format(q))
        player_answer = prompt.string('Your answer: ')
        if player_answer.lower() != a:
            print("'{}'{}'{}'.".format(player_answer, wrong_answ, a))
            break
        else:
            print("Correct!")
            count_of_right_answ = count_of_right_answ + 1
            count_of_question = count_of_question + 1

    if count_of_right_answ == 3:
        print("Congratulations, {}!".format(player_name))
    else:
        print("Let's try again, {}!".format(player_name))
