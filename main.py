
import pygame
from pygame.locals import *

from GUI.Game_Board import GameBoard
from pygame import Vector2 as vec

from Game_Logic import Game_Logic

pygame.init()
ScreenWidthpx = 600
ScreenHieghpx = 600
screen = pygame.display.set_mode((ScreenWidthpx, ScreenHieghpx))
clock = pygame.time.Clock()

def handle_mouse_click(game_board):
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        game_board.handle_click(vec(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))


def main():
    board = GameBoard(ScreenWidthpx,ScreenHieghpx)
    game_logic = Game_Logic(board)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(game_logic)

        board.draw(screen)

        clock.tick(30)
        pygame.display.flip()

main()