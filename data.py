class QuizMaster:

    question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
    ]

    def get_question(data, count):
        return (data[count]["text"])

    def get_answer(data, count):
        return (data[count]["answer"])

    def answer_checker(data, count, user_answer):
        if data[count]["answer"] == user_answer:
            return True
        else:
            return False

    def score_updater(answer_check, score, correct_answer):
        if answer_check:
            print("You chose right!")
            print(f"The correct answer was: {correct_answer}.")
            return score+1
        else:
            print ("You chose wrong!")
            print(f"The correct answer was: {correct_answer}.")
            return score
