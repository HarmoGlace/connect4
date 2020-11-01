from termcolor import colored

from case import Case
from column import Column
from player import Player


class Connect4Party:
    numbers = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    default_color = '🟢'
    win_cases = 4
    __player_position = 0

    def __init__(self, players, height=6, width=7):
        self.players = list(map(lambda player: Player(player['id'], player['case']), players))
        if len(players) <= 1:
            raise Exception(f'Please provide at least two players. Received only {len(players)} player(s)')

        self.height = height
        self.width = width
        self.cases = list(map(lambda position: Case(self, None, position), range(0, height * width)))

    @property
    def full(self):
        return not len(list(filter(lambda case: case.color_name is None, self.cases)))

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

    def get_column(self, number):
        if number < 0 or number >= self.width: return None
        return Column(self, number)

    def __check_cases__(self, case, condition, increase):
        checks = 0
        index = case.position

        def current_case():
            return self.cases[index]

        while index < len(self.cases) and condition(current_case(), checks, case):
            if self.cases[index].color_name != case.color_name:
                break

            checks += 1
            index += increase

        return checks >= self.win_cases

    @property
    def results(self):

        def linear_check(check_case, checks, base):
            return check_case.position <= case.position + self.win_cases and check_case.line == base.line

        def upward_check(check_case, checks, base):
            return check_case.position <= base.position + (self.width * self.win_cases)

        def diag_left_to_right_check(check_case, checks, base):
            return check_case.position <= base.position + (self.width + 1) * self.win_cases and check_case.line == base.line + checks

        def diag_right_to_left_check(check_case, checks, base):
            return check_case.position <= base.position + (self.width + 1) * self.win_cases and check_case.line == base.line + checks

        for case in self.cases:
            # Checks
            if case.color_name is not None and (self.__check_cases__(case, linear_check, 1) \
                                                or self.__check_cases__(case, upward_check, self.width) \
                                                or self.__check_cases__(case, diag_left_to_right_check, self.width - 1) \
                                                or self.__check_cases__(case, diag_right_to_left_check, self.width + 1)) \
                    :
                return {'finished': True, 'winner': case.player}

        return {'finished': self.full, 'winner': None}

    def __str__(self, *args):
        lines = self.__list__(*args)
        return '\n'.join(lines)

    def __list__(self, numbers=True):
        lines = []
        for line_number in range(0, self.height):
            lines.append(''.join(list(map(lambda case: colored(self.default_color, case.real_color_name),
                                          self.cases[line_number * self.width: self.width * (line_number + 1)]))))

        if numbers:
            indication = ''
            for number in range(1, self.width + 1):
                indication += self.numbers[number]
            lines.append(colored(indication, 'blue'))

        lines.reverse()
        return lines
