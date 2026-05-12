import numpy as np


# Processo ripetibile

np.random.seed(42)


# Array con linspace

array1 = np.linspace(0, 10, 50)


# Array casuale

array2 = np.random.random(50)


# Somma dei due array

nuovo_array = array1 + array2


# Somme

somma_totale = np.sum(nuovo_array)
somma_maggiori_5 = np.sum(nuovo_array[nuovo_array > 5])


# Stampa

print("Array linspace:")
print(array1)

print("\nArray casuale:")
print(array2)

print("\nNuovo array:")
print(nuovo_array)

print("\nSomma totale:")
print(somma_totale)

print("\nSomma elementi > 5:")
print(somma_maggiori_5)



# Scelta salvataggio
scelta = input("\nVuoi sovrascrivere il file? (si/no): ")

# w = sovrascrive, a = aggiunge
modalita = "w" if scelta == "si" else "a"   # ho messo w se l'utente vuole sovrascrivere, altrimenti a per aggiungere al file esistente

# Salvataggio nel file
with open("dati.txt", modalita) as file:   # apre il file in modalità scelta dall'utente

    file.write("Nuovo array:\n")
    file.write(str(nuovo_array) + "\n")

    file.write(f"\nSomma totale: {somma_totale}\n")
    file.write(f"Somma > 5: {somma_maggiori_5}\n\n")

print("\nDati salvati.")