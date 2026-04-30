""" file = open("inputoutput.txt", "r")   # r sta per read, leggi il file

contenuto = file.read()               # legge l'intero contenuto del file

riga = file.readline()                # legge una singola riga del file 

print(contenuto)                      # stampa il contenuto del file """                




file = open("provascrittura.txt", "w")  # w sta per write, scrivi nel file

file.write("Ciao, questo ha un testo di prova.\n")  # scrive una riga nel file

file.close()                             # chiude il file



with open("provascrittura.txt", "a") as file:     # a sta per append, aggiungi al file
contenuto = file.read()   # operazioni sul contenuto del file 



from os import getcwd

# Esempio : >>> print(getcwd()) /home/andrea








