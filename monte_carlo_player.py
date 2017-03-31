"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 100       # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player


def mc_trial(board, player):
    """
    Receives board state and initial player and plays
    a random game.
    """
    while board.check_win() is None: 
        row, col = random.choice(board.get_empty_squares())
        board.move(row, col, player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    Function that updates square scores from a finished game
    """
    if board.check_win() != provided.DRAW:
        score_to_add = {player: SCORE_CURRENT, provided.switch_player(player): SCORE_OTHER}
        dim = board.get_dim()
        all_squares = set((i,j) for i in range(dim) for j in range(dim))
        played_squares = all_squares.difference(set(board.get_empty_squares()))
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
    candidates = [(row, col) for row, col in board.get_empty_squares() if scores[row][col]==max_score]
    return random.choice(candidates)

def mc_move(board, player, trials):
    """
    Function that returns the machine move
    """
    dim = board.get_dim()
    scores = [[0]*dim for dummy_row in range(dim)]
    for dummy_trial in range(trials):
        board_to_play = board.clone()
        mc_trial(board_to_play, player)
        mc_update_scores(scores, board_to_play, player)
    return get_best_move(board, scores)
    
    

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#get_best_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), [[0, 2, 0], [0, 2, 0], [0, 2, 0]])
#get_best_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), [[3, 2, 5], [8, 2, 8], [4, 0, 2]])
#mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, NTRIALS)
provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
