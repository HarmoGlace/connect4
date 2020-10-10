from case import Case
from player import Player


class Connect4Party:
    def __init__(self, players, height=6, width=7):
        self.players = list(map(lambda player: Player(player['id'], player['case']), players))
        if len(players) <= 1:
            raise Exception(f'Please provide at least two players. Received only {len(players)} player(s)')

        self.height = height
        self.width = width
        self.default_color = '⚫'
        self.cases = list(map(lambda position: Case(self, None, position), range(0, height * width)))

        self.__player_position = 0

    @property
    def full(self):
        return not len(list(filter(lambda case: case.color_name is not None, self.cases)))

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

    def __check_cases__(self, case, condition, increase):
        checks = 0
        index = case.position

        def current_case():
            return self.cases[index]

        while condition(current_case(), checks) & index < len(self.cases):
            if self.cases[index].color_name != case.color_name:
                break

            checks += 1
            index += increase

        return checks >= 4

    @property
    def results(self):

        for case in self.cases:
            # Checks
            if self.__check_cases__(case, lambda check_case: check_case.index <= case.position + 4 and check_case.line == case.line, 1) \
                    or self.__check_cases__(case, lambda check_case: check_case.position <= case.position + (self.width * 4), self.width) \
                    or self.__check_cases__(case, lambda check_case, checks: check_case.position <= case.position + (self.width + 1) * 4 and check_case.line == case.line + checks, self.width - 1) \
                    or self.__check_cases__(case, lambda check_case, checks: check_case.position <= case.position + (self.width + 1) * 4 and check_case.line == case.line + checks, self.width + 1) \
                    :
                return {'finished': True, 'winner': case.player}

        return {'finished': False, 'winner': None}

    def __str__(self):
        lines = self.__list__()
        return '\n'.join(lines)

    def __list__(self):
        lines = []
        for line_number in range(0, self.height):
            lines.append(''.join(list(map(lambda case: case.color if case.color else self.default_color,
                                          self.cases[line_number * self.width: self.width * (line_number + 1)]))))

        lines.reverse()
        return lines
