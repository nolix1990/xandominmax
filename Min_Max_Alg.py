
from random import randint

from pygame import Vector2
from Game_State import Game_State
from GUI.Game_Board import GameBoard
from Game_Logic import Game_Logic


class MinMaxAlg:

    def __init__(self,game_board :GameBoard , game_logic : Game_Logic):
        self.game_borad = game_board
        self.game_logic = game_logic
        self.mark = 0
        self.num_of_moves = 0

    def min_max_alg(self):
        if self.game_logic.button_clicked_counter == 0:
            vec = Vector2(randint(0, self.game_borad.matrix_height),randint(0, self.game_borad.matrix_width))
            return (vec , 0 , Game_State.IDLE)

        res = self.between_choose_moves(0)

        print("min_max_finished")
        return res


    def between_choose_moves(self , depth):
        best_move = self.check_if_ai_will_loose()
        if best_move is not None:
            print("entred check_if_loose")
            return best_move
        print("find best move")
        return self.find_best_move(depth)


    def check_if_ai_will_loose(self):
        self.game_logic.change_player()
        for i in range(self.game_borad.num_of_rows):
            for j in range(self.game_borad.num_of_cols):
                button = self.game_borad.game_matrix[i][j]
                if button.text == " ":
                    bt_center_tupple = button.GetTextCenter()

                    game_state = self.game_logic.handle_click(Vector2(bt_center_tupple[0], bt_center_tupple[1]))

                    self.game_logic.undo_change(button)

                    if game_state == Game_State.WIN:
                        self.game_logic.change_player()
                        return (Vector2(bt_center_tupple[0], bt_center_tupple[1]), 0 , Game_State.IDLE)

        self.game_logic.change_player()
        return None



    def take_current_best_move(self,current_best_move , current_move , bt_center_tupple):

        if current_move[2] == Game_State.WIN and (current_move[1] < current_best_move[1]):
            current_best_move = (Vector2(bt_center_tupple[0], bt_center_tupple[1]), current_move[1], current_move[2])

        elif current_move[2] == Game_State.DRAW and (current_move[1] <= current_best_move[1]):
            current_best_move = (Vector2(bt_center_tupple[0], bt_center_tupple[1]), current_move[1], current_move[2])

        return current_best_move




    def find_best_move(self,depth):
        best_value = ( Vector2(0,0) , 10**6 , Game_State.LOOSE)
        for i in range(self.game_borad.num_of_rows):
            for j in range(self.game_borad.num_of_cols):
                button = self.game_borad.game_matrix[i][j]
                if button.text == " ":
                    bt_center_tupple = button.GetTextCenter()
                    game_state = self.game_logic.handle_click(Vector2(bt_center_tupple[0], bt_center_tupple[1]))

                    if ( game_state == Game_State.WIN and self.game_logic.current_player == 0) or game_state == Game_State.DRAW:
                        self.game_logic.undo_change(button)
                        return (Vector2(bt_center_tupple[0], bt_center_tupple[1]), depth + 1, game_state)
                    elif (game_state == Game_State.WIN and self.game_logic.current_player == 1):
                        self.game_logic.undo_change(button)
                        return (Vector2(bt_center_tupple[0], bt_center_tupple[1]), depth + 1, Game_State.LOOSE)

                    self.num_of_moves = self.num_of_moves + 1

                    res = self.find_best_move(depth + 1)
                    self.game_logic.undo_change(button)

                    best_value = self.take_current_best_move(best_value,res,bt_center_tupple)


        return best_value











