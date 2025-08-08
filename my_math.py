import random

from validation import validate_number


def is_fives_candidate(num1, num2):
    return (
        abs(num1 % 10 - 5) < 3 and abs(num2 % 10 - 5) < 3 and num1 % 10 + num2 % 10 > 10
    )


def practice_table(min, max):
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)

    answer = num1 * num2
    user_answer = validate_number(input(f"What is {num1} * {num2}?\n\n"))
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Sorry, the correct answer was {answer}")

def practice_addition_and_subtraction(num_digits):
    num1 = random.randint(1, 10 * 10 * num_digits)
    num2 = random.randint(1, 10 * 10 * num_digits)
    practice_routines = [practice_fives]
    routine_to_execute = lambda: random.choice(practice_routines)(num1, num2)
    routine_to_execute()


def practice_fives(num1, num2):
    num1_ten = (num1 // 10) * 10 + 5
    num2_ten = (num2 // 10) * 10 + 5
    remainder = num1 % 10 - 5 + num2 % 10 - 5
    print(num1_ten, num2_ten, remainder)

    _ = validate_number(
        input("Fives: a5 + b5 + c.\nEnter your solution comma seperated\n")
    )
