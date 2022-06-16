import pygame.draw

from .constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY
from checkers.square import Square


class Piece:
    PADDING = 10
    OUTLINE = 2

    def __init__(self, square, color):
        self.square = square
        self.color = color

    def draw_piece(self,win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.square.row * SQUARE_SIZE + SQUARE_SIZE // 2, self.square.col * SQUARE_SIZE+ SQUARE_SIZE // 2), radius)


"""     self.row = row
        self.col = col
        self.color = color
        self.king = False
        # self.selected = False

        if self.color == BURLYWOOD:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius + self.OUTLINE)

    def __repr__(self):
        return str(self.color)"""
