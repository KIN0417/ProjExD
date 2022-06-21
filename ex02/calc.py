import tkinter as tk
import tkinter.messagebox as tkm
def button_click(event):
    btn=event.widget
    txt=btn["text"]
    if txt!="=":
        entry.insert(tk.END,txt)
    else:
        q=entry.get()
        a=eval(q)
        entry.delete(0,tk.END)
        entry.insert(tk.END,a)
root=tk.Tk()
root.geometry("300x570")
x=0
y=1
for i in range(9,-1,-1):
    btn=tk.Button(root,
                    text=i,
                    width=4,
                    height=2,
                    font=("Times New Roman", 30)
    )
    btn.grid(row=y,column=x,)
    btn.bind("<1>",button_click)
    if y==1 or y==2 or y==3:
        x+=1
    if x==3:
        x=0
        y+=1
entry=tk.Entry(justify="right",width=10,font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)
btn2=tk.Button(root,text="+",width=4,height=2,font=("Times New Roman", 30))
btn2.grid(row=4,column=1)
btn2.bind("<1>",button_click)
btn3=tk.Button(root,text="=",width=4,height=2,font=("Times New Roman", 30))
btn3.grid(row=4,column=2)
btn3.bind("<1>",button_click)

root.mainloop()