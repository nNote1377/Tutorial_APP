#importowanie przykładowych rozszerzeń
import math #rozszerzona matematyka
import tkinter #graficzne GUI
import random #moduł pozwalający tworzyć liczby pseudolosowe
import kalkulator as kalk #importowanie podprogramu
import tkinter as tk
from tkinter import ttk

rozdzial=0

win = tk.Tk()
win.title("Tutorial_APP")
aLabel = ttk.Label(win, text="Tekst bez zmiany")
aLabel.grid(column=0, row=0)

#Button Click Event Function
def clickMe1():
    aLabel.configure(foreground='red')
    aLabel.configure(text="Wybrano")
    kalk.licz()
def clickMe2():
    aLabel.configure(foreground='red')
    aLabel.configure(text="Wybrano")
    rozdzial=int(2)

#Adding a Button
action = ttk.Button(win, text="Kalkulator", command=clickMe1)
action.grid(column=0, row=1)
action = ttk.Button(win, text="Drugi program", command=clickMe2)
action.grid(column=1, row=1)

if rozdzial == 1:
    kalk.licz()
elif rozdzial == 2:
    wartosc1=int(input('Wpisz 1. liczbe '))
    #Dzięki poleceniu "input możemy podać wartość zmiennej podczas działania programu"
    wartosc2=int(random.randint(-10, 10))
    #losujemy liczbę od -10 do 10 używając modułu random.randint(-10, 10)
    print(wartosc1)#Drukujemy wartość pierwszej zmiennej
    print(wartosc2)#Drukkujemy wartość drugiej zmiennej
    print(wartosc1*wartosc2)#Drukujemy iloczyn naszych zmienncy

win.mainloop()