import gspread
import random

a_answer = 0
b_answer = 0
c_answer = 0
d_answer = 0

"""
Questions to ask user to determine personality
"""
question = {
    "question": "What is your ideal weekend activity?",
    "answers": [
        "a. Binge-watching a new TV series or movie",
        "b. Going on an outdoor adventure",
        "c. Attending a social event or party",
        "d. Exploring new art galleries and exhibitions"
    ]
}
"""
Prints the question
"""
print(question["question"])

"""
Prints answer
"""
for answer in question["answers"]:
        print(answer)

def pick_random_question():
    """
    collects answer from the user, and checks if it is 
    either a,b,c,d
    """
    user_answer = input("Enter your answer (A, B, C, or D): ").lower()
    print(user_answer)

    if user_answer in ['a', 'b', 'c', 'd']:
        print("complted")
    else:
        print("please type either: a, b, c, d")

pick_random_question()