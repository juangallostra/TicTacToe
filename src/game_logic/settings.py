from game_logic import helper


class Settings(object):
    def __init__(self, trials, opponent, player):
        self.trials = trials
        self.opponent = opponent
        self.player = player

    def __get_opponent_player(self):
        return {'X': helper.PLAYERO, 'O': helper.PLAYERX}[self.player]

    def get_trials(self):
        return self.trials

    def get_opponent(self):
        return {'Human': helper.HUMAN, 'Computer': helper.MACHINE}[self.opponent]

    def get_player(self):
        return {'X': helper.PLAYERX, 'O': helper.PLAYERO}[self.player]

    def get_players(self):
        return {self.get_player(): helper.HUMAN, self.__get_opponent_player(): self.get_opponent()}

    def save_settings(self, settings):
        self.trials = settings['trials']
        self.opponent = settings['opponent'][0]
        self.player = settings['player'][0]