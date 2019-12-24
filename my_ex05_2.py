def check_fermat():
    a = int(input("Inserisci il valore di a \n"))
    b = int(input("Inserisci il valore di b \n"))
    c = int(input("Inserisci il valore di c \n"))
    n = int(input("Inserisci il valore di n \n"))
    if n > 2 and a ** n + b ** n == c ** n:
        print("Holy smokes Fermat was wrong")
    else:
        print("Fermat was right")


check_fermat()
