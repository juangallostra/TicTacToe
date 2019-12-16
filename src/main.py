# -*- encoding: utf-8 -*-

import pygame
from scenes import director
from scenes import intro_scene

pygame.init()


def main():
    game_director = director.Director()
    scene = intro_scene.IntroScene(game_director)
    game_director.change_scene(scene)
    game_director.loop()


if __name__ == '__main__':
    pygame.init()
    main()
