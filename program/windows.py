import PySimpleGUI as sg
from algorithm import *

sg.theme('DarkGreen')

def win_menu():

    win_layout = [[sg.Text("LỰA CHỌN CỦA BẠN", font = ('TimesNewRoman bold', 20))],
                [sg.Text("")],
                [sg.HorizontalSeparator()],
                [sg.Button("Chơi Với Máy", font = ('TimesNewRoman', 15), key = "single", size = (15, 5)), sg.Button("Chơi Đối Kháng", font = ('TimesNewRoman', 15), key = "multi", size = (15, 5))],
                [sg.Button("Thoát", font = ('TimesNewRoman', 15), key = "exit", size = (10, 3))]
                ]
    
    menu = sg.Window(title="Menu", layout = win_layout, margins=(200, 60), element_justification='c').Finalize()
    menu.TKroot.tk.call('tk', 'scaling', 1)


    mode = int(0)

    while True:
        event, values = menu.read()
        if (event == "exit"):
            menu.close()
            return -1
        else:
            if event == "single": mode = 1
            elif event == "multi": mode = 2
        menu.close()
        break
    return mode
  

def game_menu(x):

    #Tạo băng trong của sổ game_window
    
    game_layout = [[sg.Text("TRẠNG THÁI TRÒ CHƠI: Lượt của người chơi 'X'", font = ('TimesNewRoman bold', 30), key = '-status-')],
                    [sg.Text('', font = ('TimesNewRoman', 70))],
                    [sg.Button('', font = ('TimesNewRoman', 70), key = 1, size = (3, 1)), sg.Button('', font = ('TimesNewRoman', 70), key = 2, size = (3, 1)), sg.Button('', font = ('TimesNewRoman', 70), key = 3, size = (3, 1))],
                    [sg.Button('', font = ('TimesNewRoman', 70), key = 4, size = (3, 1)), sg.Button('', font = ('TimesNewRoman', 70), key = 5, size = (3, 1)), sg.Button('', font = ('TimesNewRoman', 70), key = 6, size = (3, 1))],
                    [sg.Button('', font = ('TimesNewRoman', 70), key = 7, size = (3, 1)), sg.Button('', font = ('TimesNewRoman', 70), key = 8, size = (3, 1)), sg.Button('', font = ('TimesNewRoman', 70), key = 9, size = (3, 1))],
                    [sg.Text('', font = ('TimesNewRoman', 30))],
                    [sg.Button('Thoát', font = ('TimesNewRoman', 30), key = 'exit', size = (10, 1))]
                ]
    game_window = sg.Window(title = "New Game", layout = game_layout, element_justification='c').Finalize()
    print(game_window.TKroot.tk.call('tk', 'scaling'))
    char  = 'X'
    color = "red"
    turn = int(0)
    arr = [''] * 10
    end_game = False
    event = -1
    stat = [0, 0, 0, 0]
    while True:
        
        #Kiểm tra trạng thái trò chơi
        if (turn != 0):
            if (stat[0] == 2):
                game_window['-status-'].update("TRẠNG THÁI TRÒ CHƠI: Kết quả hoà", text_color = "Green")
                end_game = True
            elif (stat[0] == 1):
                if (x == 1 and (turn-1)%2 != 0):
                    game_window['-status-'].update("TRẠNG THÁI TRÒ CHƠI: Máy 'O' thắng", text_color = color)
                else:
                    game_window['-status-'].update("TRẠNG THÁI TRÒ CHƠI: Người chơi '" + char + "' thắng", text_color = color)
                #Highlight đường thắng
                for i in range(1, 4):
                    game_window[stat[i]].update(text = "✅", button_color = ('lime', color))
                end_game = True

        #Lượt của máy 
        if (x == 1 and turn %2 != 0 and not end_game):
            event = GetComputerMove(arr)   
        
        else: event, values = game_window.read()

        #Thoát trò chơi

        if event == 'exit':
            response = sg.popup_yes_no("Bạn có chắc chắn muốn thoát trò chơi?")
            if (response == 'Yes'):
                game_window.close()
                break
            else: continue

        #Kiểm tra xem trò chơi đã kết thúc hay chưa

        if (end_game):
            sg.popup("Trò chơi đã kết thúc")
            continue

        #Lấy giá trị hiện tại của nút vừa chọn

        button_value = game_window[event].GetText()


        #Kiểm tra xem nút đã được chọn trước đó hay chưa

        if (button_value != ''):
            sg.popup("Ô đã được chọn. Vui lòng chọn ô khác")
            continue

        #Đổi màu của nút và chữ
        char, color = add(game_window, turn, event, x)

        #Lấy kết quả trò chơi
        arr[event] = char 
        stat = check(arr, char)


        turn += 1


    return         

# --------------------------------------test-------------------------------
# game_menu(1)