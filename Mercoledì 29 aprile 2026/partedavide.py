from abc import ABC, abstractmethod

from datetime import datetime



class Elettrodomestico(ABC): # classe astratta
    
    def init(self, marca: str, modello: str, anno_acquisto: int, guasto: str): # costruttore con parametri, con controllo sull'anno di acquisto
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto


    @property # getter e setter per marca, modello, anno_acquisto e guasto, con controllo sull'anno di acquisto
    def marca(self):
        return self.marca


    @marca.setter
    def marca(self, valore):
        # Controllo: stringa non vuota
        if isinstance(valore, str) and valore.strip():
            self.marca = valore.strip()
        else:
            raise ValueError("Errore: La marca deve essere una stringa valida.")


    @property


    def modello(self):
        return self.modello

    @modello.setter
    def modello(self, valore):
        # Controllo: stringa non vuota
        if isinstance(valore, str) and valore.strip():
            self.modello = valore.strip()
        else:
            raise ValueError("Errore: Il modello deve essere una stringa valida.")


    @property
    
    def anno_acquisto(self):
        return self.anno_acquisto



    @anno_acquisto.setter # controllo sull'anno di acquisto, non può essere nel futuro
    def anno_acquisto(self, valore):
        anno_attuale = datetime.today().year
        if valore <= anno_attuale:
            self.anno_acquisto = valore
        else:
            print(f"Errore: L'anno {valore} è nel futuro!")
            self.anno_acquisto = anno_attuale



    @property
    def guasto(self):
        return self.guasto


    @guasto.setter
    def guasto(self, valore):
        if isinstance(valore, str) and valore.strip():
            self.guasto = valore.strip()
        else:
            self.guasto = "Guasto non specificato"


    @abstractmethod
    def descrizione(self):
        pass

    @abstractmethod
    def stima_costo_base(self):
        pass
    
    