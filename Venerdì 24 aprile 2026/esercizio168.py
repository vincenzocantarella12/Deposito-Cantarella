class ContoBancario:
    
    

    def __init__(self, titolare, saldo=0.0):
        self.__titolare = ""
        self.set_titolare(titolare)
        self.__saldo = saldo if saldo > 0 else 0.0

   
    def get_titolare(self):                                       # getter titolare
        return self.__titolare


   
    def set_titolare(self, valore):                               # setter titolare
        if isinstance(valore, str) and valore.strip():
            self.__titolare = valore.strip()
        else:
            print("Errore: titolare non valido")


    
    def get_saldo(self):                                           # getter saldo
        return self.__saldo


   
    def deposita(self, importo):
        if not isinstance(importo, (int, float)):
            print("Errore: l'importo deve essere numerico")
            return
        if importo <= 0:
            print("Errore: importo non valido")
            return

        self.__saldo += importo                            #aumento il saldo se l'importo è positivo



    
    def preleva(self, importo):
        if not isinstance(importo, (int, float)):
            print("Errore: l'importo deve essere numerico")
            return
        if importo <= 0:
            print("Errore: importo non valido")
            return
        if importo > self.__saldo:
            print("Errore: fondi insufficienti")
            return

        self.__saldo -= importo                           # diminuisco il saldo se preleva

    
    
    def visualizza_saldo(self):
        return self.__saldo



conto = ContoBancario("Mario Rossi", 1500)

conto.deposita(100)
conto.preleva(150)
conto.preleva(2000)

print("Titolare:", conto.get_titolare())
print("Saldo:", conto.visualizza_saldo())






