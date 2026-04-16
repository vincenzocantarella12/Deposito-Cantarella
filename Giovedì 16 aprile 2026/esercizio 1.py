#esercizio 1 pagina 96   #funzione random per generare numeri casuali  # usare break per uscire da un ciclo infinito
    


import random

def indovina_numero():
    numero = random.randint(1, 100)
    tentativi = 0

    while True:
        tentativi += 1
        n = int(input("Indovina il numero (1-100): "))

        if n < numero:
            print("Troppo basso")
        elif n > numero:
            print("Troppo alto")
        else:
            print(f"Hai indovinato in {tentativi} tentativi!")
            break

indovina_numero()




""" #esercizio 2 sequenza di Fibonacci

n = int(input("Quanti numeri della sequenza di Fibonacci vuoi vedere? "))

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    seq = [0, 1]
    for i in range(2, n):
        next_num = seq[i-1] + seq[i-2]
        seq.append(next_num)

    return seq
print(fibonacci(n)) """











