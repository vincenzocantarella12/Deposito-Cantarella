import numpy as np


# Creazione dell'array da 10 a 49

array_interi = np.arange(10, 50)


# Verifica del tipo di dato


print("Array originale:")
print(array_interi)

print("\nTipo di dato originale:")
print(array_interi.dtype)


# Conversione in float64


array_float = array_interi.astype(np.float64)

print("\nArray convertito:")
print(array_float)

print("\nNuovo tipo di dato:")
print(array_float.dtype)


# Forma dell'array



print("\nForma dell'array:")
print(array_float.shape)