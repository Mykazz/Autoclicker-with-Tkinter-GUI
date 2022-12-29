from pynput import mouse
from tkinter import *
from tkinter.font import Font
import customtkinter
import win32api
import pyautogui
import pyautogui


Langas = Tk()
Langas.title("Autoclicker")
Langas.geometry("300x215")
Langas.configure(bg="#141414")
Langas.resizable(width=False, height=False)
pavadinimoFont = Font(family="Brush Script MT", 
                      size="48",
                      weight="bold", 
                      slant="italic")
a = 0


def btn(x, y, text, bcolor, fcolor, cmd):

    def on_enter(e):
        mybutton['background'] = bcolor
        mybutton['foreground'] = fcolor

    def on_leave(e):
        mybutton['background'] = fcolor
        mybutton['foreground'] = bcolor

    mybutton = Button(Langas, width=42, height=2, text=text,
                      fg=bcolor, bg=fcolor, border=0, 
                      activebackground=bcolor, 
                      activeforeground=fcolor, 
                      command=cmd)
    mybutton.bind("<Enter>", on_enter)
    mybutton.bind("<Leave>", on_leave)
    mybutton.place(x=x, y=y)


def periodically_called():
    global x, y, a
    a = win32api.GetAsyncKeyState(0x01)
    print("ss")
    if a < 0:
        print("dfsdfs")
        x, y = pyautogui.position()
        a = 1
    else:
        Langas.after(10, periodically_called)


def vykdymas1():
    global x, y, delay
    a = win32api.GetAsyncKeyState(0x01)
    pyautogui.click(x, y)
    print("ss")
    pyautogui.sleep(delay)
    if a < 0:
        print("baigta")
        return
    else:
        Langas.after(10, vykdymas1)

def vykdymas2():
    global x, y, delay,laikas
    t =0
    while t<laikas:
        a = win32api.GetAsyncKeyState(0x01)
        pyautogui.click(x, y)
        pyautogui.sleep(delay)
        t+=delay
        print("ss")
        if a<0:
            break


def gaunamKieki():
    global delay,laikas
    try:
        
        float(entry1.get())

        print("Number")

        delay = float(entry1.get())

    except ValueError:
        delay = "wrong"

    try:
        float(entry2.get())

        laikas = float(entry2.get())

        print("Number")
    except ValueError:
        laikas = "nera"

    if (laikas == 'nera' and delay != 'wrong' and a):
        vykdymas1()

    elif (delay != 'wrong' and a):
        vykdymas2()

Pavadinimas = customtkinter.CTkLabel(
    Langas, text="Autoclicker", 
    font=('Jazz LETJazz LET', 20))
Pavadinimas.place(x=105, y=10)

entry1 = customtkinter.CTkEntry(
    Langas, width=100, placeholder_text="Delay",
     justify=CENTER)
entry1.place(x=100, y=45)

entry2 = customtkinter.CTkEntry(
    Langas, width=100, 
    placeholder_text="Laikas", 
    justify=CENTER)
entry2.place(x=100, y=80)


btn(0, 110, 'VIETA', '#ffcc66', '#141414', periodically_called)
btn(0, 150, 'PRADĖTI', '#f86263', '#141414', gaunamKieki)

LegalT = customtkinter.CTkLabel(
    Langas,
    text="Sukurta edukaciniais tikslais", 
    font=('Parkavenue', 10))
LegalT.place(x=90, y=190)


Langas.mainloop()
