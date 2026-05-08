from gestione_file import leggi_preventivi


def analizza_dati():

    preventivi = leggi_preventivi()

    if not preventivi:
        print("Nessun dato disponibile")
        return

    totale = len(preventivi)

    somma_premi = sum(float(p["premio"]) for p in preventivi)

    media = somma_premi / totale

    print(f"Totale preventivi: {totale}")

    print(f"Premio medio: {media:.2f}€")



    polizze = {}           # creo un dizionario per contare il numero di preventivi per ogni tipo di polizza

    for p in preventivi:

        tipo = p["polizza"]

        if tipo in polizze:
            polizze[tipo] += 1

        else:
            polizze[tipo] = 1

    print("\nPolizze presenti:")

    for tipo, numero in polizze.items():

        print(f"{tipo}: {numero}")