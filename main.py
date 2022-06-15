import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

FPS = 120

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # uppercase because constants
pygame.display.set_caption("Checkers")

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        board = Board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_cubes(WIN)
        pygame.display.update()




main()