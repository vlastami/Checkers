import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
from checkers.piece import Piece
from checkers.constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # uppercase because constants
pygame.display.set_caption("Checkers")


def main():
    run = True
    clock = pygame.time.Clock()

    board = Board()
    board.create_squares(WIN)

    piece = Piece(board.squares[3], GREY)

    piece.draw_piece(WIN)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        pygame.display.update()




main()