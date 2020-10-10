class Column:
    def __init__(self, party, number):
        self.party = party
        self.number = number

    @property
    def cases(self):
        return list(filter(lambda case: case.column.number == self.number, self.party.cases))