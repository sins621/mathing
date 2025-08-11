class InputValidator:
    def is_number(self, value) -> bool:
        try:
            value = int(value)
            return True
        except:
            return False
