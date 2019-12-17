# -*- encoding: utf-8 -*-

import pygame
import os
from scenes import scene
from scenes import game_scene
from game_logic import tic_tac_toe_board
from game_logic import helper


class IntroScene(scene.Scene):
    """ Intro scene that shows up when starting the game """

    def __init__(self, director, skip_intro=False):
        scene.Scene.__init__(self, director)
        self.background = pygame.image.load(
            os.getcwd()+'/scenes/images/intro.bmp')
        self.start_game = skip_intro
        # TODO -> make parameters configurable by the player
        # This params go to the settings object
        self.board_dim = 3
        self.starting_player = helper.PLAYERX
        self.player_type = {helper.PLAYERX: helper.HUMAN,
                            helper.PLAYERO: helper.MACHINE}
        self.ntrials = 1000  # the higher the number of trials the better the player will be

    def __start_new_game(self):
        board = tic_tac_toe_board.Board(self.board_dim)
        square_size = helper.WIDTH / board.get_dim(), helper.HEIGHT / board.get_dim()
        font = helper.FONT_TYPE, helper.compute_symbol_font_size(
            helper.FONT_TYPE, helper.TEST_SYMBOL, *square_size)

        return board, font, self.starting_player, self.player_type, self.ntrials

    def read_settings(self, settings):
        self.settings = settings

    def on_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    self.start_game = True

    def on_update(self):
        if self.start_game:
            scene = game_scene.GameScene(
                self.director, *self.__start_new_game())
            self.director.change_scene(scene, self.settings)

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
