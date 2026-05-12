import numpy as np

# indexing e slicing

arrInd = np.arange(1, 6)

# indexing base
print(arrInd[0])  # primo elemento

# slicing
print(arrInd[1:3])  # elementi dall'indice 1 all'indice 2 (escluso l'indice 3)

# boolean indexing
print(arrInd[arrInd > 2])  # elementi maggiori di 2


#indexing e slicing con array multidimensionali

arr2dInd = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
print(arr2dInd[1, 3]) # elemento alla riga 1 e colonna 3 (indice 0-based) # slicing su righe

# slicing su colonne

print("\n")
print(arr2dInd[:2, 0:3]) # tutti gli elementi della colonna 2 (indice 0-based)

# slicing avanzato

arrSlice = np.arange(0,10)

print("\n")
print(arrSlice)

print("\nSlicing base:")
print(arrSlice[2:7]) # elementi dall'indice 2 all'indice 6 (escluso l'indice 7)

print("\nSlicing con step:")
print(arrSlice[1:8:2]) # elementi dall'indice 1 all'indice 7 (escluso l'indice 8) con step di 2

print("\nSlicing con start e stop:")
print(arrSlice[:5])
print(arrSlice[5:])


print("\nSlicing con step negativo:")
print(arrSlice[-5:])
print(arrSlice[:-5])

# fancy indexing

arr = np.array([10, 20, 30, 40, 50])

print("\nFancy indexing:")
indices = np.array([0, 2, 4])  # indici degli elementi da selezionare
print(arr[indices])  # seleziona gli elementi agli indici specificati



