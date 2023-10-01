from tkinter import *
from string import ascii_letters
import os
import sys
# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            print("scvalue is "+scvalue.get(), 'screenvalue is '+screen.get())
            value = eval(scvalue.get())
            scvalue.set(value)
            screen.update()

    elif (text == "C"):
        scvalue.set("")

    else:
        scvalue.set(scvalue.get() + text)

        #
        for alpha in ascii_letters:
            if (alpha in scvalue.get()):
                scvalue.set(scvalue.get().replace(alpha, ""))


root = Tk()


root.geometry("550x600")

root.maxsize(550, 600)


root.title("Calculator")

root.wm_iconbitmap(resource_path("Calculator-icon.ico"))


# Sc value

scvalue = StringVar()
scvalue.set("")

# screen

screen = Entry(root, textvariable=scvalue, font="comic 45 ", borderwidth=10,
               relief=SUNKEN, background="lightblue", state="readonly")
# ,background="lightblue"
screen.pack(fill=X, ipadx=5, ipady=3)

# Buttons

f = Frame(root)

b = Button(f, text="C", font="comic 30")
b.bind("<Button-1>", click)
b.pack(ipadx=240, pady=5)

f.pack(anchor="w", padx=3)

f = Frame(root)

b = Button(f, text="7", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="8", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="9", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="/", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=44)

f.pack(anchor="w", pady=5, padx=3)

f = Frame(root)

b = Button(f, text="4", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="5", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="6", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="*", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=41)

f.pack(anchor="w", pady=5, padx=3)

f = Frame(root)

b = Button(f, text="1", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="2", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="3", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=40)

b = Button(f, text="-", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=43)

f.pack(anchor="w", pady=5, padx=3)

f = Frame(root)

b = Button(f, text="0", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=64)

b = Button(f, text=".", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=64)

b = Button(f, text="+", font="comic 30")
b.bind("<Button-1>", click)
b.pack(side=LEFT, ipadx=64)


f.pack(anchor="w", padx=3)

f = Frame(root)

b = Button(f, text="=", font="comic 30")
b.bind("<Button-1>", click)
b.pack(ipadx=244)

f.pack(anchor="w", pady=5)

root.mainloop()
