import pygame.draw

from .constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY
from checkers.square import Square


class Stone:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, square, color, win):
        self.square = square
        self.color = color
        self.win = win
        self.draw_stone()

    def draw_stone(self):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(self.win, self.color, (self.square.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.square.col * SQUARE_SIZE+ SQUARE_SIZE // 2), radius)

    def move_stone(self, square):
        self.square.draw(self.win)
        self.square = square
        self.draw_stone(self.win)
