class NotFound(Exception):
    def __init__(self):
        super().__init__("Not Found")


class TooManyArguments(Exception):
    def __init__(self):
        super().__init__("Too many arguments")
