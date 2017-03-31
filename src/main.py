import sys, pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255

pygame.init()

size = width, height = 240, 320
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(WHITE)
    pygame.display.flip()

