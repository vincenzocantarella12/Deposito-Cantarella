numeri_primi = []
conteggio = 0

while conteggio < 5:
    numero = int(input("Inserisci un numero: "))

    if numero < 2:
        print("Il numero non è primo")
        continue

    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        numeri_primi.append(numero)
        conteggio += 1
        print("Il numero è primo")
    else:
        print("Il numero non è primo")

print("Numeri primi trovati:", numeri_primi)
