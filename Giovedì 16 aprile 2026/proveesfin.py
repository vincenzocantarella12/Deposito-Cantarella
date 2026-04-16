import random

# 1. Funzione per ottenere un numero positivo
def leggi_n():
    n = 0
    while n <= 0:
        n = int(input("Inserisci un numero intero positivo n: "))
        if n <= 0:
            print("Errore: il numero deve essere positivo!")
    return n


# 2. Genera lista casuale
def genera_lista(n):
    return [random.randint(1, n) for _ in range(n)]


# 3. Somma numeri pari
def somma_pari(lista):
    somma = 0
    for num in lista:
        if num % 2 == 0:
            somma += num
    print("Somma dei numeri pari:", somma)
    return somma


# 4. Stampa numeri dispari
def stampa_dispari(lista):
    print("Numeri dispari nella lista:")
    for num in lista:
        if num % 2 != 0:
            print(num, end=" ")
    print()


# 5. Controllo numero primo
def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 6. Stampa numeri primi nella lista
def stampa_primi(lista):
    print("Numeri primi nella lista:")
    for num in lista:
        if is_primo(num):
            print(num, end=" ")
    print()


# 7. Somma totale e controllo se è primo
def somma_totale(lista):
    return sum(lista)


def verifica_somma_prima(lista):
    totale = somma_totale(lista)
    print("Somma totale della lista:", totale)

    if is_primo(totale):
        print("La somma È un numero primo")
    else:
        print("La somma NON è un numero primo")


# MENU
def menu():
    lista = []
    
    while True:
        print("\n===== MENU =====")
        print("1. Inserisci n e genera lista")
        print("2. Somma numeri pari")
        print("3. Stampa numeri dispari")
        print("4. Stampa numeri primi")
        print("5. Verifica se somma totale è primo")
        print("6. Visualizza lista")
        print("0. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            n = leggi_n()
            lista = genera_lista(n)
            print("Lista generata con successo!")

        elif scelta == "2":
            if lista:
                somma_pari(lista)
            else:
                print("Prima genera la lista!")

        elif scelta == "3":
            if lista:
                stampa_dispari(lista)
            else:
                print("Prima genera la lista!")

        elif scelta == "4":
            if lista:
                stampa_primi(lista)
            else:
                print("Prima genera la lista!")

        elif scelta == "5":
            if lista:
                verifica_somma_prima(lista)
            else:
                print("Prima genera la lista!")

        elif scelta == "6":
            print("Lista attuale:", lista)

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida!")


# Avvio programma
menu()