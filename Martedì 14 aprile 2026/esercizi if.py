
#Esercizio 1

numero = 50
if numero >0:
    print("Il numero è positivo")
    if numero == 50:
        print('Vincenzo')
    elif numero<0:
        print("Il numero è negativo")
    else:
        print("Il numero è zero")
        
        
        
            
 #Esercizio 2   
         
        
        menu = [aggiungi, modifica, elimina]
        selezione = input("Scegli un'opzione: ")   
        if selezione == "aggiungi":
            print("Hai scelto di aggiungere un elemento.")
        elif selezione == "modifica":
            print("Hai scelto di modificare un elemento.")
        elif selezione == "elimina":
            print("Hai scelto di eliminare un elemento.")
        else:
            print("Opzione non valida.")
            
            
            
            
            
              
    
    utenti = []
id_corrente = 1

scelta = input("Hai già un account? (si/no)")

if scelta == "no":
    print("REGISTRAZIONE")

    nome = input("Inserisci nome: ")
    password = input("Inserisci password: ")

    utenti.append({
        "id": id_corrente,
        "nome": nome,
        "password": password
    })

    print("Account creato con successo!")
    print("I tuoi dati:", utenti)
    id_corrente += 1


else:
    print("LOGIN")

    nome = input("Inserisci nome: ")
    password = input("Inserisci password: ")

    accesso = False

    for utente in utenti:
        if utente["nome"] == nome and utente["password"] == password:
            accesso = True

    if accesso:
        print("Accesso riuscito! Benvenuto ")
    else:
        print("Account non trovato o dati errati ")

print("Fine programma")



            
            

    
    
    
    
    
    
    
    
    
    
            
        
        