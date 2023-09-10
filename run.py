import gspread
import random
import sys

a_answer = 0
b_answer = 0
c_answer = 0
d_answer = 0


"""
Collects players name and welcomes them to the quiz.
"""
print("Welcome, this quiz is to tell you which South Park character you are\n")
named = input("To begin, please enter your name: ").capitalize()
if named.isalpha() is False:
    print("Invalid, only letters are allowed!")
    sys.exit()
else:
    print(f"\nWelcome {named}.\n")


"""
Questions to ask user to determine personality
"""
questions = [
    {
        "question": "What's your sense of humor like?",
        "answers": [
            "a. Sarcastic",
            "b. Slapstick",
            "c. Witty",
            "d. Dark and twisted"
        ]
    },
    {
        "question": "What's your preferred mode of transportation?",
        "answers": [
            "a. Car",
            "b. Walking",
            "c. Bicycle",
            "d. Public Transport"
        ]
    },
    {
        "question": "Choose a recreational activity:",
        "answers": [
            "a. Playing video games",
            "b. Fishing",
            "c. Skiing/snowboarding",
            "d. Karaoke"
        ]
    },
    {
        "question": "What's your favorite food?",
        "answers": [
            "a. Pizza",
            "b. Tacos",
            "c. Burgers",
            "d. Sushi"
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
        "question": "How do you handle conflict?",
        "answers": [
            "a. Confront it head-on",
            "b. Avoid it at all costs",
            "c. Seek mediation and compromise",
            "d. Use humor to defuse tension "
        ]
    },
    {
        "question": "Pick a holiday destination:",
        "answers": [
            "a. Beach resort",
            "b. Cultural city",
            "c. Ski resort",
            "d. Remote wilderness"
        ]
    },
    {
        "question": "What's your stance on authority figures?",
        "answers": [
            "a. Challenge and question ",
            "b. Respect and Obey",
            "c. Make fun of them",
            "d. Ignore them"
        ]
    },
    {
        "question": "How do you feel about school/work?",
        "answers": [
            "a. Try to follow rules and guidelines",
            "b. Enjoy it",
            "c. Tolerate it",
            "d. Dread it"
        ]
    },
    {
        "question": "What type of pet would you prefer?",
        "answers": [
            "a. Snake",
            "b. Dog",
            "c. Cat",
            "d. Hamster"
        ]
    },
    {
        "question": "What's your favorite TV show genre?",
        "answers": [
            "a. Science fiction",
            "b. Comedy",
            "c. Drama",
            "d. Horror"
        ]
    },
    {
        "question": "What's your preferred way to express your feelings?",
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
            "a. Through outbursts and tantrums",
            "b. Through art",
            "c. Through speeches and activism",
            "d. Through music"
        ]
    },
    {
        "question": "Pick a favorite subject in school:",
        "answers": [
            "a. Lunchtim",
            "b. English adn Writing",
            "c. math",
            "d. Recess"
        ]
    },
    {
        "question": "Choose a superpower:",
        "answers": [
            "a. Super strength",
            "b. Telepaths",
            "c. Invisibility",
            "d. Immortal "
        ]
    },
    {
        "question": "ow do you react to authority figures in your life?",
        "answers": [
            "a. Rebel and question their authority",
            "b. Follow their rules and advice",
            "c. Seek their approval",
            "d. Ignore them and do your own thing"
        ]
    },
    {
        "question": "What's your favorite way to spend free time?",
        "answers": [
            "a. Playing video games",
            "b. Hanging out with friends",
            "c. Reading books",
            "d. Going on adventures"
        ]
    },
    {
        "question": "Pick a favorite South Park episode:",
        "answers": [
            "a. Scott Tenorman Must Die",
            "b. Make Love, Not Warcraft",
            "c. Imaginationland",
            "d. The Coon"
        ]
    },
    {
        "question": "What's your approach to problem-solving?",
        "answers": [
            "a. Manipulate and deceive others",
            "b. Make inpulsive decisions",
            "c. Try to follow rules and guidelines",
            "d. Think logically and rationally"
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
        input("\nInvalid input. Please only type either a, b, c, or d: ")
        if user_answer == 'a':
            a_answer += 1
            print("\nThank you.\n")
        elif user_answer == 'b':
            b_answer += 2
            print("\nThank you.\n")
        elif user_answer == 'c':
            c_answer += 3
            print("\nThank you.\n")
        elif user_answer == 'd':
            d_answer += 4
            print("\nThank you.\n")
        else:
            print("\nInvalid input.\n")


def main_function():
    """
    Chooses random questions and answer to ask and uses checkanswer function
    to see how many points to give.
    """
    random_question = random.choice(questions)
    question_answer(random_question)
    check_answer()


def calculate_personality():
    """
    Checks total score to decide which character they are.
    Prints name if certain answers were collected.
    """
    if a_answer > b_answer and a_answer > c_answer and a_answer > d_answer:
        print(f"{named}, based on your results, you are Eric Cartman.")
    elif b_answer > a_answer and b_answer > c_answer and b_answer > d_answer:
        print(f"{named}, based on your results, you are Stan Marsh.")
    elif c_answer > a_answer and c_answer > b_answer and c_answer > d_answer:
        print(f"{named}, based on your results, you are Kyle Broflovski.")
    elif d_answer > a_answer and d_answer > b_answer and d_answer > c_answer:
        print(f"{named}, based on your results, you are Kenny McCormick.")
    else:
        print("You have not entered the appropriate answers, please try again.")


for x in range(5):
    """
    Prints 5 questions and answer to ask before printing personality type
    """
    main_function()


calculate_personality()

# Repeats quiz - when function. completes doesn't repeat


def repeat_quiz():
    startOver = input("Would you like to play again, type (yes/no):")
    if startOver == 'yes':
        for x in range(5):
            main_function()
        calculate_personality()
        startOver
    else:
        print("Thanks for playing, bye.")


repeat_quiz()

# To do
# 1. Deploy
# 2. Complete readme
# 3. put in python validator
