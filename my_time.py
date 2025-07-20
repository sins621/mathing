import time


def practice_for_duration(duration_minutes: int, exercise):
    duration_seconds = duration_minutes * 60
    start_time = time.time()

    while time.time() - start_time < duration_seconds:
        exercise()

    print("Time's up!")
