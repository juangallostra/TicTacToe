from game_logic import helper


class Settings(object):
    """
    Object to store the current settings
    of the game plus some utility methods
    to make working with the settings easier
    """

    def __init__(self, trials, opponent, player):
        """
        When creating the settings object set
        as initial values the ones passed to 
        the constructor
        """
        self.trials = trials
        self.opponent = opponent
        self.player = player

    def __get_opponent_player(self):
        """
        Get the constant used to know which player
        is the oppponent based on the symbol of the 
        main player            
        """
        return {'X': helper.PLAYERO, 'O': helper.PLAYERX}[self.player]

    def get_trials(self):
        """
        Get the number of trials the Montecarlo algorithm
        will use to get the best play for each turn
        """
        return self.trials

    def get_opponent(self):
        """
        Get the constant that defines which type of payer
        is the opponent
        """
        return {'Human': helper.HUMAN, 'Computer': helper.MACHINE}[self.opponent]

    def get_player(self):
        """
        Get the constant value that represents the main player's
        symbol
        """
        return {'X': helper.PLAYERX, 'O': helper.PLAYERO}[self.player]

    def get_players(self):
        """
        Get the dictionary that relates symbols (X, O) 
        to type of players (Human, Machine)
        """
        return {self.get_player(): helper.HUMAN, self.__get_opponent_player(): self.get_opponent()}

    def save_settings(self, settings):
        """
        Save the settings in the object from the values
        obtained when exiting the settings menu
        """
        self.trials = settings['trials']
        self.opponent = settings['opponent'][0]
        self.player = settings['player'][0]
