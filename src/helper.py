"""
Helper functions and constants
"""

PLAYERX = 2
PLAYERO = 1
EMPTY = DRAW = 0


def switch_player(player):
    """
    Function that switches whose turn is in the game
    """
    switch = {PLAYERX: PLAYERO, PLAYERO: PLAYERX}
    return switch[player]
