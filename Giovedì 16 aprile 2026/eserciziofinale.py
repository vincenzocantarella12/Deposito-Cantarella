#Esercitazione 

import random

# 1 funzione per ottenere  un numero intero positivo 
def numero_intero_positivo():
    n = 0
    while n <= 0:
        n = int(input("Inserisci un numero intero positivo n: "))
        if n <= 0:
            print("Errore: il numero deve essere positivo!")
    return n


# 2 funzione per generare una lista di numeri casuali

def genera_lista_casuale(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(1, 100))
    return lista

# 3 funzione per sommare i numeri pari in una lista


def somma_numeri_pari(lista):
    somma = 0
    for num in lista:
        if num % 2 == 0:
            somma += num
    print("La somma dei numeri pari è:", somma)
    return somma

# 4 funzione per stampare i numeri dispari in una lista


def stampa_numeri_dispari(lista):
    print("I numeri dispari nella lista sono:")
    for num in lista:
        if num % 2 != 0:
            print(num, end=" ")
    print()
    
    
# 5 funzione per controllare se un numero è primo

def e_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True 

# 6 funzione per stampare i numeri primi in una lista

def stampa_numeri_primi(lista):
    print("I numeri primi nella lista sono:")
    for num in lista:
        if e_primo(num):
            print(num, end=" ")
    print()
    
# 7 funzione per sommare tutti i numeri in una lista e controllare se la somma è un numero primo

def somma_e_controlla_primo(lista):
    somma = sum(lista)
    print("La somma totale è:", somma)
    if e_primo(somma):
        print("La somma è un numero primo.")
    else:
        print("La somma non è un numero primo.")
    return somma 

# 8 Menù per eseguire le funzioni

def mostra_menu():
    print("Menu:")
    print("1. Genera una lista di numeri casuali")
    print("2. Somma dei numeri pari")
    print("3. Stampa dei numeri dispari")
    print("4. Stampa dei numeri primi")
    print("5. Somma totale e controllo se è primo")
    print("6. Esci") 
    
    
    

    
    

