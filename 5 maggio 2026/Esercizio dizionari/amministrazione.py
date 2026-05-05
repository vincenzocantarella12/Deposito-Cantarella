def carica_admin():
    
    admin = {}              # dizionario vuoto per admin che ho aggiunto su txt
    try:
        with open("amministrazione.txt", "r") as f:
            for riga in f:
                user, pw = riga.strip().split(",")
                admin[user] = pw
    except FileNotFoundError:
        pass
    return admin



def login_admin(admin, username, password):
    return username in admin and admin[username] == password



def report_vendite(clienti):
    totale = 0
    print("\n--- REPORT CLIENTI ---")
    for user, dati in clienti.items():
        print(f"{user} ha speso: {dati['spesa']}")
        totale += dati["spesa"]

    print(f"\nGUADAGNO TOTALE: {totale}")