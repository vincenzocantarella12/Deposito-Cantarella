import random


class MetodoPagamento:
    
    
    def effettua_pagamento(self, utente, importo):
        print("Metodo non definito")



# METODI DI PAGAMENTO


class CartaDiCredito(MetodoPagamento):
    
    
    def effettua_pagamento(self, utente, importo):
        if utente.saldo >= importo:
            utente.saldo -= importo
            print(f"{utente.nome} ha pagato {importo}€ con Carta di Credito")
        else:
            print(f"Pagamento rifiutato: saldo insufficiente ({utente.saldo}€)")


class PayPal(MetodoPagamento):
    
    
    def effettua_pagamento(self, utente, importo):
        if utente.saldo >= importo:
            utente.saldo -= importo
            print(f"{utente.nome} ha pagato {importo}€ con PayPal")
        else:
            print(f"Pagamento rifiutato: saldo insufficiente ({utente.saldo}€)")


class BonificoBancario(MetodoPagamento):
    
    
    def effettua_pagamento(self, utente, importo):
        if utente.saldo >= importo:
            utente.saldo -= importo
            print(f"{utente.nome} ha pagato {importo}€ con Bonifico Bancario")
        else:
            print(f"Pagamento rifiutato: saldo insufficiente ({utente.saldo}€)")




# GESTORE PAGAMENTI


class GestorePagamenti:
    
    def paga(self, metodo, utente, importo):
        metodo.effettua_pagamento(utente, importo)





# UTENTE CON SALDO RANDOM


class Utente:
    
    def __init__(self, nome):
        self.nome = nome
        
        self.saldo = random.randint(10, 1000)                # saldo random tra 10 e 1000 euro



# UTILIZZO PROGRAMMA



print("Benvenuto nel sistema di pagamento")

nome = input("Come ti chiami? ")

utente = Utente(nome)

print(f"Il tuo saldo iniziale è: {utente.saldo}€")


print("\nScegli metodo di pagamento:")
print("1 - Carta di Credito")
print("2 - PayPal")
print("3 - Bonifico Bancario")


scelta = input("Scelta (1/2/3): ")
importo = float(input("Importo da pagare: "))


# SCELTA METODO


if scelta == "1":
    metodo = CartaDiCredito()
elif scelta == "2":
    metodo = PayPal()
elif scelta == "3":
    metodo = BonificoBancario()
else:
    print("Scelta non valida")
    exit()



gestore = GestorePagamenti()
gestore.paga(metodo, utente, importo)


print(f"Saldo rimanente: {utente.saldo}€")              


        

# manca la parte delle commissioni perché me la sono persa, la carico pomeriggio