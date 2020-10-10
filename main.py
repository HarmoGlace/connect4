from connect4 import Connect4Party

party = Connect4Party([{'id': 'lol', 'case': 'red'}, {'id': 'another', 'case': 'yellow'}])

print(party.__str__())

print(party.results)

print()

for case in party.get_column(0).cases:
    print(case.position)
