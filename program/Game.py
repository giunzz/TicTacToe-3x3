from windows import *

while (True):
    game_mode = win_menu()
    if (game_mode == -1): break
    game_menu(game_mode)
