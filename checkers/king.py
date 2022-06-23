from checkers.stone import Stone
from .constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK
import pygame


class King(Stone):
    def __init__(self, square, color, win):
        super().__init__(square, color, win)



    def draw_stone(self):
        super().draw_stone()
        radius = SQUARE_SIZE // 3 - 10

        pygame.draw.circle(self.win, BLACK, (self.square.col * SQUARE_SIZE + SQUARE_SIZE // 1.96, self.square.row * SQUARE_SIZE+ SQUARE_SIZE // 1.96), radius)

    def get_csv_data(self):
        data = ""
        if self.color == GREY:
            data = "bb"
        else:
            data = "ww"
        return data

