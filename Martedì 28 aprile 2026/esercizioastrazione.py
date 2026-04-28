from abc import ABC, abstractmethod


# CLASSE ASTRATTA


class Impiegato(ABC):
    
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base


    @abstractmethod
    def calcola_stipendio(self):              # metodo astratto per il calcolo dello stipendio implementato nelle sottoclassi
        pass


    def info(self):
        return f"{self.nome} {self.cognome}"



#CLASSI DERIVATE IMPIEGATO FISSO



class ImpiegatoFisso(Impiegato):
    
    def calcola_stipendio(self):
        return self.stipendio_base



#CLASSI DERIVATE IMPIEGATO A PROVVIGIONE



class ImpiegatoAProvvigione(Impiegato):
    
    def __init__(self, nome, cognome, stipendio_base, vendite, bonus):          #ho aggiunto vendite e bonus e con super richiamo le basi
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.bonus = bonus

    def calcola_stipendio(self):
        bonus_totale = self.vendite * self.bonus
        return self.stipendio_base + bonus_totale




# INFORMAZIONI IMPIEGATI E STIPENDIO



def stampa_impiegati(lista_impiegati):
    for imp in lista_impiegati:
        print("Nome:", imp.info())
        print("Stipendio:", imp.calcola_stipendio())




impiegato1 = ImpiegatoFisso("Mirko", "Campari", 1500)
impiegato2 = ImpiegatoAProvvigione("Vincenzo", "Cantarella", 1200, 5000, 0.4)

print(impiegato1.info(), impiegato1.calcola_stipendio())
print(impiegato2.info(), impiegato2.calcola_stipendio())


    
    