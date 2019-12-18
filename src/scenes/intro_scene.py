# -*- encoding: utf-8 -*-

import pygame
import os
from scenes import scene, game_scene, settings_scene
from game_logic import tic_tac_toe_board
from game_logic import helper


class IntroScene(scene.Scene):
    """ Intro scene that shows up when starting the game """

    def __init__(self, director):
        scene.Scene.__init__(self, director)
        self.background = pygame.image.load(
            os.getcwd()+'/scenes/images/intro.bmp')
        self.start_game = False
        self.go_to_settings = False
        self.settings = None

    def load_settings(self, settings):
        self.settings = settings

    def on_enter(self):
        pass

    def on_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    self.start_game = True
                if event.key == pygame.K_s:
                    self.go_to_settings = True

    def on_update(self):
        if self.start_game:
            scene = game_scene.GameScene(self.director)
            self.director.change_scene(scene, self.settings)
            self.start_game = False  # reset state
        if self.go_to_settings:
            scene = settings_scene.SettingsScene(
                self.director, self
            )
            self.director.change_scene(scene, self.settings)
            self.go_to_settings = False  # reset state

    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
