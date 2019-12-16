# -*- encoding: utf-8 -*-

import pygame
import time
from scenes import scene
from scenes import intro_scene
from game_logic import helper
from game_logic import monte_carlo_player as mc


class GameScene(scene.Scene):
    """ Game scene that shows up when a game is active and running """

    def __init__(self, director, board, font, initial_turn, players, ntrials):
        scene.Scene.__init__(self, director)
        self.board = board
        self.font = font
        self.__draw_empty_board(self.board.get_dim(
        ), self.director.screen, helper.WIDTH, helper.HEIGHT)
        self.turn = initial_turn
        self.players = players
        self.trials = ntrials
        self.move = None
        self.winner = None

    def __draw_empty_board(self, board_dim, screen, width, height):
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

    def __draw_player_symbol(self, player, square_width, square_height):
        """
        Function that returns a pygame surface that contains a drawing of the symbol of the given player
        """
        player_symbol = {helper.PLAYERO: 'O', helper.PLAYERX: 'X'}
        font = pygame.font.SysFont(*self.font)
        square = pygame.Surface(
            (square_width, square_height), pygame.SRCALPHA, 32)
        square.convert_alpha()
        text = font.render(player_symbol[player], True, helper.BLACK)
        text_width, text_height = text.get_size()
        square.blit(text, ((square_width - text_width) /
                           2, (square_height - text_height) / 2))
        return square

    def __restart_game(self):
        time.sleep(1)
        scene = intro_scene.IntroScene(self.director, start_game=True)
        self.director.change_scene(scene)

    def on_event(self, events):
        if self.winner is not None:
            self.__restart_game()
            return
        if self.players[self.turn] == helper.HUMAN:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    x_coord, y_coord = pygame.mouse.get_pos()
                    row, col = helper.get_square_from_coordinates(
                        self.board.get_dim(), x_coord, y_coord)
                    if (row, col) in self.board.get_empty_squares():
                        self.move = (row, col)
        else:
            self.move = mc.mc_move(self.board, self.turn, self.trials)

    def on_update(self):
        if self.move is not None:
            self.board.move(self.move[0], self.move[1], self.turn)
            self.turn = helper.switch_player(self.turn)
            self.move = None
        self.winner = self.board.check_win()

    def on_draw(self, screen):
        # draw move
        for row, col in self.board.get_used_squares():
            tile = self.__draw_player_symbol(self.board.square(row, col), helper.WIDTH/self.board.get_dim(),
                                             helper.HEIGHT/self.board.get_dim())
            screen.blit(tile, helper.get_coordinates_from_square(
                self.board.get_dim(), row, col))
        # If there is a winner,draw winning combination
        if self.winner in [helper.PLAYERX, helper.PLAYERO]:
            color_line = (255, 0, 0)
            line_points = [helper.get_center_coordinates_from_square(
                self.board.get_dim(), *cell) for cell in self.board.winning_combination]
            pygame.draw.line(
                screen, color_line, line_points[0], line_points[2], helper.WINNING_LINE_WIDTH)
