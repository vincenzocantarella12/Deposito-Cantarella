from utente import Utente            # importo la classe Utente dal file utente.py


nome_file = "ricevute.txt"           # variabile per non scriverlo sempre          



def crea_ricevuta_acquisto(utente):
    prodotto = input("Nome prodotto: ")
    prezzo = float(input("Prezzo: "))

    ricevuta = f"[ACQUISTO] {utente.nome} - {prodotto} - {prezzo}€\n"

    with open(nome_file, "a") as file:
        file.write(ricevuta)

    print("Ricevuta di acquisto salvata!")



def crea_ricevuta_ordine(utente):
    prodotto = input("Nome prodotto: ")
    quantita = int(input("Quantità: "))

    ricevuta = f"[ORDINE] {utente.nome} - {prodotto} - QTA: {quantita}\n"

    with open(nome_file, "a") as file:          # apre in modalità append per aggiungere alla fine del file senza sovrascrivere
        file.write(ricevuta)

    print("Ricevuta di ordine salvata!")



def leggi_ricevute():
    try:
        with open(nome_file, "r") as file:          # r per leggere il file 
            contenuto = file.read()
            print("RICEVUTE SALVATE:")
            print(" ")
            print(contenuto)
    except FileNotFoundError:
        print("Nessuna ricevuta trovata.")



def menu():
    nome = input("Inserisci nome utente: ")
    utente = Utente(nome)



# utilizzo interattivo del menu


    while True:
        print("MENU PRINCIPALE")
        print(" ")
        print("1. Nuova ricevuta acquisto")
        print("2. Nuova ricevuta ordine")
        print("3. Leggi ricevute")
        print("4. Esci")


        scelta = input("Scelta: ")

        if scelta == "1":
            crea_ricevuta_acquisto(utente)
        elif scelta == "2":
            crea_ricevuta_ordine(utente)
        elif scelta == "3":
            leggi_ricevute()
        elif scelta == "4":
            print("Uscita")
            break
        else:
            print("Scelta non valida")


menu()