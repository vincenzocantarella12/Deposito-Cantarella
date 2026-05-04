from modello import Vendite, Totale, Media, SopraMedia



def analizza(dati):                 
    vendite = Vendite(dati)


    totale = Totale(vendite).calcola()
    media = Media(vendite).calcola()
    sopra = SopraMedia(vendite, media).calcola()


    return totale, media, sopra      

# restituisco i risultati come tupla, poi li gestisco in main.py per la stampa e il salvataggio.