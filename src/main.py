from connect4 import Connect4Party
from termcolor import colored
from argparse import ArgumentParser
from os import system, name
import ctypes


def clear_console():
    return system('cls' if name == 'nt' else 'clear')


if name == 'nt':
    ctypes.windll.kernel32.SetConsoleTitleW("Connect4 Party - HarmoGlace")

parser = ArgumentParser()
parser.add_argument('--hide-lines', '--h-d', dest='hide_lines', action='store_const',
                    const=True, default=True,
                    help='Will only use alphanumeric characters. Note that the terminal needs to support colors')

parser.add_argument('--h', '--height', dest='height', default=6,
                    help='Change the height of the connect 4 grid')

parser.add_argument('--w', '--width', dest='width', default=7,
                    help='Change the width of the connect 4 grid')

parser.add_argument('--wc', '--win-cases', '--win-case', dest='win_cases', default=4, help='Change the default cases '
                                                                                           'needed to win')

args = parser.parse_args()
dimensions = {'height': None, 'width': None}

try:
    dimensions['height'] = int(args.height)
    dimensions['width'] = int(args.width)
    if dimensions['height'] <= 0 or dimensions['width'] <= 0:
        raise ValueError('Height and with arguments need to be positive integers.')
except ValueError:
    print(f'Invalid width or height argument. Please provide a valid positive integer')
    exit(1)

win_cases = None
try:
    win_cases = int(args.win_cases)
    if not 1 < win_cases <= min(dimensions['width'], dimensions['height']):
        raise ValueError('win-cases argument need to be a positive integer less or equal to width and height')
except ValueError:
    print('Please provided a valid win cases positive integer, less or equal to width and height')
    exit(1)

clear_console()

player1 = None

while player1 is None or not player1.strip():
    player1 = input('Please provide the first player name: ')

player2 = None

while player2 is None or not player2.strip():
    given = input('Please provide the second player name: ')
    if given == player1:
        print(colored('This name is already used by the first player. Please choose another name.', 'red'))
        continue
    player2 = given

party = Connect4Party([{'id': player1, 'case': 'red'}, {'id': player2, 'case': 'yellow'}], height=dimensions['height'],
                      width=dimensions['width'], win_cases=win_cases)


def print_colors():
    players = ', '.join(
        list(map(lambda player: colored(f'{player.id}: {party.default_case}', player.color), party.players)))
    return print(players)


clear_console()

while not party.results['finished']:
    print(party)
    print_colors()

    current_player = party.current_player
    raw_column_number = input(
        f'{colored(current_player.id, current_player.color)}, enter the column number you want to add your piece now: ')

    try:
        column_number = int(raw_column_number) - 1
    except ValueError:
        clear_console()
        print(colored('Please provide a valid column number.', 'red'))
        continue

    column = party.get_column(column_number)

    if not column:
        clear_console()
        print(colored('Please provide a valid column number.', 'red'))
        continue

    added = column.add_piece(current_player.color)

    if not added:
        clear_console()
        print(colored('This column is full. Please provide another column number.', 'red'))
        continue

    party.increment_player()
    clear_console()

print(party.__str__())
print_colors()
winner = party.results['winner']
name = winner.colored_name if winner is not None else 'nobody'
print(colored(f'The party is finished!\nThe winner is {name}', 'green'))
