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
LINE_WIDTH = 2
FONT_TYPE = "Verdana"
TEST_SYMBOL = 'X'



def switch_player(player):
    """
    Function that switches whose turn is in the game
    """
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
    return row * WIDTH / board_dim ,col * HEIGHT / board_dim

def compute_symbol_font_size(board_dim, font_type, test_symbol, square_width, square_height):
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
        or  square_height / 4 - delta_h <= square_height - text_height <= square_height / 4 + delta_h:
                return points
        else:
            points += 1


def draw_empty_board(board_dim, screen, width, height):
    """
    Function that takes a board dimension, a pygame display window,
    the width and height of the window and draws an empty board
    """
    screen.fill(WHITE)
    for line_num in range(1, board_dim):
        # Vertical lines
        pygame.draw.line(screen, BLACK, (line_num*width/board_dim, HEIGHT),
                                        (line_num*width/board_dim, 0), LINE_WIDTH)
        # Horizontal lines
        pygame.draw.line(screen, BLACK, (0, line_num*height/board_dim),
                                        (width, line_num*height/board_dim), LINE_WIDTH)


def draw_player_symbol(player, font_def, square_width, square_height):
    """
    Function that returns a pygame surface that contains a drawing of the symbol of the given player
    """
    player_symbol = {PLAYERO: 'O', PLAYERX: 'X'}
    font = pygame.font.SysFont(font_def[0],font_def[1])
    square = pygame.Surface((square_width, square_height), pygame.SRCALPHA, 32)
    square.convert_alpha()
    text = font.render(player_symbol[player], True, BLACK)
    text_width, text_height = text.get_size()
    square.blit(text, ((square_width - text_width) // 2, (square_height - text_height) // 2))
    return square