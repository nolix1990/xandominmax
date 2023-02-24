import threading


class Game_Handler:

    def __init__(self,game_board,game_logic):
        game_thread = threading.Thread(target= game_logic)
