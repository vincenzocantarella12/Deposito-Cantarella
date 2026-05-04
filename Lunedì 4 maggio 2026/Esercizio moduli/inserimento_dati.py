def inserisci_dati():    # FUNZIONE PER INSERIMENTO DATI
    
    
    
    while True:
        try:
            dati = input("Inserisci vendite separate da spazio: ")
            
            if not dati.strip():
                return []
                                            
            lista = list(map(int, dati.split()))      # map per convertire ogni elemento in intero, split per dividere la stringa in base agli spazi
            return lista                               # CONVERSIONE IN INTERI



        except ValueError:                              # GESTIONE ERRORI con try-except
            print("Errore: inserisci solo numeri interi!")
            
