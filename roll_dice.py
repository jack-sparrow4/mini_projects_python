import random 
import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.title("Dice Roll")
root.config(background = "#FFFFFF")

frame1 = tk.Frame(root)
frame1.grid(row=1, column=1,rowspan =5,columnspan =25, sticky='N'+'S'+'E'+'W')

labelTest = tk.Label(root,text="Dice Roll", font=('Helvetica', 12), fg='red')
myFont = font.Font(weight="bold")
myFont = font.Font(size=24)
labelTest['font']=myFont
labelTest.grid(row=0,column =0,columnspan = 10, sticky='NW'+'NE')

labelTest1 = tk.Label(frame1,text=random.randint(1,6), font=('Helvetica', 12), fg='blue') 
labelTest1.grid(row=2,column =0,columnspan = 10, sticky='NW'+'NE')

def roll_dice():
    labelTest1["text"] = random.randint(1,6)


save_btn=tk.Button(frame1,text="Roll the Dice", command=roll_dice)
save_btn.grid(row=1,column =0,columnspan = 10, sticky='NW'+'NE')
root.mainloop()