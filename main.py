from connect4 import Connect4Party

party = Connect4Party([{'id': 'lol', 'case': 'red'}, {'id': 'another', 'case': 'yellow'}])

while not party.results['finished']:
    print(party.__str__())
    current_player = party.current_player
    column_number = int(input(f'{current_player.id}, play now! '))

    party.get_column(column_number).add_piece(current_player.color)
    party.increment_player()