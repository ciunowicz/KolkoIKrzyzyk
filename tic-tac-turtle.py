import turtle
import tkinter as tk
from MinMax import *
import math
import random
import time


rows, cols = (3, 3)
g_board = [[0]*cols for i in range(rows)]
board2 = [[0]*cols for i in range(rows)]
end_game = False
PLAYER = 1
OPPONENT = 2
winner = 0

screen = turtle.Screen()
screen.setup(600,600)
screen.title("Tic Tac Toe")
screen.setworldcoordinates(-5,-5,5,5)
screen.bgcolor('light gray')
screen.tracer(0,0)
turtle.hideturtle()
canvas = screen.getcanvas()

canvas.pack()


def left_move(board):
    tab = []
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
                tab.append(j + (cols * i))
    
    return tab

def check_win(board, player):
# cols win    
    global winner
    
    for i in range(rows):
        row = 0
        for j in range(cols):
            if board[j][i] == player:
                row+=1 
        if row == cols:
            winner = player
            return True
# row win
    for i in range(rows):
        row = 0
        for j in range(cols):
            if board[i][j] == player:
                row+=1 
        if row == rows:
            winner = player
            return True
 # diagonal   
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            winner = player
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            winner = player
            return True
    
    return False

def no_move(board):

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 0:
               return False
    return True

def comp_move(board):
    num = random.choice(left_move(board))

    init_temp_array(board2)
    bestMove = findBestMove(board2)
 
    num = (bestMove[1] + (bestMove[0]*cols))
    
    return num



def print_winner():

    if end_game:
        print()
        style = ('Courier', 38, 'normal')
        turtle.penup()
        turtle.goto(0,4)
        turtle.color("magenta")

        if winner == PLAYER:
            turtle.write('Wygrałeś', font=style, align='center')
        elif winner == 0:
            turtle.write('Remis', font=style, align='center')
        else:
            turtle.write('Przegrałeś', font=style, align='center')
        canvas.itemconfig(win1, state="normal")

def set_move(numer,board,player):
    x = math.floor(numer / cols)
    y = (numer % rows)
    board[x][y] = player


def init_temp_array(board):
    global g_board
    
    for i in range(rows):
        for j in range(cols):
            if g_board[i][j] == 0:
                board[i][j] = 0
            elif  g_board[i][j] == PLAYER:
                board[i][j] = PLAYER
            elif  g_board[i][j] == OPPONENT:
                board[i][j] = OPPONENT
    return board       




def draw_board():
    turtle.pencolor('black')
    turtle.pensize(8)
    turtle.up()
    turtle.goto(-3,-1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-3,1)
    turtle.seth(0)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(-1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)
    turtle.up()
    turtle.goto(1,-3)
    turtle.seth(90)
    turtle.down()
    turtle.fd(6)

def draw_circle(x,y):
    turtle.up()
    
    turtle.goto(x,y-0.5)
    turtle.seth(0)
    turtle.color('red')
    turtle.down()
    turtle.circle(0.5, steps=100)

def draw_x(x,y):
    turtle.color('darkgreen')
    turtle.up()
    turtle.goto(x-0.5,y-0.5)
    turtle.down()
    turtle.goto(x+0.5,y+0.5)
    turtle.up()
    turtle.goto(x-0.5,y+0.5)
    turtle.down()
    turtle.goto(x+0.5,y-0.5)
    
def draw_piece(i,j,p):
    if p==0: return
    x,y = 2*(j-1), -2*(i-1)
    if p==PLAYER:
        draw_x(x,y)
    else:
        draw_circle(x,y)
    
def draw(b):
    draw_board()
    for i in range(3):
        for j in range(3):
            draw_piece(i,j,b[i][j])
    screen.update()




def play(x,y):
    global turn, end_game

    if(end_game == True):
        return

    i = 3-int(y+5)//2
    j = int(x+5)//2 - 1
    if i>2 or j>2 or i<0 or j<0 or g_board[i][j]!=0: return

    num = (j + (i*cols))

    if num not in  left_move(g_board):
        return

    set_move(num,g_board,PLAYER)  
    draw(g_board)

    if check_win(g_board,PLAYER) or no_move(g_board):
        end_game = True
    else:
        z = comp_move(g_board)       
        set_move(z,g_board,OPPONENT)
        
        if check_win(g_board,OPPONENT) or no_move(g_board):
            end_game = True

    time.sleep(1)
    
    draw(g_board)
    
    print_winner()
    

def nowagra():
    global end_game, g_board, board2, winner
   
    canvas.itemconfig(win1, state="hidden")
    end_game = False
    winner = 0
    for i in range(rows):
        for j in range(cols):
            g_board[i][j] = 0
            board2[i][j] = 0
    turtle.clear()
    umplayer  = random.randint(1,2)
    
    if umplayer == OPPONENT:
        z = random.randint(0,8)
        set_move(z,g_board,OPPONENT)
    draw(g_board)


button = tk.Button(canvas.master, text="Nowa Gra", command=nowagra)
win1 = canvas.create_window(-220, -260, window=button)
canvas.itemconfig(win1, width=100)
canvas.itemconfig(win1, state="hidden")

draw(g_board)

nowagra()
#draw(g_board)
screen.onclick(play)

turtle.mainloop()
