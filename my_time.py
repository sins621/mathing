import time


def practice_for_duration(duration_minutes: int, exercise):
    duration_seconds = duration_minutes * 60
    start_time = time.time()
    questions_asked = 0
    correct_answers = 0

    while time.time() - start_time < duration_seconds:
        if exercise():
            correct_answers += 1
        questions_asked += 1

    return questions_asked, correct_answers
