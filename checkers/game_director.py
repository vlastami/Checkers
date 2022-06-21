import pygame
from .board import Board
from checkers.constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK

from .stone import Stone

class GameDirector:

    def __init__(self, board, win):
        self.white = None
        self.grey = None
        self.board = board
        self.win = win
        self.on_move = None
        self.selected_stone = None


    def new_game(self):
        self.board.create_squares(self.win)

        self.grey = [(Stone(self.board.squares["a7"], GREY, self.win)),
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
        self.white = [(Stone(self.board.squares["a1"], WHITE, self.win)),
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

        self.on_move = self.white
        print("Hra začíná. Na řadě je bílá.")



    def next_move(self):
        if self.on_move == self.white:
            self.on_move = self.grey
            print("Na tahu je šedá")
        else:
            self.on_move = self.white
            print("Na tahu je bílá")

    def is_non_capturing_move_valid(self, clicked_square):
        if self.selected_stone not in self.on_move:
            print(f"Tah není validní. Na tahu je {self.on_move[0].color}")
            return False
        if clicked_square.color != self.selected_stone.square.color:
            print("Tah není validní. Pohybuj se pouze na tmavých čtvercích.")
            return False
        if (abs(clicked_square.row - self.selected_stone.square.row) > 1) or (abs(clicked_square.col - self.selected_stone.square.col) > 1):
            print("Tah není validní. Pohybuj se pouze na platné čtverce.")
            return False
        if (self.on_move == self.white) and (clicked_square.row < self.selected_stone.square.row):
            print("Tah není validní. Pohybuj se pouze dopředu.")
            return False
        if (self.on_move == self.grey) and (clicked_square.row > self.selected_stone.square.row):
            print("Tah není validní. Pohybuj se pouze dopředu.")
            return False
        return True

    def is_capturing_move_valid(self):
        pass

    def is_capturing_move(self):
        if self.on_move == self.grey:
            for stone in self.on_move:
                print("Reseny stone", stone.square.col, stone.square.row)
                for i in range(1,9,1):
                    # if stone.square.col + i < 9 and stone.square.row - i > 0:
                    square = self.board.get_square_by_coord(stone.square.col + i, stone.square.row - i)
                    if square is not None:
                        print("Resene ctvrce: ",square.col, square.row)#TODO Sem prijde handlovani brani, protoze tohle jsou squary, ze kterych se daji brat stony, mozne brani nahazej asi do tuplu.


        return True

    def handle_click(self, clicked_square):
        self.is_capturing_move()
        if clicked_square.stone is not None:
            self.selected_stone = clicked_square.stone
        else:
            if self.selected_stone is None:
                print("Je třeba označit kámen, kterým chceš táhnout.")
            else:
                if self.is_non_capturing_move_valid(clicked_square):
                    self.selected_stone.move_stone(clicked_square)
                    self.selected_stone = None
                    self.next_move()


