from abc import ABC, abstractmethod




class VeicoloTrasporto(ABC):

    def __init__(self, targa, peso_massimo):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = 0


    def carica(self, peso):
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"Caricato {peso} kg su {self._targa}")
        else:
            print("Errore: superato peso massimo!")


    def scarica(self):
        self._carico_attuale = 0
        print(f"{self._targa} scaricato")



    @abstractmethod
    

    def costo_manutenzione(self):
        pass

    def get_targa(self):
        return self._targa

    def get_tipo(self):
        return self.__class__.__name__  




# CAMION



class Camion(VeicoloTrasporto):
    

    def __init__(self, targa, peso_massimo, numero_assi):
        super().__init__(targa, peso_massimo)
        self.numero_assi = numero_assi


    def costo_manutenzione(self):
        return (100 * self.numero_assi) + self._peso_massimo



# FURGONE


class Furgone(VeicoloTrasporto):
    

    def __init__(self, targa, peso_massimo, alimentazione):
        super().__init__(targa, peso_massimo)
        self.alimentazione = alimentazione


    def costo_manutenzione(self):
        if self.alimentazione == "elettrico":
            return 200
        else:
            return 150


# MOTOCARRO


class Motocarro(VeicoloTrasporto):


    def __init__(self, targa, peso_massimo, anni_servizio):
        super().__init__(targa, peso_massimo)
        self.anni_servizio = anni_servizio


    def costo_manutenzione(self):
        return 50 * self.anni_servizio



# GESTORE FLOTTA



class GestoreFlotta:
    

    def __init__(self):
        self.veicoli = []
        

    def aggiungi_veicolo(self, veicolo: VeicoloTrasporto):
        self.veicoli.append(veicolo)


    def rimuovi_veicolo(self, targa):
        self.veicoli = [v for v in self.veicoli if v.get_targa() != targa]


    def costo_totale_manutenzione(self):
        totale = 0
        for v in self.veicoli:
            totale += v.costo_manutenzione()
        return totale


    def stampa_veicoli(self):
        for v in self.veicoli:
            print("Targa:", v.get_targa())
            print("Tipo:", v.get_tipo())
            print("Carico:", v._carico_attuale)



# USO PROGRAMMA




flotta = GestoreFlotta()

while True:
    print("MENU")
    print(" ")
    print("1 - Aggiungi Camion")
    print("2 - Aggiungi Furgone")
    print("3 - Aggiungi Motocarro")
    print("4 - Mostra veicoli")
    print("5 - Costo totale manutenzione")
    print("0 - Esci")
    

    scelta = input("Scelta menu: ")


    if scelta == "1":
        targa = input("Targa: ")
        peso = int(input("Peso massimo: "))
        assi = int(input("Numero assi: "))
        flotta.aggiungi_veicolo(Camion(targa, peso, assi))
        print("Camion aggiunto!")


    elif scelta == "2":
        targa = input("Targa: ")
        peso = int(input("Peso massimo: "))
        alimentazione = input("Alimentazione (elettrico/diesel): ")
        flotta.aggiungi_veicolo(Furgone(targa, peso, alimentazione))
        print("Furgone aggiunto!")


    elif scelta == "3":
        targa = input("Targa: ")
        peso = int(input("Peso massimo: "))
        anni = int(input("Anni di servizio: "))
        flotta.aggiungi_veicolo(Motocarro(targa, peso, anni))
        print("Motocarro aggiunto!")


    elif scelta == "4":
        flotta.stampa_veicoli()

    elif scelta == "5":
        print("Costo totale:", flotta.costo_totale_manutenzione())

    elif scelta == "0":
        print("Uscita")
        break

    else:
        print("Scelta non valida")
        
        
        
        