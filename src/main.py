import sys, pygame
import helper
import TTTboard


pygame.init()

screen = pygame.display.set_mode(helper.SIZE)
board = TTTboard.TTTBoard(3)

pygame.display.set_caption("Tic Tac Toe")
helper.draw_empty_board(board.get_dim(),screen, helper.WIDTH, helper.HEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            x_press, y_press = pygame.mouse.get_pos()
            row, col = helper.get_square_from_coords(board.get_dim(),x_press,y_press)

    pygame.display.flip()

