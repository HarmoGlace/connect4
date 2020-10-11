from termcolor import colored


class Player:
    def __init__(self, id, color):
        self.id = id
        self.color = color

    @property
    def colored_name(self):
        return colored(self.id, self.color)
