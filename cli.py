from my_math import practice_addition_and_subtraction, practice_table
from my_time import practice_for_duration
from validation import validate_number


def start_practice():
    choice = validate_number(
        input(
            "What would you like to practice?\n1: Times Tables\n2: Addition & Subtraction\n\n"
        )
    )

    duration = validate_number(input("How long would you like to practice for?\n\n"))

    match choice:
        case 1:
            min_val = validate_number(
                input("What's the minimum number for the tables?\n\n")
            )
            max_val = validate_number(
                input("What's the maximum number for the tables?\n\n")
            )
            practice_function = lambda: practice_table(min_val, max_val)
            questions_asked, correct_answers = practice_for_duration(
                duration, practice_function
            )
            print(f"You got {correct_answers}/{questions_asked} correct!")
        case 2:
            n_digits = validate_number(
                input("How many digits large should the number be?\n\n")
            )
            practice_function = lambda: practice_addition_and_subtraction(n_digits)
            questions_asked, correct_answers = practice_for_duration(
                duration, practice_function
            )
            print(f"You got {correct_answers}/{questions_asked} correct!")
        case _:
            print("Not an option")

    print("See you later")
