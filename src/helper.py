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


def draw_empty_board(board_dim, screen, width, height):
    """
    Function that takes a board, a pygame display window, the width and height of the window
    and draws an empty board
    """
    screen.fill(WHITE)
    for line_num in range(1, board_dim):
        # Vertical lines
        pygame.draw.line(screen, BLACK, (line_num*width/board_dim, HEIGHT),
                                        (line_num*width/board_dim, 0), 2)
        # Horizontal lines
        pygame.draw.line(screen, BLACK, (0, line_num*height/board_dim),
                                        (width, line_num*height/board_dim), 2)

def get_square_from_coords(board_dim, x_coord, y_coord):
    return (int(x_coord//(WIDTH/board_dim)), int(y_coord//(HEIGHT/board_dim)))