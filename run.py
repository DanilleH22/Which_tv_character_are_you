import random
import sys
from questions import questions

a_answer = 0
b_answer = 0
c_answer = 0
d_answer = 0
invalid_answer = 0
named = ""


def welcome():
    """
    Collects players name and welcomes them to the quiz.
    """
    global named
    print("\nWelcome, let's find what South Park Character you are.")
    for _ in range(5):
        named = input("\nTo begin, please enter your name: ").capitalize()
        if named.isalpha() is True:
            print(f"\nWelcome {named}.\n")
            break
        elif named.isalpha() is False:
            print("Invalid, only letters are allowed!\n")
    else:
        print("You obviously can't follow simple instructions, goodbye.")
        sys.exit()


def question_answer(questions_dict):
    """
    Prints the questions and answer
    """
    print(questions_dict["question"])
    for answer in questions_dict["answers"]:
        print(answer)


def check_answer():
    """
    collects answer from the user, and checks if it is
    either a,b,c,d and gives a point
    """
    user_answer = input("\nEnter your answer (a, b, c, or d): ").lower()
    if user_answer == 'a':
        global a_answer
        a_answer += 1
    elif user_answer == 'b':
        global b_answer
        b_answer += 2
    elif user_answer == 'c':
        global c_answer
        c_answer += 3
    elif user_answer == 'd':
        global d_answer
        d_answer += 4
    else:
        print("\nInvalid input. Please try again.")
        global invalid_answer
        invalid_answer += 1
        break_check_answer()


def break_check_answer():
    if invalid_answer == 5:
        print(
            "You obviously don't understand how to play the game. " +
            "Goodbye.")
        sys.exit()
    else:
        return check_answer()


def calculate_personality():
    """
    Checks total score to decide which character they are.
    Prints name if certain answers were collected.
    """
    if a_answer > b_answer and a_answer > c_answer and a_answer > d_answer:
        print(f"{named}, based on your results, you are Eric Cartman.\n")
    elif b_answer > a_answer and b_answer > c_answer and b_answer > d_answer:
        print(f"{named}, based on your results, you are Stan Marsh.\n")
    elif c_answer > a_answer and c_answer > b_answer and c_answer > d_answer:
        print(f"{named}, based on your results, you are Kyle Broflovski.\n")
    elif d_answer > a_answer and d_answer > b_answer and d_answer > c_answer:
        print(f"{named}, based on your results, you are Kenny McCormick.\n")
    else:
        print(
            "You have not entered the appropriate answers, please try again."
        )


def repeat_quiz():
    """
    Asks player if they would like to repeat the quiz,
    and repeats if yes
    """
    startOver = input("Would you like to play again, type (yes/no) or (y/n): ")
    if startOver == 'yes' or 'y':
        main_function()
        return startOver
    elif startOver == 'no' or 'n':
        print("Thanks for playing, bye.")
    else:
        print("Invalid Input, game automatically ending.")


def main_function():
    """
    Chooses random questions and answer to ask and uses
    checkanswer function to see how many points to give.
    """
    welcome()
    for _ in range(5):
        random_question = random.choice(questions)
        question_answer(random_question)
        check_answer()
    calculate_personality()
    repeat_quiz()


main_function()
