import random
import tkinter as tk

win = tk.Tk()
win.title("2048")
win.geometry("480x516")
win.minsize(480,516)
win.maxsize(480,516)

def start_game():
    global game,random_number
    game = [[0,0,2,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    random_number = [2,2,2,2,2,2,2,4]

    """tmp = [random.randint(0,3),random.randint(0,3)]
    game[tmp[0]][tmp[1]] = random_number[random.randint(0,7)]

    new_x,new_y = random.randint(0,3),random.randint(0,3)
    while new_x == tmp[0] or new_y == tmp[1]:
        new_x,new_y = random.randint(0,3),random.randint(0,3)
    game[new_x][new_y] = random_number[random.randint(0,7)]"""

    b_quit.destroy()
    b_start_game.destroy()

    win.bind('<Left>',move_left)
    win.bind('<Right>',move_right)
    win.bind('<Up>',move_up)
    win.bind('<Down>',move_down)

    main_game()

def no_move():
    pass

def move_left(arg):
    for x in range(len(game)):
        for y in range(len(game[0])):
            if game[x][y] != 0:
                if y != 0:
                    t = y
                    while t >= 1 or game[x][t] == game[x][y] or game[x][t] in dico_colors.keys() and game[x][t] != game[x][y]:
                        if t == 0:
                            break
                        else:
                            t-=1
                    if game[x][t] == game[x][y]:
                        game[x][t] = game[x][t] * 2
                        game[x][y] = 0
                    elif game[x][t] != 0:
                        if game[x][t] != game[x][y-1]:
                            game[x][t+1] = game[x][y]
                            game[x][y] = 0
                    elif t == 0:
                        game[x][t] = game[x][y]
                        game[x][y] = 0
                    main_game()

def move_right(arg):
    for x in range(len(game)):
        for y in range(len(game[0])):
            if game[x][y] != 0:
                if y != 3:
                    t = y
                    while t <= 2 or game[x][t] == game[x][y] or game[x][t] in dico_colors.keys() and game[x][t] != game[x][y]:
                        if t == 3:
                            break
                        else:
                            t+=1
                    if game[x][t] == game[x][y]:
                        game[x][t] = game[x][t] * 2
                        game[x][y] = 0
                    elif game[x][t] != 0:
                        if game[x][t] != game[x][y+1]:
                            game[x][t-1] = game[x][y]
                            game[x][y] = 0
                    elif t == 3:
                        game[x][t] = game[x][y]
                        game[x][y] = 0
                    main_game()

def move_up(arg):
    pass

def move_down(arg):
    pass

dico_colors = {2:"#EEE4DA",4:"#EDE0C8",8:"#F2B179",16:"#F59563",32:"#F67C60",64:"#F65E3B",128:"#EDCF73",256:"#EDCC62",512:"#EDC850",1024:"#EDC53F",2048:"#EDC22D"}
s_b = []
s_main = False
def main_game():
    global s_main,s_b
    if s_main:
        for elem in s_b:
            elem.destroy()
        s_b = []
        s_main = False
    for x in range(len(game)):
        for y in range(len(game[0])):
            if game[x][y] == 0:
                b_tmp = tk.Button(win,text="",font=('Segoe UI Black',"26"),command=None,width=5,height=2)
                b_tmp.grid(row=x,column=y)
                """b_tmp.append(s_b)"""
            else:
                b_tmp = tk.Button(win,text=str(game[x][y]),font=('Segoe UI Black',"26"),bg=dico_colors[game[x][y]],command=None,width=5,height=2)
                b_tmp.grid(row=x,column=y)
                """b_tmp.append(s_b)"""
    s_main = True

def main():
    global b_start_game,b_quit
    b_start_game = tk.Button(win,text="Start Game",font=('Segoe UI Black',"26"),command=start_game)
    b_quit = tk.Button(win,text="Quit",font=('Segoe UI Black',"26"),command=win.destroy)

    b_start_game.grid(row=0,column=0,padx=135,pady=105)
    b_quit.grid(row=1,column=0)

if __name__ == "__main__":
    main()

win.mainloop()