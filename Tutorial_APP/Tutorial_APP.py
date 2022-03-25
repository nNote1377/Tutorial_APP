#importowanie przykładowych rozszerzeń
import math #rozszerzona matematyka
import tkinter #graficzne GUI
import random #moduł pozwalający tworzyć liczby pseudolosowe
import kalkulator as kalk #importowanie podprogramu

print("Program do wyboru:")
print("1. Kalkulator")

rozdzial=int(input("Wpisz nr. rozdiału króry chcesz przetestować: "))
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