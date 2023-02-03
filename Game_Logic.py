from random import randint

from pygame import Vector2

from GUI.Game_Board import GameBoard

class Game_Logic:

    def __init__(self,game_board : GameBoard):
        self.game_board = game_board
        self.current_player = randint(0, 1)
        self.marks = ["X","O"]
        self.game_finished = False
        self.button_clicked_counter = 0


    def handle_click(self,coordinate : Vector2):
        if self.game_finished:
            return
        button = self.game_board.get_clicked_button(coordinate)
        if button.get_is_flliped():
            return
        button.text = self.marks[self.current_player]
        button.handle_click(coordinate)
        self.button_clicked_counter = self.button_clicked_counter + 1
        self.check_win(coordinate,button)
        self.check_draw()
        self.change_player()


    def check_win(self,coordinate : Vector2,button):
        bt_coordinate = self.game_board.get_button_coordinate(coordinate)
        win = self.check_main_digonal(button) \
              or self.check_sec_digonal(button) \
              or self.check_row(button,bt_coordinate) \
              or self.check_col(button,bt_coordinate)

        if win:
            self.declare_winner()
            self.game_finished = True

    def check_draw(self):
        if self.button_clicked_counter == self.game_board.num_of_rows*self.game_board.num_of_cols:
            self.game_finished = True
            print(f"its a Draw!!!!!!!!!! you idiot")


    def check_row(self,button,bt_coordinate : Vector2):
        row = int(bt_coordinate.x)
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[row][i].get_button_mark() != button.get_button_mark():
                return False
        return True

    def check_col(self, button, bt_coordinate: Vector2):
        col = int(bt_coordinate.y)
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[i][col].get_button_mark() != button.get_button_mark():
                return False
        return True


    def check_main_digonal(self,button):
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[i][i].get_button_mark() != button.get_button_mark():
                return False
        return True


    def check_sec_digonal(self,button):
        for i in range(self.game_board.num_of_rows):
            if self.game_board.game_matrix[i][self.game_board.num_of_cols - i - 1].get_button_mark() != button.get_button_mark():
                return False
        return True


    def change_player(self):
        self.current_player = self.current_player^1

    def declare_winner(self):
        print(f"player -> {self.current_player} , mark -> {self.marks[self.current_player]} is the winner")
