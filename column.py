class Column:
    def __init__(self, party, number):
        self.party = party
        self.number = number

    @property
    def cases(self):
        return list(filter(lambda case: case.column.number == self.number, self.party.cases))

    @property
    def blank_cases(self):
        return list(filter(lambda case: case.color_name is None, self.cases))

    @property
    def filled_cases(self):
        return list(filter(lambda case: case.color_name is not None, self.cases))

    @property
    def full(self):
        return len(list(filter(lambda case: case.color_name is None, self.cases))) == 0

    def add_piece(self, color_name):
        if self.full: return False

        to_add = self.blank_cases[0]
        to_add.color_name = color_name
        return True
