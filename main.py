import pygame, sys
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
from checkers.stone import Stone
from checkers.game_director import GameDirector
from checkers.constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # uppercase because constants
pygame.display.set_caption("Checkers")


def main():
    run = True
    clock = pygame.time.Clock()

    board = Board()
    game_director = GameDirector(board, WIN)
    game_director.new_game()



    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                board.get_square_by_pos(pos)

        pygame.display.update()




main()

