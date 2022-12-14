from tkinter import *
import random
def next_turn(row, column):
    global player
    if buttons[row][column]['text']=="" and check_winner() is False:
        if player==players[0]:
            buttons[row][column]['text']=player
            if check_winner() is False:
                player=players[1]
                label.config(text=(players[1]+"'S TURN"))
            elif check_winner() is True:
                label.config(text=("'"+players[0]+"' WINS"))
            elif check_winner()=="TIE":
                label.config(text="TIE!")
        else:
            buttons[row][column]['text']=player
            if check_winner() is False:
                player=players[0]
                label.config(text=(players[0]+"'S TURN"))
            elif check_winner() is True:
                label.config(text=("'"+players[1]+"' WINS"))
            elif check_winner()=="TIE":
                label.config(text="TIE!")
def check_winner():
    for row in range(3):
        if buttons[row][0]['text']==buttons[row][1]['text']==buttons[row][2]['text']!="":
            buttons[row][0].config(bg="#006400")
            buttons[row][1].config(bg="#006400")
            buttons[row][2].config(bg="#006400")
            return True
    for column in range(3):
        if buttons[0][column]['text']==buttons[1][column]['text']==buttons[2][column]['text']!="":
            buttons[0][column].config(bg="#006400")
            buttons[1][column].config(bg="#006400")
            buttons[2][column].config(bg="#006400")
            return True
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']!="":
        buttons[0][0].config(bg="#006400")
        buttons[1][1].config(bg="#006400")
        buttons[2][2].config(bg="#006400")
        return True
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']!="":
        buttons[0][2].config(bg="#006400")
        buttons[1][1].config(bg="#006400")
        buttons[2][0].config(bg="#006400")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#9b870c")
        return "TIE"
    else:
        return False
def empty_spaces():
    spaces=9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text']!="":
                spaces-=1
    if spaces==0:
        return False
    else:
        return True
def new_game():
    global player
    player=random.choice(players)
    label.config(text=player+"'S TURN")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg='#1c1c1c', fg='#e6e6e6')
window=Tk()
window.configure(bg='#1c1c1c')
window.title("Tic Tac Toe")
window.iconbitmap('icon.ico')
window.resizable("false", "false")
players=["X","O"]
player=random.choice(players)
buttons=[[0,0,0], [0,0,0], [0,0,0]]
label=Label(text=player+"'S TURN", font=('Showcard Gothic',30), bg='#1c1c1c', fg='#e6e6e6')
label.pack(side="top")
reset_button=Button(text="RESTART", font=('Jetbrains Mono',10), command=new_game, bg='#1c1c1c', fg='#e6e6e6')
reset_button.pack(side="top", pady=7)
frame=Frame(window)
frame.configure(bg='#1c1c1c')
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame, text="",font=('Showcard Gothic',40), width=4, height=1, command=lambda row=row, column=column: next_turn(row,column), bg='#1c1c1c', fg='#e6e6e6')
        buttons[row][column].grid(row=row,column=column)
window.mainloop()