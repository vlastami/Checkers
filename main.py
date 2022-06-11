import pygame
from checkers.constants import WIDTH, HEIGHT

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # uppercase because constants
pygame.display.set_caption("Checkers")

def main():
    run = True
    clock = pygame.time.Clock

    while run:
        pass

main()

