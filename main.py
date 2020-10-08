from connect4 import Connect4Party

lol = { 'mdr': 3 }

print(lol)

party = Connect4Party(['premier', 'deuxieme'])

print(party.current_player, party.next_player)

party.increment_player()

print(party.current_player, party.next_player)