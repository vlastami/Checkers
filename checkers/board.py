import pygame
from .constants import BLACK,ROWS,COLS, BURLYWOOD, SQUARE_SIZE, SADDLEBROWN
from .square import Square


class Board:
    def __init__(self):
        self.squares = []
        # self.turn = 0
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0

    def create_squares(self, win):

        for col in range(COLS):
            for row in range(ROWS):

                if (col % 2 == 0):
                    if (row % 2 == 0):
                        square = Square(row, col, BURLYWOOD)
                        square.draw(win)
                        self.squares.append(square)
                    else:
                        square = Square(row, col, SADDLEBROWN)
                        square.draw(win)
                        self.squares.append(square)
                else:
                    if (row % 2 > 0):
                        square = Square(row, col, BURLYWOOD)
                        square.draw(win)
                        self.squares.append(square)
                    else:
                        square = Square(row, col, SADDLEBROWN)
                        square.draw(win)
                        self.squares.append(square)
