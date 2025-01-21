from students import *
from tkinter import *
from tkinter import messagebox

oyna = Tk()
oyna.title("Dasturcha :)")
oyna.geometry("700x600")
oyna.configure(bg="blue")

l = Label(
    text="Talabalarning ma'lumotlarini shakllantiruvchi dastur",
    bg = "aqua",
    font=('arial',18,'bold'),
    fg = "black"
    )
l.place(x=0,y=0,width=700,height=150)



kalit = Entry()
kalit.place(x=50,y=250,width=200, height=40)


qiymat = Entry()
qiymat.place(x=50,y=300,width=200, height=40)



oyna.mainloop()