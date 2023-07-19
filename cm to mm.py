from tkinter import *
window = Tk()
window.title("Cm to mm")
window.minsize(300,100)

start = Label(text="Please Enter the input: ")
start.pack()
i = Entry(width=15)
i.pack()


def buttonclick():
    e = int(i.get())
    c= e*10
    o = Label(text=f"Convertion in mm is {c}mm")
    o.pack()

cal = Button(text = "Convert To mm",command=buttonclick)

cal.pack()
window.mainloop()