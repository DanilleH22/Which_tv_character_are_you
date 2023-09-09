import gspread
import random
from itertools import repeat

a_answer = 0
b_answer = 0
c_answer = 0
d_answer = 0

def welcome_message():
    print("Welcome to the quiz. This quiz is to tell you which South Park character you are")
    named = input("To begin, please enter your name:")
    print(f"Welcome {named}.")

welcome_message()

"""
Questions to ask user to determine personality
"""
questions = [
    {
        "question": "What is your ideal weekend activity?",
        "answers": [
            "a. Binge-watching a new TV series or movie",
            "b. Going on an outdoor adventure",
            "c. Attending a social event or party",
            "d. Exploring new art galleries and exhibitions"
        ]
    },
    {
        "question": "How do you handle stress?",
        "answers": [
            "a. I prefer to meditate and practice mindfulness",
            "b. I take action and tackle the source of stress head-on",
            "c. I rely on the support and advice of friends and family",
            "d. I express myself through creative outlets like writing or painting"
        ]
    },
    {
        "question": "Choose a favorite fictional world:",
        "answers": [
            "a. Middle-earth (The Lord of the Rings)",
            "b. The Wizarding World (Harry Potter)",
            "c. Westeros (Game of Thrones)",
            "d. The Marvel Cinematic Universe (MCU)"
        ]
    },
    {
        "question": "What's your go-to social media platform?",
        "answers": [
            "a. Instagram",
            "b. Twitter",
            "c. Facebook",
            "d. TikTok"
        ]
    },
    {
        "question": "Pick a superpower:",
        "answers": [
            "a. Invisibility",
            "b. Super strength",
            "c. Mind reading",
            "d. Time manipulation"
        ]
    },
    {
        "question": "Which genre of music resonates with you the most?",
        "answers": [
            "a. Pop",
            "b. Rock",
            "c. Hip-hop/Rap",
            "d. Indie/Alternative"
        ]
    },
    {
        "question": "How do you approach problem-solving?",
        "answers": [
            "a. Careful planning and analysis",
            "b. Trusting my instincts and taking risks",
            "c. Seeking advice and input from others",
            "d. Thinking outside the box and embracing creativity"
        ]
    },
    {
        "question": "What's your ideal vacation destination?",
        "answers": [
            "a. A serene beach resort",
            "b. A bustling city with lots to explore",
            "c. A remote mountain cabin",
            "d. A culturally rich and historic town"
        ]
    },
    {
        "question": "What's your favorite way to spend a rainy day?",
        "answers": [
            "a. Reading a good book or watching a movie",
            "b. Going for a long drive or walk",
            "c. Hosting a game night with friends",
            "d. Trying out new recipes and cooking"
        ]
    },
    {
        "question": "When it comes to fashion, which style do you prefer?",
        "answers": [
            "a. Classic and timeless",
            "b. Edgy and bold",
            "c. Trendy and fashionable",
            "d. Eclectic and unique"
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
