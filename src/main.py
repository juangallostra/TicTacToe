# -*- encoding: utf-8 -*-

import pygame
from scenes import director
from scenes import intro_scene
from game_logic import settings

pygame.init()


def main():
    initial_settings = settings.Settings(
        trials=1000, player='O', opponent='Computer')
    game_director = director.Director()
    scene = intro_scene.IntroScene(game_director)
    game_director.change_scene(scene, initial_settings)
    game_director.loop()


if __name__ == '__main__':
    pygame.init()
    main()
