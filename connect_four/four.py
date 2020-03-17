from enum import IntEnum

class Player(IntEnum):
    Player_One = 0
    Player_Two = 1

board_height = 6
board_width = 7
board = []
while(len(board) < board_width):
    board.append([' ', ' ', ' ', ' ', ' ', ' '])

def drawboard():
    print(f'|{board[0][5]}|{board[1][5]}|{board[2][5]}|{board[3][5]}|{board[4][5]}|{board[5][5]}|{board[6][5]}|')
    print(f'|{board[0][4]}|{board[1][4]}|{board[2][4]}|{board[3][4]}|{board[4][4]}|{board[5][4]}|{board[6][4]}|')
    print(f'|{board[0][3]}|{board[1][3]}|{board[2][3]}|{board[3][3]}|{board[4][3]}|{board[5][3]}|{board[6][3]}|')
    print(f'|{board[0][2]}|{board[1][2]}|{board[2][2]}|{board[3][2]}|{board[4][2]}|{board[5][2]}|{board[6][2]}|')
    print(f'|{board[0][1]}|{board[1][1]}|{board[2][1]}|{board[3][1]}|{board[4][1]}|{board[5][1]}|{board[6][1]}|')
    print(f'|{board[0][0]}|{board[1][0]}|{board[2][0]}|{board[3][0]}|{board[4][0]}|{board[5][0]}|{board[6][0]}|')
    print('---------------')
    print('|0|1|2|3|4|5|6|')

def fourinarow(row):
    i = 0
    streak = 1
    current = ''
    while(i < len(board)):
        if (current == board[i][row]) and (current != ' '):
            streak += 1
            if(streak == 4):
                return True
        else:
            current = board[i][row]
            streak = 1
        i += 1
    return False

def fourinacolumn(column):
    i = 0
    streak = 1
    current = ''
    while(i < board_height):
        if (current == board[column][i]) and (current != ' '):
            streak += 1
            if(streak == 4):
                return True
        else:
            current = board[column][i]
            streak = 1
        i += 1
    return False

def fourindiagonalrising(x, y):
    i = 0
    streak = 1
    current = ''
    while(x + i < len(board) and y + i < board_height):
        if (current == board[x+i][y+i]) and (current != ' '):
            streak += 1
            if(streak == 4):
                return True
        else:
            current = board[x+i][y+i]
            streak = 1
        i += 1
    return False

def fourindiagonalfalling(x, y):
    i = 0
    streak = 1
    current = ''
    while(x + i < board_width and y - i >= 0):
        if (current == board[x+i][y-i]) and (current != ' '):
            streak += 1
            if(streak == 4):
                return True
        else:
            current = board[x+i][y-i]
            streak = 1
        i += 1
    return False

def gameOver():
    win = False
    i = 0
    while(i < board_height):
        win = win or fourinarow(i)
        i += 1
    i = 0
    while(i < board_width):
        win = win or fourinacolumn(i)
        i += 1
    y = board_height - 4
    x = 0
    while(y >= 0):
        win = win or fourindiagonalrising(x, y)
        y = y - 1
    y = 0
    while(x <= board_width - 4):
        win = win or fourindiagonalrising(x, y)
        x = x + 1
    y = 3
    x = 0
    while(y < board_height):
        win = win or fourindiagonalfalling(x, y)
        y = y + 1
    y = board_height - 1
    while(x <= board_width - 4):
        win = win or fourindiagonalfalling(x, y)
        x = x + 1
    
    return win

def isInputValid(value):
    return (value.isnumeric() and (int(value) >= 0 and int(value) < 7))

playernames = ['Player One', 'Player Two']

def maketurn(player):
    print(f'{playernames[player]}\'s Turn. Choose a Column. [0-6]')
    while(True):
        value = input()
        if isInputValid(value):
            value = int(value)
            i = 0
            while(i < len(board[value])):
                if(board[value][i] == ' '):
                    if(player == Player.Player_One):
                        board[value][i] = 'O'
                    else:
                        board[value][i] = 'X'
                    break
                i += 1
            else:
                print('Column already full. Cose another one')
                continue
            break
    else:
        print('invalid input. try again')

turn = Player.Player_Two
while(not gameOver()):
    drawboard()
    turn = (turn+1)%2
    maketurn(turn)
drawboard()
print(f'{playernames[turn]} wins!')