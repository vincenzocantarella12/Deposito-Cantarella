def carica_clienti():             # funzione clienti per caricare i clienti da un file
    
    clienti = {}              #dizionario vuoto  che poi si riempirà dopo il login
    try:
        with open("clienti.txt", "r") as f:  # r per leggere
            for riga in f:
                user, pw, spesa = riga.strip().split(",")
                clienti[user] = {"password": pw, "spesa": float(spesa)}
    except FileNotFoundError:
        pass
    return clienti



def salva_clienti(clienti):
    with open("clienti.txt", "w") as f:           # w per scrivere (sovrascrive)
        for user, dati in clienti.items():
            f.write(f"{user},{dati['password']},{dati['spesa']}\n")


def registra_cliente(clienti, username, password):
    clienti[username] = {"password": password, "spesa": 0}


def login_cliente(clienti, username, password):
    return username in clienti and clienti[username]["password"] == password


def acquista(clienti, inventario, user, prodotto, quantita):
    if prodotto in inventario:
        if inventario[prodotto]["quantita"] >= quantita:
            costo = inventario[prodotto]["prezzo"] * quantita

            inventario[prodotto]["quantita"] -= quantita
            clienti[user]["spesa"] += costo

            print(f"Acquisto completato! Totale: {costo}")
            return costo
        else:
            print("Quantità insufficiente")
    else:
        print("Prodotto non trovato")
    return 0

