from connect4 import Connect4Party

party = Connect4Party([{'id': 'lol', 'case': 'red'}, {'id': 'another', 'case': 'yellow'}])

print(party.__str__())

print(party.results)

column = party.get_column(0)

print(column.full)

for case in column.cases:
    print(case.position)
