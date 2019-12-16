# -*- encoding: utf-8 -*-

"""
Helper functions and constants
"""
import pygame

SIZE = WIDTH, HEIGHT = 300, 320
LINE_WIDTH = 2
WINNING_LINE_WIDTH = 5
FONT_TYPE = "Verdana"
TEST_SYMBOL = 'X'
GAME_NAME = "Tic Tac Toe"

PLAYERX = 2
PLAYERO = 1
EMPTY = DRAW = 0

MACHINE = 0
HUMAN = 1

BLACK = 0, 0, 0
WHITE = 255, 255, 255


def switch_player(player):
    """ Function that switches whose turn is in the game """
    switch = {PLAYERX: PLAYERO, PLAYERO: PLAYERX}
    return switch[player]


def get_square_from_coordinates(board_dim, x_coord, y_coord):
    """
    Function that given the mouse press coordinates x and y and the board dimensions
    returns the indexes row, col of the square of the board where the mouse was pressed
    """
    return int(x_coord//(WIDTH/board_dim)), int(y_coord//(HEIGHT/board_dim))


def get_coordinates_from_square(board_dim, row, col):
    """
    Function that given a row and a column return the upper left window coordinates of the square
    """
    return row * WIDTH / board_dim, col * HEIGHT / board_dim


def get_center_coordinates_from_square(board_dim, row, col):
    """
    Function that given a row and a column return the middle coordinates of the square
    """
    cell_width = WIDTH / board_dim
    cell_height = HEIGHT / board_dim
    return row * cell_width + cell_width / 2, col * HEIGHT / board_dim + cell_height / 2


def compute_symbol_font_size(font_type, test_symbol, square_width, square_height):
    """
    Function that given a board dimensions and the overall window
    size computes the required size of the symbols to be drawn
    """
    points = 0
    delta_w = square_width / 10   # Width tolerance
    delta_h = square_height / 10  # Height tolerance
    while True:
        font = pygame.font.SysFont(font_type, points)
        text = font.render(test_symbol, True, BLACK)
        text_width, text_height = text.get_size()
        if square_width / 4 - delta_w <= square_width - text_width <= square_width / 4 + delta_w \
                or square_height / 4 - delta_h <= square_height - text_height <= square_height / 4 + delta_h:
            return points
        else:
            points += 1
