# -*- encoding: utf-8 -*-

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
from game_logic import helper

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
# NTRIALS = 100      # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0    # Score for squares played by the other player


def mc_trial(board, player):
    """
    Receives board state and initial player and plays
    a random game.
    """
    while board.check_win() is None:
        row, col = random.choice(board.get_empty_squares())
        board.move(row, col, player)
        player = helper.switch_player(player)


def mc_update_scores(scores, board, player):
    """ Function that updates square scores from a finished game """
    # if board.check_win() != helper.DRAW:
    if board.check_win():
        score_to_add = {player: SCORE_CURRENT,
                        helper.switch_player(player): SCORE_OTHER}
        # dim = board.get_dim()
        # all_squares = set((i, j) for i in range(dim) for j in range(dim))
        # played_squares = all_squares.difference(set(board.get_empty_squares()))
        played_squares = board.get_used_squares()
        for row, col in played_squares:
            if board.check_win() == board.square(row, col):
                scores[row][col] += score_to_add[board.square(row, col)]
            else:
                scores[row][col] -= score_to_add[board.square(row, col)]


def get_best_move(board, scores):
    """
    Function that computes the best move for the machine given
    the actual board state
    """
    max_score = max(scores[row][col] for row, col in board.get_empty_squares())
    candidates = [(row, col) for row, col in board.get_empty_squares()
                  if scores[row][col] == max_score]
    return random.choice(candidates)


def mc_move(board, player, trials):
    """ Function that returns the machine move """
    dim = board.get_dim()
    scores = [[0]*dim for dummy_row in range(dim)]
    for dummy_trial in range(trials):
        board_to_play = board.clone()
        mc_trial(board_to_play, player)
        mc_update_scores(scores, board_to_play, player)
    return get_best_move(board, scores)
