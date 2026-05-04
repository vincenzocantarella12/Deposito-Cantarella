from abc import ABC, abstractmethod




class AnalisiBase(ABC):                       # ASTRAZIONE 

    @abstractmethod
    def calcola(self):
        pass




class Vendite:                               # INCAPSULAMENTO + EREDITARIETÀ
    def __init__(self, dati):
        self.__dati = dati  # privato

    def get_dati(self):
        return self.__dati




class Totale(AnalisiBase):                   # POLIMORFISMO più classi con stesso metodo
    def __init__(self, vendite):
        self.vendite = vendite

    def calcola(self):
        return sum(self.vendite.get_dati())



class Media(AnalisiBase):
    def __init__(self, vendite):
        self.vendite = vendite

    def calcola(self):
        dati = self.vendite.get_dati()
        return sum(dati) / len(dati) if dati else 0



class SopraMedia(AnalisiBase):
    def __init__(self, vendite, media):
        self.vendite = vendite
        self.media = media

    def calcola(self):
        return [x for x in self.vendite.get_dati() if x > self.media] # lista di vendite sopra la media
    
    
    
    
# creo le class per ogni tipo di analisi, tutte ereditano da AnalisiBase 
# implementano il metodo calcola() in modo diverso, ma con la stessa interfaccia.