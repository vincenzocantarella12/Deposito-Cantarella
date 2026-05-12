import numpy as np


# Creazione di un array unidimensionale

arr = np.array([1, 2, 3, 4, 5])


# Creazione di un array bidimensionale

arr2d = np.array([[1, 2, 3], [4, 5, 6]])


print(arr)
print(arr2d)

zeroarr = np.zeros((10, 10))
print("\nArray di zeri 10x10:")
print(zeroarr)

# shape serve a conoscere la forma dell'array, ovvero il numero di elementi in ogni dimensione

print("\nArray unidimensionale (Shape):")
print(arr.shape)
print("\nArray bidimensionale (Shape):")
print(arr2d.shape)
print("\nArray di zeri (Shape):")
print(zeroarr.shape)

#ndim serve a conoscere il numero di dimensioni dell'array, ovvero se è un array unidimensionale, bidimensionale, tridimensionale, ecc.

print("\nArray unidimensionale (ndim):")
print(arr.ndim)
print("\nArray bidimensionale (ndim):")
print(arr2d.ndim)
print("\nArray di zeri (ndim):")
print(zeroarr.ndim)

# size serve a conoscere il numero totale di elementi presenti nell'array, ovvero il prodotto delle dimensioni dell'array

print("\nArray unidimensionale (size):")
print(arr.size)
print("\nArray bidimensionale (size):")
print(arr2d.size)
print("\nArray di zeri (size):")
print(zeroarr.size)

#dtype serve a conoscere il tipo di dati degli elementi presenti nell'array, ad esempio int, float, ecc.

print("\nArray unidimensionale (dtype):")
print(arr.dtype)
print("\nArray bidimensionale (dtype):")
print(arr2d.dtype)
print("\nArray di zeri (dtype):")
print(zeroarr.dtype)

#sum serve a calcolare la somma di tutti gli elementi presenti nell'array, restituendo un singolo valore che rappresenta la somma totale degli elementi.

print("\nArray unidimensionale (sum):")
print(arr.sum())
print("\nArray bidimensionale (sum):")
print(arr2d.sum())
print("\nArray di zeri (sum):")
print(zeroarr.sum())

#mean serve a calcolare la media aritmetica di tutti gli elementi presenti nell'array, restituendo un singolo valore che rappresenta la media degli elementi.

print("\nArray unidimensionale (mean):")
print(arr.mean())
print("\nArray bidimensionale (mean):")
print(arr2d.mean())
print("\nArray di zeri (mean):")
print(zeroarr.mean())

# max serve a trovare il valore massimo presente nell'array, restituendo un singolo valore che rappresenta il massimo degli elementi.

print("\nArray unidimensionale (max&min):")
print(" max: " + str(arr.max()) + " - i " + str(arr.argmax()))
print(" min: " + str(arr.min()) + " - i " + str(arr.argmin()))
print("\nArray bidimensionale (max&min):")
print(" max: " + str(arr2d.max()) + " - i " + str(arr2d.argmax()))
print(" min: " + str(arr2d.min()) + " - i " + str(arr2d.argmin()))
print("\nArray di zeri (max&min):")
print(" max: " + str(zeroarr.max()) + " - i " + str(zeroarr.argmax()))
print(" min: " + str(zeroarr.min()) + " - i " + str(zeroarr.argmin()))

# arange serve a creare un array con valori equidistanti in un intervallo specificato, restituendo un array che contiene i valori generati.

arrRange = np.arange(10)
print("\nArray con arange:")
print(arrRange)

#reshape serve a modificare la forma di un array esistente, restituendo un nuovo array con la stessa data ma con una forma diversa.


reshaped = arrRange.reshape((10, 4))
print("\nArray reshaped :")
print(reshaped)







