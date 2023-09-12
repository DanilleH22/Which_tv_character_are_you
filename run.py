import random
import sys
import pprint

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
        "question": "How do you react to authority figures in your life?",
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
        print("You have not entered the appropriate answers, please try again.")


def repeat_quiz():
    """
    Asks player if they would like to repeat the quiz,
    and repeats if yes
    """
    startOver = input("Would you like to play again, type (yes/no): ")
    if startOver == 'yes':
        main_function()
        return startOver
    elif startOver == 'no':
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