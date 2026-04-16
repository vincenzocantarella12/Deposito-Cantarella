""" """ def saluta(nome):
    print("Ciao",nome)
    saluta ("Vincenzo")
    
    
    def somma(a,b):
        risultato = a + b
        print("La somma è:", risultato)
        somma(5, 3)
        
        def quadrato(numero)
            return numero*numero
        risultato  """
        
        
        
def saluta(nome:str, messaggio="Ciao"):
    print(f"{messaggio}, {nome}!")
            
    saluta("Vincenzo")
    saluta("Luigi", messaggio="Buongiorno") """
    
    
    #esercizio 1 pagina 96   #funzione random per generare numeri casuali  # usare break per uscire da un ciclo infinito
    
    
import random

def indovina_numero():
    numero = random.randint(1, 100)
    tentativi = 0

    while True:
        tentativi += 1
        n = int(input("Indovina il numero (1-100): "))

        if n < numero:
            print("Più basso")
        elif n > numero:
            print("Più alto")
        else:
            print(f"Hai indovinato in {tentativi} tentativi")
            break

indovina_numero()




    
    
    
    
        
        
    