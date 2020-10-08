from case import Case

class Connect4Party:
    def __init__(self, players, height=6, width=7):
        self.players = list(map(lambda player: player.__str__, players))
        if len(players) <= 1:
            raise Exception(f'Please provide at least two players. Received only {len(players)} player(s)')

        self.height = height
        self.width = width
        self.default_color = '⚫'
        self.cases = list(map(lambda position: Case(None, position), range(0, height * width - 1)))

        self.__player_position = 0

    @property
    def current_player(self):
        return self.players[self.__check_position(self.__player_position)]

    @property
    def next_player(self):
        return self.players[self.__check_position(self.__player_position + 1)]

    def __check_position(self, position):
        return position % len(self.players)

    def increment_player(self):
        self.__player_position = self.__check_position(self.__player_position + 1)
        return self.current_player

    @property
    def results(self):
        return ''

    def __str__(self):
        lines = []
        for line_number in range(0, self.height - 1):
            lines.append(''.join(list(map(lambda case: case.color if case.color else self.default_color, self.cases[line_number * self.width: self.width * (line_number + 1)]))))



        return '\n'.join(list(lines))
