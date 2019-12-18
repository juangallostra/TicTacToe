from game_logic import helper


class Settings(object):
    def __init__(self, trials, oponent, player):
        self.trials = trials
        self.oponent = oponent
        self.player = player

    def __get_oponent_player(self):
        return {'X': helper.PLAYERO, 'O': helper.PLAYERX}[self.player]

    def get_trials(self):
        return self.trials

    def get_oponent(self):
        return {'Human': helper.HUMAN, 'Computer': helper.MACHINE}[self.oponent]

    def get_player(self):
        return {'X': helper.PLAYERX, 'O': helper.PLAYERO}[self.player]

    def get_players(self):
        return {self.get_player(): helper.HUMAN, self.__get_oponent_player(): self.get_oponent()}

    def save_settings(self, settings):
        self.trials = settings['trials']
        self.oponent = settings['oponent'][0]
        self.player = settings['player'][0]