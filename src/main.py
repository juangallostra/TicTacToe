import sys, pygame
import helper
import TTTboard


pygame.init()

screen = pygame.display.set_mode(helper.SIZE)
board = TTTboard.TTTBoard(3)

pygame.display.set_caption("Tic Tac Toe")
helper.draw_empty_board(board,screen, helper.WIDTH, helper.HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip()

