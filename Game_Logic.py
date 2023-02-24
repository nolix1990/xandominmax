import logging
from random import randint

from pygame import Vector2
from Game_State import Game_State

from GUI.Game_Board import GameBoard
from GUI.Game_Button import Game_Button
logger = logging.getLogger(__name__)

class Game_Logic:

    def __init__(self,game_board : GameBoard):
        self.game_board = game_board
        self.current_player = randint(0, 1)
        self.marks = ["X","O"]
        self.game_finished = False
        self.button_clicked_counter = 0
        self.epsilon = self.game_board.button_width/2


    def handle_click(self,coordinate : Vector2):
        if self.game_finished:
            return
        button = self.game_board.get_clicked_button(coordinate)
        if button.get_is_flliped():
            return
        button.text = self.marks[self.current_player]
        button.handle_click(coordinate)
        self.button_clicked_counter = self.button_clicked_counter + 1
        game_state = self.get_game_state(coordinate,button)
        self.change_player()
        return game_state


    def get_game_state(self,coordinate,button):
        if self.check_win(coordinate,button) : return Game_State.WIN
        if self.check_draw() : return Game_State.DRAW
        return Game_State.IDLE


    def undo_change(self , button : Game_Button):
        button.undo_handle_click()
        button.text = " "
        self.game_finished = False
        self.button_clicked_counter = self.button_clicked_counter - 1
        self.change_player()
        self.game_board.winingLine = None


    def check_win(self,coordinate : Vector2,button):
        bt_coordinate = self.game_board.get_button_coordinate(coordinate)
        win = self.check_main_digonal(button) \
              or self.check_sec_digonal(button) \
              or self.check_row(button,bt_coordinate) \
              or self.check_col(button,bt_coordinate)

        if win:
            self.declare_winner()
            self.game_finished = True
            return True
        return False


    def check_draw(self):
        if self.button_clicked_counter == self.game_board.num_of_rows*self.game_board.num_of_cols:
            self.game_finished = True
            logger.info(f"its a Draw!!!!!!!!!! you idiot")
            return True
        return False

    def check_row(self, button, bt_coordinate: Vector2):
        row = int(bt_coordinate.x)
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[row][i].get_button_mark() != button.get_button_mark():
                return False

        startPoint = self.game_board.game_matrix[row][0].GetTextCenter()
        startPoint = (startPoint[0] - self.epsilon, startPoint[1])
        endPoint = self.game_board.game_matrix[row][self.game_board.num_of_cols-1].GetTextCenter()
        endPoint = (endPoint[0] + self.epsilon, endPoint[1])
        self.game_board.setWiningLine(startPoint, endPoint)

        return True

    def check_col(self, button, bt_coordinate: Vector2):
        col = int(bt_coordinate.y)
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[i][col].get_button_mark() != button.get_button_mark():
                return False

        startPoint = self.game_board.game_matrix[0][col].GetTextCenter()
        startPoint = (startPoint[0], startPoint[1] - self.epsilon)
        endPoint = self.game_board.game_matrix[self.game_board.num_of_rows - 1][col].GetTextCenter()
        endPoint = (endPoint[0], endPoint[1] + self.epsilon)
        self.game_board.setWiningLine(startPoint, endPoint)

        return True

    def check_main_digonal(self, button):
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[i][i].get_button_mark() != button.get_button_mark():
                return False

        startPoint = self.game_board.game_matrix[0][0].GetTextCenter()
        startPoint = (startPoint[0] - self.epsilon, startPoint[1] - self.epsilon)
        endPoint = self.game_board.game_matrix[self.game_board.num_of_rows - 1][self.game_board.num_of_cols - 1].GetTextCenter()
        endPoint = (endPoint[0] + self.epsilon, endPoint[1] + self.epsilon)
        self.game_board.setWiningLine(startPoint, endPoint)

        return True

    def check_sec_digonal(self, button):
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[i][
                self.game_board.num_of_cols - i - 1].get_button_mark() != button.get_button_mark():
                return False

        startPoint = self.game_board.game_matrix[0][self.game_board.num_of_cols - 1].GetTextCenter()
        startPoint = (startPoint[0] + self.epsilon, startPoint[1] - self.epsilon)
        endPoint = self.game_board.game_matrix[self.game_board.num_of_rows - 1][0].GetTextCenter()
        endPoint = (endPoint[0] - self.epsilon, endPoint[1] + self.epsilon)
        self.game_board.setWiningLine(startPoint, endPoint)

        return True

    def change_player(self):
        self.current_player = self.current_player ^ 1

    def declare_winner(self):
        logger.info(f"player -> {self.current_player} , mark -> {self.marks[self.current_player]} is the winner")

    def set_(self):
        return self.current_player
