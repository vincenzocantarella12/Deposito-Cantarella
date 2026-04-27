class MetodoPagamento:
    
    def effettua_pagamento(self, importo, nome):
        raise NotImplementedError("Metodo non implementato")


class CartaDiCredito(MetodoPagamento):
    
    def effettua_pagamento(self, importo, nome):
        print(f"{nome} ha pagato {importo}€ con Carta di Credito")


class PayPal(MetodoPagamento):
    
    def effettua_pagamento(self, importo, nome):
        print(f"{nome} ha pagato {importo}€ con PayPal")


class BonificoBancario(MetodoPagamento):
    
    def effettua_pagamento(self, importo, nome):
        print(f"{nome} ha pagato {importo}€ con Bonifico Bancario")






print("Ciao! Benvenuto nel sistema di pagamento")

nome = input("Come ti chiami? ")

print("Con cosa vuoi pagare?")
print("1 - Carta di Credito")
print("2 - PayPal")
print("3 - Bonifico Bancario")

scelta = input("Scegli (1/2/3): ")
importo = float(input("Quanto vuoi pagare? "))

if scelta == "1":
    metodo = CartaDiCredito()
elif scelta == "2":
    metodo = PayPal()
elif scelta == "3":
    metodo = BonificoBancario()
else:
    print("Scelta non valida")
    exit()

metodo.effettua_pagamento(importo, nome)