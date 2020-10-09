from connect4 import Connect4Party

party = Connect4Party([{'id': 'lol', 'case': 'red'}, {'id': 'another', 'case': 'yellow'}])

print(party.__str__())

print(party.results)
