def carica_inventario():
    
    
    inventario = {}       #dizionario vuoto perché ho inserito i dati in un file di testo, quindi devo caricarli in un dizionario per poterli utilizzare

    try:
        with open("inventario.txt", "r") as file:
            for riga in file:
                riga = riga.strip()

                if not riga:
                    continue

                nome, prezzo, quantita = riga.split(",")

                inventario[nome] = {
                    "prezzo": float(prezzo),
                    "quantita": int(quantita)
                }

    except FileNotFoundError:
        pass

    return inventario



def salva_inventario(inventario):
    with open("inventario.txt", "w") as file:
        for nome, dati in inventario.items():
            file.write(f"{nome},{dati['prezzo']},{dati['quantita']}\n")



def mostra_inventario(inventario):    # per mostrare l'inventario 
    if not inventario:
        print("Inventario vuoto")
        return

    for nome, dati in inventario.items():
        print(f"{nome} - Prezzo: {dati['prezzo']}€ - Quantità: {dati['quantita']}")



def aggiungi_articolo(inventario, nome, prezzo, quantita):
    inventario[nome] = {
        "prezzo": prezzo,
        "quantita": quantita
    }



def aggiorna_articolo(inventario, nome, prezzo=None, quantita=None):
    if nome in inventario:
        if prezzo is not None:
            inventario[nome]["prezzo"] = prezzo
        if quantita is not None:
            inventario[nome]["quantita"] = quantita


def rimuovi_articolo(inventario, nome):
    if nome in inventario:
        del inventario[nome]