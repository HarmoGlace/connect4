from connect4 import Connect4Party
from os import system, name


def clear_console():
    return print('\n'*100)


player1 = input('Please provide the first player name: ')
player2 = input('Please provide the second player name: ')

party = Connect4Party([{'id': player1, 'case': 'red'}, {'id': player2, 'case': 'yellow'}])

while not party.results['finished']:
    clear_console()
    print(party.__str__())
    current_player = party.current_player
    raw_column_number = input(f'{current_player.id}, play now! ')

    try:
        column_number = int(raw_column_number) - 1
    except:
        print('Please provide a valid column number')
        continue

    column = party.get_column(column_number)

    if not column:
        print('Please provide a valid column number!')
        continue

    column.add_piece(current_player.color)

    party.increment_player()

clear_console()
print(party.__str__())
winner = party.results['winner']
name = winner.id if winner is not None else 'nobody'
print('The party is finished!')
print(f'The winner is {name}')
