# -*- encoding: utf-8 -*-

import scene
import helper
import pygame

class SceneGame(scene.Scene):
    """Game scene that shows up when a game is active and running"""

    def __init__(self, director, board):
        scene.Scene.__init__(self, director)
        self.board = board

    def draw_empty_board(self, board_dim, screen, width, height):
        """
        Function that takes a board dimension, a pygame display window,
        the width and height of the window and draws an empty board
        """
        screen.fill(helper.WHITE)
        for line_num in range(1, board_dim):
            # Vertical lines
            pygame.draw.line(screen, helper.BLACK, (line_num * width / board_dim, helper.HEIGHT),
                             (line_num * width / board_dim, 0), helper.LINE_WIDTH)
            # Horizontal lines
            pygame.draw.line(screen, helper.BLACK, (0, line_num * height / board_dim),
                             (width, line_num * height / board_dim), helper.LINE_WIDTH)

    def draw_player_symbol(self, player, font_def, square_width, square_height):
        """
        Function that returns a pygame surface that contains a drawing of the symbol of the given player
        """
        player_symbol = {helper.PLAYERO: 'O', helper.PLAYERX: 'X'}
        font = pygame.font.SysFont(*font_def)
        square = pygame.Surface((square_width, square_height), pygame.SRCALPHA, 32)
        square.convert_alpha()
        text = font.render(player_symbol[player], True, helper.BLACK)
        text_width, text_height = text.get_size()
        square.blit(text, ((square_width - text_width) / 2, (square_height - text_height) / 2))
        return square

    def on_update(self):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen):
        board = self.draw_empty_board(self.board.get_dim(), self.director.screen, helper.WIDTH, helper.HEIGHT)

