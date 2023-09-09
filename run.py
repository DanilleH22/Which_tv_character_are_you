import gspread
import random
from itertools import repeat

a_answer = 0
b_answer = 0
c_answer = 0
d_answer = 0

def welcome_message():
    """
    Collects players name and welcomes them to the quiz.
    """
    print("Welcome to the quiz. This quiz is to tell you which South Park character you are")
    named = input("To begin, please enter your name:")
    print(f"Welcome {named}.")

welcome_message()

"""
Questions to ask user to determine personality
"""
questions = [
    {
        "question": "What's your sense of humor like?",
        "answers": [
            "a. Dark and cynical",
            "b. Sarcastic and witty",
            "c. Outrageously absurd",
            "d. Innocently naive"
        ]
    },
    {
        "question": "How do you handle conflicts with friends?",
        "answers": [
            "a. Manipulate and scheme",
            "b. Be the voice of reason",
            "c. Get caught up in ridiculous adventures",
            "d. Try to keep the peace"
        ]
    },
    {
        "question": "Choose a favorite activity during recess:",
        "answers": [
            "a. Prank others",
            "b. Play sports or games",
            "c. Start a bizarre trend",
            "d. Daydream and imagine fantastical scenarios"
        ]
    },
    {
        "question": "What's your attitude towards authority figures?",
        "answers": [
            "a. Defy and challenge them",
            "b. Respect and obey them",
            "c. Embarrass or mock them",
            "d. Try to please and impress them"
        ]
    },
    {
        "question": "What's your favorite school subject?",
        "answers": [
            "a. None, I hate school",
            "b. Science or math",
            "c. Social studies or current events",
            "d. Art or creative writing "
        ]
    },
    {
        "question": "How do you react to bizarre or supernatural situations?",
        "answers": [
            "a. Embrace them with excitement",
            "b. Investigate them logically",
            "c. Act like a conspiracy theorist",
            "d. Get easily scared and confused"
        ]
    },
    {
        "question": "What's your favorite type of humor?",
        "answers": [
            "a. Offensive and shock humor",
            "b. Satirical and observational humor",
            "c. Absurdist and surreal humor",
            "d. Innocent and slapstick humor"
        ]
    },
    {
        "question": "Choose a hobby:",
        "answers": [
            "a. Collecting and trading items",
            "b. Playing music or an instrument",
            "c. Engaging in strange and quirky hobbies ",
            "d. Doing arts and crafts"
        ]
    },
    {
        "question": "What's your approach to problem-solving?",
        "answers": [
            "a. Manipulate and deceive others",
            "b. Think logically and rationally",
            "c. Make impulsive and questionable decisions",
            "d. Try to follow rules and guidelines"
        ]
    },
    {
        "question": "Choose a role in a group project:",
        "answers": [
            "a. The bossy leader",
            "b. The dependable team player",
            "c. The wildcard who suggests crazy ideas",
            "d. The eager helper who follows instructions"
        ]
    }
]


def question_answer(questions_dict):
    """
    Prints the question
    """
    print(questions_dict["question"])
    """
    Prints question answer
    """
    for answer in questions_dict["answers"]:
        print(answer)


def check_answer():
    """
    collects answer from the user, and checks if it is
    either a,b,c,d and gives a point
    """
    user_answer = input("\n Enter your answer (A, B, C, or D): ").lower()
    if user_answer == 'a':
        global a_answer
        a_answer += 1
        print(a_answer)
    elif user_answer == 'b':
        global b_answer
        b_answer += 2
        print(b_answer)
    elif user_answer == 'c':
        global c_answer
        c_answer += 3
        print(c_answer)
    elif user_answer == 'd':
        global d_answer
        d_answer += 4
        print(d_answer)
    else:
        print("please only type either: a, b, c, d")


def main_function():
    """
    Chooses random questions and answer to ask.
    """
    random_question = random.choice(questions)
    question_answer(random_question)
    check_answer()


def calculate_personality():
    """
    Checks total score to decide which character they are.
    Prints name if certain answers were collected.
    """
    if (a_answer > b_answer, c_answer, d_answer):
        print("You are Cam")
    elif (b_answer > a_answer, c_answer, d_answer):
        print("You are Hayley")
    elif (c_answer > b_answer, a_answer, d_answer):
        print("You are Claire")
    elif (d_answer > b_answer, c_answer, a_answer):
        print("You are Mitchell")


for x in range(5):
    """
    Prints 5 questions to ask before printing personality type
    """
    main_function()

print("Congrats, you have completed the quiz!")
calculate_personality()
