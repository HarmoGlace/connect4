class Connect4Party:
    def __init__(self, players, height=6, width=7):
        self.players = list(map(lambda player: player.__str__(), players))
        if len(players) <= 1:
            raise Exception(f'Please provide at least two players. Received only {len(players)} player(s)')

        self.height = height
        self.width = width
        self.__player_position = 0

    @property
    def current_player(self):
        return self.players[self.__check_position(self.__player_position)]

    def __check_position(self, position):
        return position % len(self.players)

    @property
    def results(self):
        return self.data

    def __str__(self):
        return 'lol'
