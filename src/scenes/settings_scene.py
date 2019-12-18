# -*- encoding: utf-8 -*-

import pygame
import pygameMenu
import os
from scenes import scene, game_scene, intro_scene
from game_logic import tic_tac_toe_board, settings_menu
from game_logic import helper


class SettingsScene(scene.Scene):
    """ Settings scene that enables configuring the game """

    def __init__(self, director, past_scene):
        scene.Scene.__init__(self, director)
        self.__past_scene = past_scene
        self.settings = None
        self.__go_back = False
        self.__menu = settings_menu.SettingsMenu(self.director.screen)
        # self.background = pygame.image.load(
        #     os.getcwd()+'/scenes/images/intro.bmp')

    def __go_back(self):
        director.change_scene(self.__past_scene)

    def read_settings(self, settings):
        self.settings = settings

    def on_event(self, events):
        pass

    def on_update(self):
        self.__menu()
        self.director.change_scene(self.__past_scene, self.settings)
        self.__go_back = False  # reset state

    def on_draw(self, screen):
        screen.fill(helper.WHITE)
        #screen.blit(self.background, (0, 0))
