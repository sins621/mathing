import random

from validation import validate_number


def practice_table(min, max):
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)

    answer = num1 * num2
    user_answer = validate_number(input(f"What is {num1} * {num2}?\n\n"))
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Sorry, the correct answer was {answer}")
