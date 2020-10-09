from enum import Enum
from math import floor


class CasesTypes(Enum):
    red = ''
    yellow = ''
    default = '⚫'


class Case:
    def __init__(self, party, color, position=0):
        self.party = party
        self.color_name = color
        self.position = position

    @property
    def color(self):
        return CasesTypes(self.color_name if self.color_name else 'default')

    @property
    def empty(self):
        return self.color_name == 'default'

    @property
    def line(self):
        return floor(self.position / self.party.width)

    @property
    def player(self):
        for player in self.party.players:
            if player.case.position == self.position:
                return player
