"""
Helper functions and constants
"""
import pygame

PLAYERX = 2
PLAYERO = 1
EMPTY = DRAW = 0
BLACK = 0, 0, 0
WHITE = 255, 255, 255
SIZE = WIDTH, HEIGHT = 300, 320


def switch_player(player):
    """
    Function that switches whose turn is in the game
    """
    switch = {PLAYERX: PLAYERO, PLAYERO: PLAYERX}
    return switch[player]



def draw_empty_board(board, screen, width, height):
    """
    Function that takes a board, a pygame display window, the width and height of the window
    and draws an empty board
    """
    screen.fill(WHITE)
    for line_num in range(1,board.get_dim()):
        pygame.draw.line(screen, BLACK, (line_num*width/board.get_dim(), HEIGHT), (line_num*width/board.get_dim(), 0), 2)
        pygame.draw.line(screen, BLACK, (0, line_num*height/board.get_dim()), (width, line_num*height/board.get_dim()), 2)