from visita import Visita



nome_file = "visite.txt"




def salva_visita(visita):
    stato = "ACCETTATA" if visita.accettata else "IN ATTESA"

    riga = f"{visita.paziente} | {visita.medico} | {visita.data} | {stato}\n"

    with open(nome_file, "a") as file:
        file.write(riga)



def leggi_visite():
    try:
        with open(nome_file, "r") as file:
            print("VISITE REGISTRATE:")
            print(file.read())
    except FileNotFoundError:
        print("Nessuna visita trovata.")



def crea_visita():
    paziente = input("Nome paziente: ")
    medico = input("Nome medico: ")
    data = input("Data visita: ")

    visita = Visita(paziente, medico, data)
    salva_visita(visita)

    print("Visita registrata!")



def accetta_visita():
    paziente = input("Nome paziente da accettare: ")

    try:
        with open(nome_file, "r") as file:
            righe = file.readlines()

        with open(nome_file, "w") as file:
            for riga in righe:
                if paziente in riga and "IN ATTESA" in riga:
                    riga = riga.replace("IN ATTESA", "ACCETTATA")
                file.write(riga)

        print("Visita aggiornata!")
    except FileNotFoundError:
        print("File non trovato.")





def menu():
    while True:
        print("MENU VISITE MEDICHE")
        print(" ")
        print("Scegli un'opzione:")
        print(" ")
        print("1. Registra visita")
        print("2. Leggi visite")
        print("3. Accetta visita")
        print("4. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            crea_visita()
        elif scelta == "2":
            leggi_visite()
        elif scelta == "3":
            accetta_visita()
        elif scelta == "4":
            break
        else:
            print("Scelta non valida")


menu()