import pygame, sys, csv
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board
from checkers.stone import Stone
from checkers.game_director import GameDirector
from checkers.constants import BURLYWOOD, WHITE, SQUARE_SIZE, GREY, BLACK

FPS = 60

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # uppercase because constants
pygame.display.set_caption("Checkers")


def main():
    run = True
    clock = pygame.time.Clock()

    board = Board()
    game_director = GameDirector(board, WIN)
    game_director.new_game()


    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                clicked_square = board.get_square_by_pos(pos)
                game_director.handle_click(clicked_square)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    game_director.random_move()
                elif event.key == pygame.K_F5:

                    with open('./csv_file', 'w', newline='') as f:
                        writer = csv.writer(f)
                        writer.writerows(board.get_csv())
                elif event.key == pygame.K_F6:
                    board.create_squares(WIN)
                    game_director.white = []
                    game_director.grey = []
                    game_director.on_move = game_director.white
                    with open('./csv_file', 'r') as f:
                        reader = csv.reader(f)
                        for row in reader:
                            game_director.spawn_stone(row)






        pygame.display.update()





main()

