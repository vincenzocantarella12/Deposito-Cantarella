import mio_modulo

mio_modulo.saluta("Alice")                # Stampa: Ciao, Alice

raggio = 2
cerchio = mio_modulo.Cerchio(raggio)
print(cerchio.area())                    # Stampa: l'area del cerchio con raggio 2

#modularià è un concetto fondamentale nella programmazione che si riferisce alla suddivisione di un programma in parti più piccole e gestibili chiamate moduli. Un modulo è un file che contiene definizioni di funzioni, classi e variabili che possono essere importati e utilizzati in altri file.
#In Python, i moduli sono semplicemente file con estensione .py che contengono codice Python. Per utilizzare un modulo, è necessario importarlo nel file in cui si desidera utilizzarlo. Ci sono diversi modi per importare un modulo, ma il più comune è utilizzare la parola chiave "import" seguita dal nome del modulo.
#Ad esempio, se abbiamo un modulo chiamato "mio_modulo.py" che contiene la funzione "saluta" e la classe "Cerchio", possiamo importarlo in un altro file come segue:
# import mio_modulo

