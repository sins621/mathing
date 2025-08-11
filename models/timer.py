import time


class SessionTimer:
    start_time = None
    end_time = None
    duration = None

    def set_practice_duration(self, duration: int) -> int:
        """Set the practice session duration.

        Args:
            duration (int): Duration of practice session in minutes
        """
        self.duration = duration * 60
        return duration

    def start_timer(self) -> float:
        """Start the session timer."""
        self.start_time = time.time()
        return self.start_time

    def is_time_left(self) -> bool:
        """Check if the timer has expired."""
        if self.start_time is None or self.duration is None:
            raise RuntimeError("Session Timer not Started")
        return time.time() - self.start_time < self.duration
