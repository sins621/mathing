def choice_is_number(value) -> bool:
    try:
        value = int(value)
        return True
    except:
        return False


def validate_number(value) -> int:
    while not choice_is_number(value):
        value = input("Sorry, you didn't input a valid option, try again.\n\n")
    return int(value)
