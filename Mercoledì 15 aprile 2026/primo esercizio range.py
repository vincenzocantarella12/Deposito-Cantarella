ripeti = "si"

while ripeti == "si":
    numero = int(input("Inserisci un numero: "))

    for i in range(numero, -1, -1):
        print(i)

    ripeti = input("Vuoi ripetere? (si/no): ")
    
    
    