import tkinter as tk
import tkinter.messagebox as tkm
import random 
def button_click(event):
    btn=event.widget
    txt=btn["text"]
    if txt=="=":
        q=entry.get()
        q1=q.replace("×","*")
        q2=q1.replace("÷","/")
        a=eval(q2)
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)
    else:
        entry.insert(tk.END,txt)
def button_click2(event):
    btn=event.widget
    txt=btn["text"]
    if "昼" in txt:
        hiru=["マック","カレー","なし","いも虫","ステーキ","パスタ","チキン","パイモン",]
        num=random.randint(0,7)
        entry.delete(0,tk.END)
        entry.insert(tk.END,hiru[num])

root=tk.Tk()
root.title("電卓")
root.geometry("220x550")
x=0
y=1
for i in range(9,-1,-1):
    btn=tk.Button(root,
                    text=i,
                    width=4,
                    height=2,
                    font=("Times New Roman", 20)
    )
    btn.grid(row=y,column=x,)
    btn.bind("<1>",button_click)
    if y==1 or y==2 or y==3:
        x+=1
    if x==3:
        x=0
        y+=1
entry=tk.Entry(justify="right",width=10,font=("Times New Roman",30))
entry.grid(row=0,column=0,columnspan=3)
btn2=tk.Button(root,text="+",width=4,height=2,font=("Times New Roman", 20))
btn2.grid(row=4,column=1)
btn2.bind("<1>",button_click)
btn3=tk.Button(root,text="=",width=4,height=2,font=("Times New Roman", 20))
btn3.grid(row=4,column=2)
btn3.bind("<1>",button_click)
btn4=tk.Button(root,text="-",width=4,height=2,font=("Times New Roman", 20))
btn4.grid(row=5,column=0)
btn4.bind("<1>",button_click)
btn5=tk.Button(root,text="×",width=4,height=2,font=("Times New Roman", 20))
btn5.grid(row=5,column=1)
btn5.bind("<1>",button_click)
btn6=tk.Button(root,text="÷",width=4,height=2,font=("Times New Roman", 20))
btn6.grid(row=5,column=2)
btn6.bind("<1>",button_click)
btn7=tk.Button(root,text="昼",width=4,height=2,font=("Times New Roman", 20))
btn7.grid(row=6,column=0)
btn7.bind("<1>",button_click2)

root.mainloop()