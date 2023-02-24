from pygame import Color, Surface
from pygame.math import Vector2

from GUI.Game_Button import Game_Button
from GUI.Game_line import GameLine
from Interface.IClick import IClick
from Interface.IDraw import IDraw


class GameBoard(IDraw,IClick):
    BORDER=5#px

    def __init__(self, matrix_width, matrix_height: int , enable_ai : bool):
        if matrix_width * matrix_height % 2 != 0: raise Exception("matrix_size must be odd number")
        self.matrix_width = matrix_width
        self.matrix_height = matrix_height
        self.num_of_rows = 3
        self.num_of_cols = 3
        self.game_matrix:[[Game_Button]] = []
        self.border_lines = []
        self.button_width = matrix_width/self.num_of_cols
        self.button_height = matrix_height/self.num_of_rows
        self.button_color  = Color(255, 153, 51)
        self.font_color = Color(255, 255, 255)
        self.create_game()
        self.generate_border_lines()
        self.enable_ai = enable_ai



    def create_game(self):
        values_idx = 0

        for row in range(self.num_of_rows):
            temp_buttons_arr = []
            for col in range(self.num_of_cols):
                temp_buttons_arr.append(self.create_gamebutton_object(str(" "),col,row))
                values_idx = values_idx + 1
            self.game_matrix.append(temp_buttons_arr)



    def create_gamebutton_object(self,text_value : str ,col : int , row : int)->Game_Button:
        button = Game_Button(text_value,
                             self.button_width,
                             self.button_height,
                             self.button_color,
                             self.font_color,
                             self.calculate_button_coordinate(col,row))
        return button

    def generate_border_lines(self):
        for row in range(self.num_of_rows):
            # horizontal lines
            y = row * self.button_height
            startPoint = Vector2(0, y)
            endPoint = Vector2(self.matrix_width, y)
            self.border_lines.append(GameLine(GameBoard.BORDER,
                                              startPoint,
                                              endPoint))
        for col in range(self.num_of_cols):
            # vertecal  lines
            x = col * self.button_width
            startPoint = Vector2(x, 0)
            endPoint = Vector2(x, self.matrix_height)
            self.border_lines.append(GameLine(GameBoard.BORDER,
                                              startPoint,
                                              endPoint))


    def calculate_button_coordinate(self,col,row):
        return Vector2(col*self.button_width,row*self.button_height)


    def draw(self,surface : Surface):
        if self.enable_ai :
            return
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                self.game_matrix[row][col].draw(surface)
        for line in self.border_lines:
            line.draw(surface)

    def is_clicked(self,coordinate : Vector2):
        pass

    def get_clicked_button(self,coordinate : Vector2) -> Game_Button:
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if self.game_matrix[row][col].is_clicked(coordinate):
                    return self.game_matrix[row][col]

        return None


    def get_button_coordinate(self,coordinate):
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if self.game_matrix[row][col].is_clicked(coordinate):
                    return Vector2(row,col)


