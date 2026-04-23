# ESERCIZIO 1


class Convertitore:

    @staticmethod               
    def euro_in_dollari(euro):
        return euro * 1.08

    @staticmethod
    def km_in_miglia(km):
        return km * 0.621371


print(Convertitore.euro_in_dollari(100))
print(Convertitore.km_in_miglia(10)) 



"""# ESERCIZIO 2


class Animale:
    
    numero_animali = 0
    
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie
        Animale.numero_animali += 1      # ogni volta che creo un animale aumento il contatore degli animali
        
    @classmethod
    def quanti_animali(cls):
        print(f"Sono stati creati {cls.numero_animali} animali.")
        
        
animale1 = Animale ("Vincenzo", "Orso")
animale2 = Animale ("Marta", "Delfino")
animale3 = Animale ("Luca", "Gatto")


Animale.quanti_animali()"""
