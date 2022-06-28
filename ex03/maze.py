import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random

def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global key,cx,cy,mx,my,maze_bg
    if key=="Up" and maze_bg[my-1][mx]==0:
        my-=1
    elif key=="Down" and maze_bg[my+1][mx]==0:
        my+=1
    elif key=="Left" and maze_bg[my][mx-1]==0:
        mx-=1
    elif key=="Right" and maze_bg[my][mx+1]==0:
        mx+=1
    cx,cy=mx*100+50,my*100+50
    canvas.coords("tori",cx,cy)
    if my==gy and mx==gx:
        tkm.showinfo("OME DETOU","GAME CLEAR")
    root.after(100,main_proc)

if __name__=="__main__":
    mx,my=1,1
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()
    maze_bg=mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg)
    tori=tk.PhotoImage(file="fig/5.png")
    cx,cy=mx*100+50,my*100+50
    canvas.create_rectangle(100,100,200,200,fill="green") #スタートを緑に塗る
    gx=random.randint(0,14) #ゴールのｘ座標をランダムに決める
    gy=random.randint(0,8) #ゴールのy座標をランダムに決める
    while maze_bg[gy][gx]==1: #ゴールが壁の場合、決めなおす
        gx=random.randint(0,15)
        gy=random.randint(0,9)
    canvas.create_rectangle(gx*100,gy*100,gx*100+100,gy*100+100,fill="red") #ゴールを赤に塗る
    canvas.create_image(cx,cy,image=tori,tag="tori")
    key=""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop()
