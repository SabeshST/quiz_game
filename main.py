import replit
from data import QuizMaster
import random
question_data = QuizMaster.question_data

keep_playing = True

while keep_playing:
    count = 0
    score = 0
    random.shuffle(question_data)

    for count in range(0,1):
        user_answer = input(f"Q{count+1}. {QuizMaster.get_question(question_data,count)} True/False: ")

        answer_check = QuizMaster.answer_checker(question_data, count, user_answer)

        correct_answer = QuizMaster.get_answer(question_data, count)

        score = QuizMaster.score_updater(answer_check, score, correct_answer)

        print(f"Your current score is {score}/{count+1}.")

        count += 1

    play_on = (input("Would you like to play_again? y/n: "))

    if play_on == "n":
        keep_playing = False
        print("Thank you for playing.")
    else:
        replit.clear()

