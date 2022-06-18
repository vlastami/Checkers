import pygame
from .board import Board
from checkers.constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK

from .stone import Stone

class GameDirector:

    def __init__(self, board, win):
        self.board = board
        self.win = win


    def new_game(self):
        self.board.create_squares(self.win)

        black = [(Stone(self.board.squares["a7"], GREY, self.win)),
                 (Stone(self.board.squares["b6"], GREY, self.win)),
                 (Stone(self.board.squares["c7"], GREY, self.win)),
                 (Stone(self.board.squares["d6"], GREY, self.win)),
                 (Stone(self.board.squares["d8"], GREY, self.win)),
                 (Stone(self.board.squares["e7"], GREY, self.win)),
                 (Stone(self.board.squares["f6"], GREY, self.win)),
                 (Stone(self.board.squares["g7"], GREY, self.win)),
                 (Stone(self.board.squares["h6"], GREY, self.win)),
                 (Stone(self.board.squares["h8"], GREY, self.win)),
                 (Stone(self.board.squares["b8"], GREY, self.win)),
                 (Stone(self.board.squares["f8"], GREY, self.win)),
                 ]
        white = [(Stone(self.board.squares["a1"], WHITE, self.win)),
                 (Stone(self.board.squares["a3"], WHITE, self.win)),
                 (Stone(self.board.squares["b2"], WHITE, self.win)),
                 (Stone(self.board.squares["c1"], WHITE, self.win)),
                 (Stone(self.board.squares["c3"], WHITE, self.win)),
                 (Stone(self.board.squares["d2"], WHITE, self.win)),
                 (Stone(self.board.squares["e1"], WHITE, self.win)),
                 (Stone(self.board.squares["e3"], WHITE, self.win)),
                 (Stone(self.board.squares["f2"], WHITE, self.win)),
                 (Stone(self.board.squares["g1"], WHITE, self.win)),
                 (Stone(self.board.squares["g3"], WHITE, self.win)),
                 (Stone(self.board.squares["h2"], WHITE, self.win)),
                 ]


