import random 

def indovina_numero(): 
    numero_sconosciuto = random.randint(1, 100) 
    tentativi = 0 
    while True: 
        tentativi += 1 
        try: 
            guess = int(input("Indovina il numero tra 1 e 100: ")) 
        except ValueError: 
            print("Per favore, inserisci un numero valido.") 
            continue 
        if guess < numero_sconosciuto: 
            print("Troppo basso! Riprova.") 
        elif guess > numero_sconosciuto: 
            print("Troppo alto! Riprova.") 
        else: 
            print(f"Congratulazioni! Hai indovinato il numero in {tentativi} tentativi.") 
            break 
indovina_numero()
