import numpy as np

# Creazione array di 20 numeri casuali tra 10 e 50

array = np.random.randint(10, 51, 20)  # 20 numeri casuali tra 10 e 50 inclusi

print("Array originale:")
print(array)



# Primi 10 elementi

primi_10 = array[:10]


# Ultimi 5 elementi

ultimi_5 = array[-5:]


# Elementi dall'indice 5 al 15 escluso

da_5_a_15 = array[5:15]


# Ogni terzo elemento

ogni_terzo = array[::3]


# Modifica degli elementi dall'indice 5 al 10 escluso

array[5:10] = 99



print("\nPrimi 10 elementi:")
print(primi_10)

print("\nUltimi 5 elementi:")
print(ultimi_5)

print("\nElementi dall'indice 5 al 15:")
print(da_5_a_15)

print("\nOgni terzo elemento:")
print(ogni_terzo)

print("\nArray dopo la modifica:")
print(array)