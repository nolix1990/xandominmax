import pygame
from pygame.locals import *
from GUI.Game_Board import GameBoard
from pygame import Vector2 as vec

from Game_Logic import Game_Logic
from Min_Max_Alg import MinMaxAlg
import logging

logging.basicConfig(filename='app.log', level=logging.INFO,filemode='w', format='%(asctime)s - %(name)s - [%(levelname)s] funcName=%(funcName)s- %(message)s')
logger = logging.getLogger(__name__)

pygame.init()
ScreenWidthpx = 600
ScreenHieghpx = 600
screen = pygame.display.set_mode((ScreenWidthpx, ScreenHieghpx))
clock = pygame.time.Clock()

def handle_mouse_click(game_board,coordinate = None):
    if coordinate is not None:
        game_board.handle_click(coordinate)
        return
    left, middle, right = pygame.mouse.get_pressed()
    if left:
        game_board.handle_click(vec(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))


def main():
    board = GameBoard(ScreenWidthpx,ScreenHieghpx,False)
    game_logic = Game_Logic(board)
    min_max_alg = MinMaxAlg(board,game_logic)

    while True:
        if game_logic.current_player == 0 and not game_logic.game_finished :
            tupple = min_max_alg.min_max_alg()
            logger.info(str(tupple[0]))
            handle_mouse_click(game_logic,tupple[0])
            continue

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