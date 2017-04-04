# -*- encoding: utf-8 -*-

import sys
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
    scene = scene_game.SceneGame(dir, board)
    dir.change_scene(scene)
    dir.loop()

if __name__ == '__main__':
    pygame.init()
    main()

# screen = pygame.display.set_mode(helper.SIZE)
# pygame.display.set_caption("Tic Tac Toe")
# helper.draw_empty_board(board.get_dim(), screen, helper.WIDTH, helper.HEIGHT)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
#             x_press, y_press = pygame.mouse.get_pos()
#             row, col = helper.get_square_from_coordinates(board.get_dim(), x_press, y_press)
#             # Remove after testing
#             d = helper.draw_player_symbol(helper.PLAYERX, font, *square_size)
#             screen.blit(d, helper.get_coordinates_from_square(board.get_dim(), row, col))
#     pygame.display.flip()
