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
        """ Class constructor """
        scene.Scene.__init__(self, director)
        self.__past_scene = past_scene
        self.settings = None
        self.__go_back = False
        self.__menu = settings_menu.SettingsMenu(self.director.screen)
        # self.background = pygame.image.load(
        #     os.getcwd()+'/scenes/images/intro.bmp')

    def __go_back(self):
        """ Go back to the scene the Menu was loaded from """
        director.change_scene(self.__past_scene)

    def load_settings(self, settings):
        """ 
        Load the current settings of the game
        and set the widget's values accordingly 
        """
        self.settings = settings
        self.__menu.load_settings(self.settings)

    def on_enter(self):
        """ Actions to perform when entering this scene """
        pass

    def on_event(self, events):
        """ Handle events """
        pass

    def on_update(self):
        """ Update state based on the processed events """
        new_settings = self.__menu()
        self.settings.save_settings(new_settings)
        self.director.change_scene(self.__past_scene, self.settings)
        self.__go_back = False  # reset state

    def on_draw(self, screen):
        """ Draw screen with current status """
        screen.fill(helper.WHITE)
