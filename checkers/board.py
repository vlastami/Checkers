import pygame
from .constants import BLACK, ROWS, COLS, BURLYWOOD, SQUARE_SIZE, SADDLEBROWN
from .square import Square


class Board:
    def __init__(self):
        self.squares = {}
        # self.turn = 0
        self.selected_piece = None

    def create_squares(self, win):
        squares = []
        for col in range(COLS):

            for row in range(ROWS):

                if col % 2 == 0:
                    if row % 2 == 0:
                        square = Square(row, col, SADDLEBROWN)
                        square.draw(win)
                        squares.append(square)

                    else:
                        square = Square(row, col, BURLYWOOD)
                        square.draw(win)
                        squares.append(square)
                else:
                    if row % 2 > 0:
                        square = Square(row, col, SADDLEBROWN)
                        square.draw(win)
                        squares.append(square)
                    else:
                        square = Square(row, col, BURLYWOOD)
                        square.draw(win)
                        squares.append(square)
        self.squares = {"a1": squares[0], "b1": squares[1], "c1": squares[2], "d1": squares[3],
                        "e1": squares[4], "f1": squares[5], "g1": squares[6], "h1": squares[7],
                        "a2": squares[8], "b2": squares[9], "c2": squares[10], "d2": squares[11],
                        "e2": squares[12], "f2": squares[13], "g2": squares[14], "h2": squares[15],
                        "a3": squares[16], "b3": squares[17], "c3": squares[18], "d3": squares[19],
                        "e3": squares[20], "f3": squares[21], "g3": squares[22], "h3": squares[23],
                        "a4": squares[24], "b4": squares[25], "c4": squares[26], "d4": squares[27],
                        "e4": squares[28], "f4": squares[29], "g4": squares[30], "h4": squares[31],
                        "a5": squares[32], "b5": squares[33], "c5": squares[34], "d5": squares[35],
                        "e5": squares[36], "f5": squares[37], "g5": squares[38], "h5": squares[39],
                        "a6": squares[40], "b6": squares[41], "c6": squares[42], "d6": squares[43],
                        "e6": squares[44], "f6": squares[45], "g6": squares[46], "h6": squares[47],
                        "a7": squares[48], "b7": squares[49], "c7": squares[50], "d7": squares[51],
                        "e7": squares[52], "f7": squares[53], "g7": squares[54], "h7": squares[55],
                        "a8": squares[56], "b8": squares[57], "c8": squares[58], "d8": squares[59],
                        "e8": squares[60], "f8": squares[61], "g8": squares[62], "h8": squares[63],
                        }

    def get_square_by_pos(self, pos):
        posx = pos[0] // 100
        posy = pos[1] // 100
        for key in self.squares:
            if posx == self.squares[key].col and posy == self.squares[key].row:
                print(self.squares[key].row, self.squares[key].col)
                return self.squares[key]
