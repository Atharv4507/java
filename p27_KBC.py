from tkinter import*

top = Tk()
top.geometry("720x720")
top.title("KBC")
l = Label(top,text="Let The Game Begine",font=24,justify='left')
li = Listbox(top,borderwidth=5,height=2,width=700,font=24,justify='left',)
li.insert(1,"1.What is the Capital of INDIA?")
l.pack()
li.pack(padx=10,pady=20)

f = Frame(top)
r1 = IntVar()
b = Radiobutton(bg="lightblue",text="1.Delhi",font=24,fg="black",width=50, variable = r1,value = 1,command=SEL,borderwidth=5,justify='left')
b.pack(anchor= W,padx=5,pady=5)
b1 = Radiobutton(bg="lightblue",text="2.Mumbai",font=24,border=5,fg="black",width=50,variable = r1,value = 2,command=SEL,justify='left')
b1.pack(anchor= W,padx=5,pady=5)
b2 = Radiobutton(bg="lightblue",text="3.kolkatta",font=24,border=5,fg="black",width=50,variable = r1,value = 3,command=SEL,justify='left')
b2.pack(anchor= W,padx=5,pady=5)
b3 = Radiobutton(bg="lightblue",text="4.Bengaluru",font=24,border=5,fg="black",width=50,variable = r1,value = 4,command=SEL,justify='left')
b3.pack(anchor= W,padx=5,pady=5)

b4 = Button(background="green",fg="black",text="Next",font="24")
b4.pack(anchor= E,padx=25,pady=65)
f.pack(side=LEFT,pady=20)
top.mainloop()