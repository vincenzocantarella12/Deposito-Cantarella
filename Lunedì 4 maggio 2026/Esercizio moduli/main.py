from inserimento_dati import inserisci_dati
from analisi import analizza
from file_manager import salva_risultati



def main():            

    while True:
        
        print(" ") 
        print("ANALIZZATORE VENDITE")
        print(" ")
        print("1. Inserisci e analizza dati")
        print("2. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":

            dati = inserisci_dati()

            if not dati:
                print("Nessun dato inserito.")
            else:
                totale, media, sopra = analizza(dati)

                print(f"\nTotale: {totale}")
                print(f"Media: {media:.2f}")


                if sopra:
                    print("Vendite sopra la media:", sopra)
                else:
                    print("Nessuna vendita sopra la media")

                salva_risultati(totale, media, sopra)

        elif scelta == "2":
            print("Uscita dal programma...")
            break

        else:
            print("Scelta non valida, riprova.")



if __name__ == "__main__":
    main()
    


# aggiungo un menu per l'inserimento dei dati.
# con un ciclo while per permettere più inserimenti senza dover riavviare il programma.