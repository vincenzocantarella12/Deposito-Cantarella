class MetodoPagamento:
    
    
    def effettua_pagamento(self, importo, nome):
        print("Metodo non definito")
    
    
    
class CartaDiCredito(MetodoPagamento):
    
    def effettua_pagamento(self, importo, nome):
        print(f"{nome} ha pagato {importo}€ con Carta di Credito")


class PayPal(MetodoPagamento):
    
    def effettua_pagamento(self, importo, nome):
        print(f"{nome} ha pagato {importo}€ con PayPal")


class BonificoBancario(MetodoPagamento):
    
    def effettua_pagamento(self, importo, nome):
        print(f"{nome} ha pagato {importo}€ con Bonifico Bancario")
        
        
        
class GestorePagamenti:
    
    def paga(self, metodo: MetodoPagamento, importo, nome):
        metodo.effettua_pagamento(importo, nome)
        


class Utente:
    
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
 
 
        
print("Benvenuto nel sistema di pagamento")


nome = input("Come ti chiami? ")
saldo = float(input("Inserisci il tuo saldo: "))

utente = Utente(nome, saldo)


print("Scegli metodo di pagamento:")
print("1 - Carta di Credito")
print("2 - PayPal")
print("3 - Bonifico Bancario")


scelta = input("Scelta (1/2/3): ")
importo = float(input("Importo da pagare: "))



if scelta == "1":                                        # selezione metodo
    metodo = CartaDiCredito()
elif scelta == "2":
    metodo = PayPal()
elif scelta == "3":
    metodo = BonificoBancario()
else:
    print("Scelta non valida")
    exit()


             
gestore = GestorePagamenti()                              # uso del gestore
gestore.paga(metodo, importo, nome)


print(f"Saldo rimanente: {utente.saldo}€")   