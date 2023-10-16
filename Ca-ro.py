
from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        t = 0 if player == players[0] else 1

        buttons[row][column]['text'] = player
        if check_winner() is False:
            player = players[1-t]
            label.config(text=(players[1-t]+" turn"))
        elif check_winner() == "Tie":
            drawTie()
            label.config(text="Tie!")
        else:
            x1,y1,x2,y2,x3,y3 = check_winner()
            drawWin(x1,y1,x2,y2,x3,y3)
            label.config(text=(players[t]+" wins"))

def drawWin(x1,y1,x2,y2,x3,y3):
    buttons[x1][y1].config(bg="green")
    buttons[x2][y2].config(bg="green")
    buttons[x3][y3].config(bg="green")

def drawTie():
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(bg="yellow")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return row,0,row,1,row,2

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return column,0,column,1,column,2
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return 0,0,1,1,2,2

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return 0,2,1,1,2,0

    elif empty_spaces() is False:
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 0

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces +=1

    if spaces == 9:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg=BUTTON_COLOR)

def instruct_frame():
    newwindow = Toplevel(window)
    newwindow.title("Instruction")
    newwindow.geometry("450x300")
    
    l = Label(newwindow,text="Read Me")
    l.config(font =("Courier", 14))
    l.pack()

    T = Text(newwindow, height = 10, width = 40)
    T.pack()
    

    instruct_text = """Each person has one turn to mark, the player will win when they create a vertical, horizontal or diagonal line."""
    
    T.insert(END, instruct_text)

    b2 = Button(newwindow, text = "Exit",command = newwindow.destroy) 
    b2.pack()

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
frame = Frame(window)
frame.pack()
label = Label(frame,text=player + " turn", font=('consolas',40))
label.pack(side="top")
reset_button = Button(frame,text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="left")
instruct_button = Button(frame,text="Instruction", font=('consolas',20),command=instruct_frame)
instruct_button.pack(side="right")
frame2 = Frame(window)
frame2.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame2, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
BUTTON_COLOR = str(buttons[0][0].cget("bg"))