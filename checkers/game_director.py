import pygame
from .board import Board
from checkers.constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK

from .stone import Stone
from .king import King


class GameDirector:

    def __init__(self, board, win):
        self.white = None
        self.grey = None
        self.board = board
        self.win = win
        self.on_move = None
        self.selected_stone = None
        self.capturing_moves = []

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
                      # (King(self.board.squares["e4"], WHITE, self.win))
                      ]

        self.on_move = self.white

        print("Hra začíná. Na řadě je bílá.")

    def next_move(self):
        if self.on_move == self.white:
            for stone in self.on_move:
                if stone.square.row == 7:
                    self.white.remove(stone)
                    king = King(stone.square, WHITE, self.win)
                    self.white.append(king)
                    king.draw_stone()
                    print("Korunovace bile damy")
            self.on_move = self.grey
            print("Na tahu je šedá")
        else:

            for stone in self.on_move:
                if stone.square.row == 0:
                    self.grey.remove(stone)
                    king = King(stone.square, GREY, self.win)
                    self.grey.append(king)
                    king.draw_stone()
                    print("Korunovace sede damy")
            self.on_move = self.white
            print("Na tahu je bílá")

    def is_non_capturing_move_valid(self, clicked_square):
        if self.selected_stone not in self.on_move:
            print(f"Tah není validní. Na tahu je {self.on_move[0].color}")
            return False
        if clicked_square.color != self.selected_stone.square.color:
            print("Tah není validní. Pohybuj se pouze na tmavých čtvercích.")
            return False
        if (abs(clicked_square.row - self.selected_stone.square.row) > 1) or (
                abs(clicked_square.col - self.selected_stone.square.col) > 1):
            print("Tah není validní. Pohybuj se pouze na platné čtverce.")
            return False
        if (self.on_move == self.white) and (clicked_square.row < self.selected_stone.square.row):
            print("Tah není validní. Pohybuj se pouze dopředu.")
            return False
        if (self.on_move == self.grey) and (clicked_square.row > self.selected_stone.square.row):
            print("Tah není validní. Pohybuj se pouze dopředu.")
            return False
        return True

    def is_capturing_move(self):

        self.capturing_moves = []
        if self.on_move == self.grey:
            for stone in self.on_move:
                diagonal_squares_1 = []
                diagonal_squares_2 = []
                diagonal_squares_3 = []
                diagonal_squares_4 = []
                print("Reseny stone", stone.square.col, stone.square.row)
                for i in range(1, 9, 1):

                    square = self.board.get_square_by_coord(stone.square.col + i, stone.square.row - i)
                    if square is not None:
                        diagonal_squares_1.append(square)

                    square = self.board.get_square_by_coord(stone.square.col - i, stone.square.row - i)
                    if square is not None:
                        diagonal_squares_2.append(square)

                    if isinstance(stone,King):
                        square = self.board.get_square_by_coord(stone.square.col + i, stone.square.row + i)
                        if square is not None:
                            diagonal_squares_3.append(square)

                        square = self.board.get_square_by_coord(stone.square.col - i, stone.square.row + i)
                        if square is not None:
                            diagonal_squares_4.append(square)

                if len(diagonal_squares_1) > 0 and diagonal_squares_1[0].stone is not None and diagonal_squares_1[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_1):
                        if diagonal_squares_1[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_1[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_1[index].stone in self.on_move:
                            break
                        index += 1
                if len(diagonal_squares_2) > 0 and diagonal_squares_2[0].stone is not None and diagonal_squares_2[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_2):
                        if diagonal_squares_2[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_2[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_2[index].stone in self.on_move:
                            break
                        index += 1
                if len(diagonal_squares_3) > 0 and diagonal_squares_3[0].stone is not None and diagonal_squares_3[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_3):
                        if diagonal_squares_3[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_3[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_3[index].stone in self.on_move:
                            break
                        index += 1
                if len(diagonal_squares_4) > 0 and diagonal_squares_4[0].stone is not None and diagonal_squares_4[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_4):
                        if diagonal_squares_4[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_4[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_4[index].stone in self.on_move:
                            break
                        index += 1


        elif self.on_move == self.white:

            for stone in self.on_move:
                diagonal_squares_1 = []
                diagonal_squares_2 = []
                diagonal_squares_3 = []
                diagonal_squares_4 = []
                print("Reseny stone", stone.square.col, stone.square.row)
                for i in range(1, 9, 1):

                    square = self.board.get_square_by_coord(stone.square.col + i, stone.square.row + i)
                    if square is not None:
                        diagonal_squares_1.append(square)

                    square = self.board.get_square_by_coord(stone.square.col - i, stone.square.row + i)
                    if square is not None:
                        diagonal_squares_2.append(square)

                    if isinstance(stone,King):
                        square = self.board.get_square_by_coord(stone.square.col + i, stone.square.row - i)
                        if square is not None:
                            diagonal_squares_3.append(square)

                        square = self.board.get_square_by_coord(stone.square.col - i, stone.square.row - i)
                        if square is not None:
                            diagonal_squares_4.append(square)

                if len(diagonal_squares_1) > 0 and diagonal_squares_1[0].stone is not None and diagonal_squares_1[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_1):
                        if diagonal_squares_1[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_1[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_1[index].stone in self.on_move:
                            break
                        index += 1
                if len(diagonal_squares_2) > 0 and diagonal_squares_2[0].stone is not None and diagonal_squares_2[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_2):
                        if diagonal_squares_2[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_2[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_2[index].stone in self.on_move:
                            break
                        index += 1
                if len(diagonal_squares_3) > 0 and diagonal_squares_3[0].stone is not None and diagonal_squares_3[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_3):
                        if diagonal_squares_3[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_3[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_3[index].stone in self.on_move:
                            break
                        index += 1
                if len(diagonal_squares_4) > 0 and diagonal_squares_4[0].stone is not None and diagonal_squares_4[
                    0].stone not in self.on_move:
                    index = 1
                    while index < len(diagonal_squares_4):
                        if diagonal_squares_4[index].stone is None:
                            self.capturing_moves.append(diagonal_squares_4[0:index + 1])
                            self.capturing_moves[len(self.capturing_moves) - 1].insert(0, stone.square)

                            break
                        elif diagonal_squares_4[index].stone in self.on_move:
                            break
                        index += 1
        return True

    def is_king_move_valid(self,clicked_square):
        if self.selected_stone not in self.on_move:
            print(f"Tah není validní. Na tahu je {self.on_move[0].color}")
            return False
        if clicked_square.color != self.selected_stone.square.color:
            print("Tah není validní. Pohybuj se pouze na tmavých čtvercích.")
            return False


    def handle_click(self, clicked_square):
        self.is_capturing_move()
        if clicked_square.stone is not None:
            self.selected_stone = clicked_square.stone
        else:
            if self.selected_stone is None:
                print("Je třeba označit kámen, kterým chceš táhnout.")
            else:
                if len(self.capturing_moves) > 0:
                    selected_move = None
                    for move in self.capturing_moves:

                        if move[0] == self.selected_stone.square and move[-1] == clicked_square:
                            selected_move = move

                    if selected_move is None:
                        print("Je povinne brat souperovy stony.")
                        return
                    self.selected_stone.move_stone(clicked_square)
                    self.remove_stone_from_squares(selected_move)
                    self.capturing_moves = []
                    self.selected_stone = None

                    self.next_move()

                if self.is_non_capturing_move_valid(clicked_square):
                    self.selected_stone.move_stone(clicked_square)
                    self.selected_stone = None
                    self.next_move()

    def remove_stone_from_squares(self, squares):
        for square in squares[1:-1:]:
            try:
                self.white.remove(square.stone)
            except ValueError:
                self.grey.remove(square.stone)

            square.draw(self.win)
            square.stone = None
