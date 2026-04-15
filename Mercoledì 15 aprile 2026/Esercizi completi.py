#Esercizio 1


""" '''numero = int(input("Inserisci un numero: "))

if numero % 2 == 0:
    print("Il numero è pari")
else:
    print("Il numero è dispari")
    
    
    
#Esercizio 2


while True:
    n = int(input("Inserisci un numero intero positivo: "))

    if n < 0:
        print("Numero non valido")
        continue

    for i in range(n, -1, -1):
        print(i)
        
        
        
#Esercizio 3


numeri = input("Inserisci numeri separati da spazio: ").split()

for i in numeri:
    numero = int(i)
    print(numero ** 2)''' """
    


    
#Esercizio 4


numeri = input("Inserisci numeri separati da spazio: ").split()

if len(numeri) == 0:
    print("Lista Vuota")
else:
    for i in range(len(numeri)):
        numeri[i] = int(numeri[i])

    massimo = numeri[0]
    i = 0
    conteggio = 0

    for numero in numeri:
        if numero > massimo:
            massimo = numero

    while i < len(numeri):
        conteggio += 1
        i += 1

    print(massimo)
    print(conteggio)
    
    
    





        
    
    
    
    
    