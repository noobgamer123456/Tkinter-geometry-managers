from tkinter import *
import datetime

root = Tk()
root.title('Age Calculator App')
root.geometry('400x300')

frame = Frame(master=root, height=200, width=360, bg='#FAB072')


lbl1 = Label(frame, text="Name", bg="#CA3433", fg='white', width=12)
lbl2 = Label(frame, text="Year", bg="#CA3433", fg='white', width=12)
lbl3 = Label(frame, text="Month", bg="#CA3433", fg='white', width=12)
lbl4 = Label(frame, text="Date", bg="#CA3433", fg='white', width=12)


name_entry = Entry(frame)
year_entry = Entry(frame)
month_entry = Entry(frame)
date_entry = Entry(frame)


def calculate():
    name = name_entry.get()
    year = int(year_entry.get())
    
    today = datetime.date.today()
    age = today.year - year  
    greet = f"Hey {name}"
    message = f"\nYour age is: {age}"
    
  
    textbox.insert(END, greet)
    textbox.insert(END, message)
    
textbox = Text(root, bg="#BEBEBE", fg="black")

btn = Button(root, text="Calculate", command=calculate, bg="red")

frame.place(x=20, y=20)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=50)
year_entry.place(x=150, y=50)
lbl3.place(x=20, y=80)
month_entry.place(x=150, y=80)
lbl4.place(x=20, y=110)
date_entry.place(x=150, y=110)
btn.place(x=140, y=170)
textbox.place(y=250)


root.mainloop()
