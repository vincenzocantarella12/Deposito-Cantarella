# Liste e Variabili per gestire utenti, password, storico e stato


utenti = []
passwords = []

storico_operazioni = []
storico_risultati = []

stato = {                        # dizionario per gestire lo stato dell'utente
    "loggato": False,
    "utente": "",
    "operazioni": 0
}



# Registrazione



def registra():
    nome = input("Username: ")

    if nome in utenti:
        print("Utente già esistente!")         #torna indietro se l'utente esiste già, con if dentro def
        return

    password = input("Password: ")

    utenti.append(nome)                         # aggiungo il nome e la password alla lista con append 
    passwords.append(password)

    print("Registrazione completata!")



# Login



def login():
    nome = input("Username: ")
    password = input("Password: ")

    if nome in utenti:
        i = utenti.index(nome)                        #uso index per trovare l'utente nella lista e verificare se la password corrisponde

        if passwords[i] == password:                    #if annidato per verificare se la password è corretta, con if dentro def
            stato["loggato"] = True
            stato["utente"] = nome
            stato["operazioni"] = 0

            print("Login effettuato!")
        else:
            print("Password errata")
    else:
        print("Utente non trovato")



# Logout




def logout():
    stato["loggato"] = False                                      # se non sei loggato non puoi entrare, quindi false 
    stato["utente"] = ""
    stato["operazioni"] = 0
    print("Sei uscito dal sistema")




# Calcolatrice




def calcolatrice():
    if not stato["loggato"]:
        print("Devi prima fare login!")
        return

    while True:
        print("\n--- CALCOLATRICE ---")
        print("")                                                   # \n per andare a capo e print per lasciare uno spazio, solo visivo
        print("1. Somma (+)")
        print("2. Sottrazione (-)")
        print("3. Moltiplicazione (*)")
        print("4. Divisione (/)")
        print("5. Potenza (**)")
        print("6. Esci")

        scelta = input("Scelta: ")

        if scelta == "6":
            break                                                     # con il break esco dal ciclo while se l'utente vuole di uscire
        
        if stato["operazioni"] >= 4:                                  #se le operazioni sono 4 o più esce
            print("Hai fatto 4 operazioni, devi riloggarti!")
            logout()
            break

        a = float(input("Primo numero: "))                            #float per i numeri con la virgola
        b = float(input("Secondo numero: "))

        operazione_valida = True

        if scelta == "1":                                             #un if con dentro elif 'infiniti'
            risultato = a + b
            operazione = "somma"

        elif scelta == "2":
            risultato = a - b
            operazione = "sottrazione"

        elif scelta == "3":
            risultato = a * b
            operazione = "moltiplicazione"

        elif scelta == "4":
            if b == 0:                                                 #altri if per non dividere per zero
                print("Errore: Non puoi dividere per zero")
                operazione_valida = False                              # se l'operazione non è valida, non la salvo nello storico
            else:
                risultato = a / b
                operazione = "divisione"

        elif scelta == "5":
            risultato = a ** b
            operazione = "potenza"

        else:
            print("Scelta non valida")
            operazione_valida = False

        if operazione_valida:
            storico_operazioni.append(f"{operazione}: {a}, {b}")         # conservo l'operazione fatta in una lista con append
            storico_risultati.append(risultato)

            stato["operazioni"] += 1

            print("Risultato:", risultato)




# Storico




def mostra_storico():
    if not stato["loggato"]:
        print("Devi fare login!")
        return

    print("\n--- STORICO ---")
    for i in range(len(storico_operazioni)):                   #contiamo quante operazioni sono state fatte con len e le stampiamo con un ciclo for
        print(storico_operazioni[i], "=", storico_risultati[i])



# Menu Principale



while True:
    print("\n===== MENU =====")
    print("")
    print("1. Registrazione")
    print("2. Login")
    print("3. Calcolatrice")
    print("4. Storico")
    print("5. Logout")
    print("6. Esci")
    print("")
    print("")

    scelta = input("Scelta: ")

    if scelta == "1":
        registra()                            # altro if con dentro elif per gestire le scelte del menu
    elif scelta == "2":
        login()
    elif scelta == "3":
        calcolatrice()
    elif scelta == "4":
        mostra_storico()
    elif scelta == "5":
        logout()
    elif scelta == "6":
        break
    else:
        print("Scelta non valida")
        
        
        