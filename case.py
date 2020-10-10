from enum import Enum
from math import floor
from column import Column


class CasesTypes(Enum):
    red = '🔴'
    yellow = '🟡'
    blank = '⚫'


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
        if CasesTypes[color_name if color_name else 'blank']:
            self.__color_name = color_name

    @property
    def color(self):
        return CasesTypes[self.color_name if self.color_name else 'blank'].value

    @property
    def empty(self):
        return self.color_name == 'default'

    @property
    def line(self):
        return floor(self.position / self.party.width)

    @property
    def player(self):
        for player in self.party.players:
            if player.color == self.color:
                return player
