import gestione_inventario as gi
import gestione_clienti as gc
import amministrazione as am



inventario = gi.carica_inventario()
clienti = gc.carica_clienti()
admin = am.carica_admin()

# menu interattivo per clienti e admin

while True:
    print("\n--- MENU NEGOZIO ---")
    print(" ")
    print("\n1. Registrazione Cliente")
    print("2. Login Cliente")
    print("3. Login Admin")
    print("4. Esci")

    scelta = input("Scelta: ")

    
    if scelta == "1":
        user = input("Username: ")
        pw = input("Password: ")

        gc.registra_cliente(clienti, user, pw)
        gc.salva_clienti(clienti)

    
    
    elif scelta == "2":
        user = input("Username: ")
        pw = input("Password: ")

        if gc.login_cliente(clienti, user, pw):
            while True:
                print("\n1. Mostra Inventario")
                print("2. Acquista")
                print("3. Logout")

                s = input("Scelta: ")

                
                if s == "1":
                    gi.mostra_inventario(inventario)

                elif s == "2":
                    prod = input("Prodotto: ")
                    q = int(input("Quantità: "))

                    gc.acquista(clienti, inventario, user, prod, q)

                    gi.salva_inventario(inventario)
                    gc.salva_clienti(clienti)

                elif s == "3":
                    break
        else:
            print("Login fallito")

  
    elif scelta == "3":
        user = input("Admin: ")
        pw = input("Password: ")

        if am.login_admin(admin, user, pw):
            while True:
                print("\n1. Mostra Inventario")
                print("2. Aggiungi prodotto")
                print("3. Report vendite")
                print("4. Logout")

                s = input("Scelta: ")

                if s == "1":
                    gi.mostra_inventario(inventario)

                elif s == "2":
                    nome = input("Nome: ")
                    prezzo = float(input("Prezzo: "))
                    quantita = int(input("Quantità: "))

                    gi.aggiungi_articolo(inventario, nome, prezzo, quantita)
                    gi.salva_inventario(inventario)

                elif s == "3":
                    am.report_vendite(clienti)

                elif s == "4":
                    break
        else:
            print("Login admin fallito")

    elif scelta == "4":
        break