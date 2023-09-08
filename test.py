import gspread
import random



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

a_answer = []
b_answer = []
c_answer = []
d_answer = []

def check_answer():
    """
    collects answer from the user, and checks if it is
    either a,b,c,d
    """
    user_answer = input("Enter your answer (A, B, C, or D): ").lower()

    if user_answer in ['a', 'b', 'c', 'd']:
        if a_answer == 'a':
            a_answer += 1
            print(a_answer)
        elif b_answer == 'b':
            b_answer += 1
            print(b_answer)
        elif c_answer == 'c':
            c_answer += 1
            print(c_answer)
        elif d_answer == 'd':
            d_answer += 1
            print(d_answer)
    else:
        print("please type either: a, b, c, d")


def main_function():
    random_question = random.choice(questions)
    question_answer(random_question)
    check_answer()
    
main_function()