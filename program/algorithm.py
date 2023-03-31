from random import choice
def check(arr, ch):
    # for i in range(1, 10): print(arr[i], end = " ")

    # Kiểm tra hoà -> trả về 2
    IsFull = True
    for i in range(1, 10):
        if (arr[i] == ''):
            IsFull = False
            break 
    # if (IsFull): return [2, -1, -1, -1]

    #Kiểm tra ch thắng chưa -> 1/0

    ret = [0, 0, 0, 0]
    if ((arr[7] == ch and arr[8] == ch and arr[9] == ch )):
        ret = [1, 7, 8, 9]
    elif (arr[4] == ch and arr[5] == ch and arr[6] == ch):
        ret = [1, 4, 5, 6]
    elif (arr[1] == ch and arr[2] == ch and arr[3] == ch):
        ret = [1, 1, 2, 3]
    elif (arr[1] == ch and arr[4] == ch and arr[7] == ch):
        ret = [1, 1, 4, 7]
    elif (arr[2] == ch and arr[5] == ch and arr[8] == ch):
        ret = [1, 2, 5, 8]
    elif (arr[3] == ch and arr[6] == ch and arr[9] == ch):
        ret = [1, 3, 6, 9]
    elif (arr[1] == ch and arr[5] == ch and arr[9] == ch):
        ret = [1, 1, 5, 9]
    elif (arr[3] == ch and arr[5] == ch and arr[7] == ch):
        ret = [1, 3, 5, 7]
    elif IsFull: return [2, -1, -1, -1]
    return ret

def ChooseRandomFromList(arr, MoveList):
    PossibleMoves = []
    for i in MoveList:
        if arr[i] == '':
            PossibleMoves.append(i)
    if len(PossibleMoves) != 0:
        return choice(PossibleMoves)
    else:
        return None

def GetComputerMove(arr):

    #1.check computer can win in next move
    for i in range(1,10):
        if (arr[i] != ''): continue
        arr[i] = 'O'
        result = check(arr, 'O') 
        arr[i] = ''
        if (result[0] == 1):
            return i

    #2.check player can win in next move
    for i in range(1,10):
        if (arr[i] != ''): continue
        arr[i] = 'X'
        result = check(arr, 'X') 
        arr[i] = ''
        if (result[0] == 1):
            return i

    #3.checking for corner
    move = ChooseRandomFromList(arr, [1,3,7,9])
    if move != None:
        return move
        
    #4.checking for the center
    if arr[5] == '':
        return 5
        
    #5.checking for sides
    return ChooseRandomFromList(arr,[2,4,6,8])

def add(game_window, turn, loc, mode):

    #Cập nhật lượt chơi vừa rồi
    if turn%2!=0:
        char = 'O'
        color = "blue"
    else:
        char = 'X' 
        color = "red"
    game_window[loc].update(text = char, button_color = color)

    #Cập nhật status trò chơi lượt sau
    if (char == 'X'): nextchar = 'O'
    else: nextchar = 'X'

    stat_string = "TRẠNG THÁI TRÒ CHƠI: Lượt của người chơi '" + nextchar + "'"
    if (mode == 1 and nextchar == 'O'): stat_string = "TRẠNG THÁI TRÒ CHƠI: Lượt của '" + nextchar + "' (Máy)"
    game_window['-status-'].update(stat_string)

    return [char, color]




