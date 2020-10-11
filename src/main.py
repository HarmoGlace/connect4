from connect4 import Connect4Party
from termcolor import colored
from argparse import ArgumentParser
from os import system, name

parser = ArgumentParser()
parser.add_argument('--u', '--unicode', dest='unicode', action='store_const',
                    const=True, default=False,
                    help='sum the integers (default: find the max)')

unicode = parser.parse_args().unicode


def clear_console():
    return system('cls' if name == 'nt' else 'clear')


clear_console()

player1 = None

while player1 is None or player1.strip() == '':
    player1 = input('Please provide the first player name: ')

player2 = None

while player2 is None or player2.strip() == '':
    given = input('Please provide the second player name: ')
    if given == player1:
        print(colored('This name is already used by the first player. Please choose another name!', 'red'))
        continue
    player2 = given

party = Connect4Party([{'id': player1, 'case': 'red'}, {'id': player2, 'case': 'yellow'}])

if unicode:
    party.default_color = '0'
    party.numbers = []
    for number in range(0, 9):
        party.numbers.append(number.__str__())


def print_colors():
    players = ', '.join(list(map(lambda player: colored(f'{player.id}: {party.default_color}', player.color), party.players)))
    return print(players)


clear_console()

while not party.results['finished']:
    print(party.__str__())
    print_colors()

    current_player = party.current_player
    raw_column_number = input(
        f'{colored(current_player.id, current_player.color)}, enter the column number you want to add your piece now! ')

    try:
        column_number = int(raw_column_number) - 1
    except:
        clear_console()
        print(colored('Please provide a valid column number.', 'red'))
        continue

    column = party.get_column(column_number)

    if not column:
        clear_console()
        print(colored('Please provide a valid column number.', 'red'))
        continue

    added = column.add_piece(current_player.color)
    print(added)

    if not added:
        clear_console()
        print(colored('This column is full. Please provide another column number.', 'red'))
        continue

    party.increment_player()
    clear_console()

clear_console()
print(party.__str__())
print_colors()
winner = party.results['winner']
name = winner.id if winner is not None else 'nobody'
print('The party is finished!')
print(f'The winner is {name}')
