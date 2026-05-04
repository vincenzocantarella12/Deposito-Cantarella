from data_ora import ottieni_data_corrente



def salva_risultati(totale, media, sopra):


    data = ottieni_data_corrente()


    with open("risultati.txt", "a") as file:      #con a riesco a aggiungere al file senza sovrascrivere
        file.write("\n-NUOVA ANALISI-\n")
        file.write(f"Data report: {data}\n\n")

        file.write(f"Totale vendite: {totale}\n")
        file.write(f"Media vendite: {media:.2f}\n\n")

        if sopra:
            file.write("Vendite sopra la media:\n")
            for valore in sopra:
                file.write(f"{valore}\n")
        else:
            file.write("Nessuna vendita sopra la media\n")

        file.write("\n----------------------\n")
        



# con w sovrascrivo il file ogni volta, con a aggiungo al file senza sovrascrivere.
