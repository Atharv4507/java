from tkinter import *
# create a root window.
# listbox
top = Tk()

# create listbox object
listbox = Listbox(top, height=10, width=15, bg="grey",
                  activestyle='dotbox', font="Helvetica", fg="yellow")

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text=" FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# pack the widgets
label.pack()
listbox.pack()


# Display untill User
# exits themselves.
top.mainloop()


# from tkinter import *
# button
top = Tk()
btn = Button(top, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
top.title('Hello Python')
top.geometry("300x200+10+10")
top.mainloop()


# from tkinter import *
# lable
window = Tk()
lbl = Label(window, text="This is Label widget",
            fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()

# from tkinter import *

# canvas
root = Tk()

C = Canvas(root, bg="yellow",
           height=250, width=300)

line = C.create_line(108, 120,
                     320, 40,
                     fill="green")

arc = C.create_arc(180, 150, 80,
                   210, start=0,
                   extent=220,
                   fill="red")

oval = C.create_oval(80, 30, 140,
                     150,
                     fill="blue")

C.pack()
mainloop()


# from tkinter import *
# Entry
root = Tk()
root.geometry("300x200")

w = Label(root, text='GeeksForGeeks', font="50")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(root, text="Tutorial",
                      variable=Checkbutton1,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10)

Button2 = Checkbutton(root, text = "Student",
					variable = Checkbutton2,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

Button3 = Checkbutton(root, text = "Courses",
					variable = Checkbutton3,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

Button1.pack()
Button2.pack()
Button3.pack()

mainloop()


# frame
# from tkinter import *
root = Tk()
root.geometry("300x150")

w = Label(root, text='GeeksForGeeks', font="50")
w.pack()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)

b1_button = Button(frame, text="Geeks1", fg="red")
b1_button.pack(side=LEFT)

b2_button = Button(frame, text="Geeks2", fg="brown")
b2_button.pack(side=LEFT)

b3_button = Button(frame, text ="Geeks3", fg ="blue")
b3_button.pack( side = LEFT )

b4_button = Button(bottomframe, text ="Geeks4", fg ="green")
b4_button.pack( side = BOTTOM)

b5_button = Button(bottomframe, text ="Geeks5", fg ="green")
b5_button.pack( side = BOTTOM)

b6_button = Button(bottomframe, text ="Geeks6", fg ="green")
b6_button.pack( side = BOTTOM)

root.mainloop()


# from tkinter import *
# menubutton

root = Tk()
root.geometry("300x200")

w = Label(root, text='GeeksForGeeks', font="50")
w.pack()

menubutton = Menubutton(root, text="Menu")

menubutton.menu = Menu(menubutton)
menubutton["menu"] = menubutton.menu

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

menubutton.menu.add_checkbutton(label="Courses",
                                variable=var1)
menubutton.menu.add_checkbutton(label="Students",
                                variable=var2)
menubutton.menu.add_checkbutton(label = "Careers",
								variable =var3)

menubutton.pack()
root.mainloop()
