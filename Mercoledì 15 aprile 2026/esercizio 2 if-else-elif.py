#Esercizio 2

numero1 = float(input("Inserisci il primo numero: ")) #ho inserito float per i numeri con la virgola
numero2 = float(input("Inserisci il secondo numero: "))
operazione = input("Scegli l'operazione(+, -, *, /): ")


if operazione == "+":
    risultato = numero1 + numero2
    print("Il risultato è: ", risultato)
elif operazione == "-":
    risultato = numero1 - numero2
    print("Il risultato è: ", risultato)
elif operazione == "*":
    risultato = numero1 * numero2
    print("Il risultato è: ", risultato)
elif operazione == "/":
    if numero2 == 0:
        print("Errore: divisione per zero non consentita")
         risultato = numero1 / numero2
    print("Il risultato è: ", risultato)
else:
    print("Operazione non valida")
    
    
    
    
    