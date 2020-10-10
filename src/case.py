from enum import Enum
from math import floor
from src.column import Column


class CasesTypes(Enum):
    red = '🔴'
    yellow = '🟡'
    white = '⚫'


class Case:
    def __init__(self, party, color, position=0):
        self.party = party
        self.color_name = color
        self.position = position
        self.column = Column(party, self.position % party.width)

    @property
    def color_name(self):
        return self.__color_name

    @color_name.setter
    def color_name(self, color_name):
        if CasesTypes[color_name if color_name else 'white']:
            self.__color_name = color_name

    @property
    def real_color_name(self):
        return self.color_name if self.color_name else 'white'

    @property
    def color(self):
        return CasesTypes[self.real_color_name].value

    @property
    def empty(self):
        return self.color_name is None

    @property
    def line(self):
        return floor(self.position / self.party.width)

    @property
    def player(self):
        for player in self.party.players:
            if player.color == self.real_color_name:
                return player
