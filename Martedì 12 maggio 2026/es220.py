import numpy as np


# Creazione matrice 6x6 con numeri casuali tra 1 e 100

matrice = np.random.randint(1, 101, (6, 6))


print("Matrice originale:")
print(matrice)



# Estrazione della sotto-matrice centrale 4x4

sotto_matrice = matrice[1:5, 1:5]

print("\nSotto_matrice centrale 4x4:")
print(sotto_matrice)



# Inversione delle righe

matrice_invertita = sotto_matrice[::-1]

print("\nMatrice con righe invertite:")
print(matrice_invertita)



# Estrazione della diagonale principale

diagonale = np.diag(matrice_invertita)

print("\nDiagonale principale:")
print(diagonale)



# Sostituzione dei multipli di 3 con -1

matrice_modificata = matrice_invertita.copy()    # ho messo copy per evitare di modificare la matrice_invertita originale
matrice_modificata[matrice_modificata % 3 == 0] = -1

print("\nMatrice invertita modificata:")
print(matrice_modificata)



 


