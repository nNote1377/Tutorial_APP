while True:
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgi")
    print("6. Pierwiastek")
    x=str(input('Jaki typ działania chcesz wykonać: '))
    if x=='1':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a+b)
        print( a ,"+", b, "=", c)
    elif x=='2':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a-b)
        print( a ,"-", b, "=", c)
    elif x=='3':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a*b)
        print( a ,"*", b, "=", c)
    elif x=='4':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        if b==0:
            print('Ale ty głupi jesteś!!!')
        else:
            c=float(a/b)
            print( a ,"/", b, "=", c)
    elif x=='5':
        a=float(input('Wpisz 1. liczbe '))
        b=float(input('Wpisz 2. liczbe '))
        c=float(a**b)
        print( a ,"^", b, "=", c)
    elif x=='6':
        a=float(input('Wpisz 1. liczbe '))
        c=float(a**0.5)
        print("√", a, "=", c)
    else:
        print('Ale ty głupi jesteś!!!')
    while True:
        answer = str(input('Uruchomić ponownie? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Zły znak")
    if answer == 'y':
        continue
    else:
        print("Do widzenia")
        break

    