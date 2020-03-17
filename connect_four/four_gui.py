from enum import IntEnum

import pygame
#from pygame.locals import *
#from OpenGL.GL import *
#from OpenGL.GLU import *

window_height = 600
window_width = 800


pygame.init()
GAMEDISPLAY = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Connect Four')
CLOCK = pygame.time.Clock()

class Player(IntEnum):
    Player_One = 0
    Player_Two = 1

tile_amount_y = 6
tile_amount_x = 7
board = []
while len(board) < tile_amount_x:
    column = []
    while len(column) < tile_amount_y:
        column.append(' ')
    board.append(column)

#reserve windows space for ui
y_offset = int(0.1 * window_height)
x_offset = int(0.2 * window_width)
board_width = window_width - 2 * x_offset
board_height = window_height - 2 * y_offset
tile_width = board_width / tile_amount_x
tile_height = board_height / tile_amount_y

print(f'y offset: {y_offset}, x offset: {x_offset}')
print(f'board width: {board_width}, board height: {board_height}')
print(f'tile width: {tile_width}, tile height: {tile_height}')
print(f'tile amount x: {tile_amount_x}')


yellow = (150, 50, 0)
red = (255, 0, 0)

    
def drawboard():
    """ print(f'|{board[0][5]}|{board[1][5]}|{board[2][5]}|{board[3][5]}|{board[4][5]}|{board[5][5]}|{board[6][5]}|')
    print(f'|{board[0][4]}|{board[1][4]}|{board[2][4]}|{board[3][4]}|{board[4][4]}|{board[5][4]}|{board[6][4]}|')
    print(f'|{board[0][3]}|{board[1][3]}|{board[2][3]}|{board[3][3]}|{board[4][3]}|{board[5][3]}|{board[6][3]}|')
    print(f'|{board[0][2]}|{board[1][2]}|{board[2][2]}|{board[3][2]}|{board[4][2]}|{board[5][2]}|{board[6][2]}|')
    print(f'|{board[0][1]}|{board[1][1]}|{board[2][1]}|{board[3][1]}|{board[4][1]}|{board[5][1]}|{board[6][1]}|')
    print(f'|{board[0][0]}|{board[1][0]}|{board[2][0]}|{board[3][0]}|{board[4][0]}|{board[5][0]}|{board[6][0]}|')
    print('---------------')
    print('|0|1|2|3|4|5|6|') """
    GAMEDISPLAY.fill(blue)

    #coords = [10, 10, 10, 10]
    #pygame.draw.rect(GAMEDISPLAY, red, coords)
    

    x = 0
    while x < tile_amount_x:
        y = 0
        while y < tile_amount_y:
            color = white
            if board[x][y] == 'X':
                color = red
            elif board[x][y] == 'O':
                color = yellow
            else:
                y += 1
                continue
            coords = [x_offset + x * tile_width, window_height - y_offset - (y + 1) * tile_height, tile_width, tile_height]
            pygame.draw.rect(GAMEDISPLAY, color, coords)
            y += 1
        x += 1
    pygame.display.update()

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
    while(i < tile_amount_y):
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
    while(x + i < len(board) and y + i < tile_amount_y):
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
    while(x + i < tile_amount_x and y - i >= 0):
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
    while(i < tile_amount_y):
        win = win or fourinarow(i)
        i += 1
    i = 0
    while(i < tile_amount_x):
        win = win or fourinacolumn(i)
        i += 1
    y = tile_amount_y - 4
    x = 0
    while(y >= 0):
        win = win or fourindiagonalrising(x, y)
        y = y - 1
    y = 0
    while(x <= tile_amount_x - 4):
        win = win or fourindiagonalrising(x, y)
        x = x + 1
    y = 3
    x = 0
    while(y < tile_amount_y):
        win = win or fourindiagonalfalling(x, y)
        y = y + 1
    y = tile_amount_y - 1
    while(x <= tile_amount_x - 4):
        win = win or fourindiagonalfalling(x, y)
        x = x + 1
    
    return win

def isInputValid(value):
    return (value.isnumeric() and (int(value) >= 0 and int(value) < 7))

playernames = ['Player One', 'Player Two']

def maketurn(player, column):
    i = 0
    while(i < len(board[column])):
        if(board[column][i] == ' '):
            if(player == Player.Player_One):
                board[column][i] = 'O'
            else:
                board[column][i] = 'X'
            return True
        i += 1
    else:
        print('Column already full. Chose another one')
        return False


turn = Player.Player_Two
userquit = False

blue = (0, 0, 200)
black = (0, 0, 0)
white = (255, 255, 255)
valid_move = False

while(not gameOver() and not userquit):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            userquit = True
            break
        elif event.type == pygame.KEYUP:
            if event.key == 48:
                valid_move = maketurn(turn, 0)
            elif event.key == 49:
                valid_move = maketurn(turn, 1)
            elif event.key == 50:
                valid_move = maketurn(turn, 2)
            elif event.key == 51:
                valid_move = maketurn(turn, 3)
            elif event.key == 52:
                valid_move = maketurn(turn, 4)
            elif event.key == 53:
                valid_move = maketurn(turn, 5)
            elif event.key == 54:
                valid_move = maketurn(turn, 6)
        #else:
            #print(event)
    CLOCK.tick(60)
    if valid_move:
        turn = (turn+1)%2
        valid_move = False
    drawboard()
#print(f'{playernames[turn]} wins!')
pygame.quit()
quit()
