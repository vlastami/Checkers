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

        self.squares = {"a1": squares[0], "a2": squares[1], "a3": squares[2], "a4": squares[3],
                    "a5": squares[4], "a6": squares[5], "a7": squares[6], "a8": squares[7],
                    "b1": squares[8], "b2": squares[9], "b3": squares[10], "b4": squares[11],
                    "b5": squares[12], "b6": squares[13], "b7": squares[14], "b8": squares[15],
                    "c1": squares[16], "c2": squares[17], "c3": squares[18], "c4": squares[19],
                    "c5": squares[20], "c6": squares[21], "c7": squares[22], "c8": squares[23],
                    "d1": squares[24], "d2": squares[25], "d3": squares[26], "d4": squares[27],
                    "d5": squares[28], "d6": squares[29], "d7": squares[30], "d8": squares[31],
                    "e1": squares[32], "e2": squares[33], "e3": squares[34], "e4": squares[35],
                    "e5": squares[36], "e6": squares[37], "e7": squares[38], "e8": squares[39],
                    "f1": squares[40], "f2": squares[41], "f3": squares[42], "f4": squares[43],
                    "f5": squares[44], "f6": squares[45], "f7": squares[46], "f8": squares[47],
                    "g1": squares[48], "g2": squares[49], "g3": squares[50], "g4": squares[51],
                    "g5": squares[52], "g6": squares[53], "g7": squares[54], "g8": squares[55],
                    "h1": squares[56], "h2": squares[57], "h3": squares[58], "h4": squares[59],
                    "h5": squares[60], "h6": squares[61], "h7": squares[62], "h8": squares[63]}

        for key in self.squares:
            print(key, self.squares[key].col, self.squares[key].row)


    def get_square_by_pos(self, pos):
        posx = pos[0] // 100
        posy = pos[1] // 100
        return self.get_square_by_coord(posx,posy)

    def get_square_by_coord(self,posx, posy):

        for key in self.squares:
            if posx == self.squares[key].col and posy == self.squares[key].row:
                # print(self.squares[key].col, self.squares[key].row)
                return self.squares[key] # vrací jeden objekt typu square