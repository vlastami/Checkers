import pygame
from checkers.constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK

class Square:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
