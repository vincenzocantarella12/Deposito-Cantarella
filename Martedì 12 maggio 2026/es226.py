import numpy as np

# Array di 12 numeri equidistanti tra 0 e 1

array = np.linspace(0, 1, 12)

print("Array originale:")
print(array)


# Cambio forma in matrice 3x4

matrice = array.reshape(3, 4)

print("\nMatrice 3x4:")
print(matrice)


# Matrice casuale 3x4 con numeri tra 0 e 1

matrice_random = np.random.rand(3, 4)

print("\nMatrice casuale:")
print(matrice_random)



# Somma degli elementi


somma_matrice = np.sum(matrice)
somma_random = np.sum(matrice_random)

print("\nSomma elementi matrice linspace:")
print(somma_matrice)

print("\nSomma elementi matrice casuale:")
print(somma_random)