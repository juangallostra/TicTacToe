# -*- encoding: utf-8 -*-

# Modules
import pygame
from game_logic import helper


class Director:
    """
    Represents the principal game object.
    Keeps the game alive, actualizes, draws and propagates events
    Requires Scene derived objects to work.
    """

    def __init__(self):
        """
        Class constructor
        """
        self.screen = pygame.display.set_mode(helper.SIZE)
        pygame.display.set_caption(helper.GAME_NAME)
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()

    def loop(self):
        """ 
        main loop that starts the game, processes 
        events and updates the screen accordingly
        """

        while not self.quit_flag:
            time = self.clock.tick(60)
            # Quit events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()

            self.scene.on_event(events)
            self.scene.on_update()
            self.scene.on_draw(self.screen)

            pygame.display.flip()

    def change_scene(self, scene, settings=None):
        """ Change current scene """
        self.scene = scene
        self.scene.load_settings(settings)
        self.scene.on_enter()

    def quit(self):
        """ set flag that signal game exit """
        self.quit_flag = True
