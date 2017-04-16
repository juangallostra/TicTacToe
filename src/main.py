# -*- encoding: utf-8 -*-

import pygame
import helper
import TTTboard
import director
import scene_game

pygame.init()

# Game variables
board = TTTboard.TTTBoard(3)
square_size = helper.WIDTH / board.get_dim(), helper.HEIGHT / board.get_dim()
font = helper.FONT_TYPE, helper.compute_symbol_font_size(helper.FONT_TYPE, helper.TEST_SYMBOL, *square_size)


def main():
    dir = director.Director()
    scene = scene_game.SceneGame(dir, board, font, helper.PLAYERX, {helper.PLAYERX: helper.HUMAN,
                                                              helper.PLAYERO: helper.HUMAN}, 1000)
    dir.change_scene(scene)
    dir.loop()

if __name__ == '__main__':
    pygame.init()
    main()