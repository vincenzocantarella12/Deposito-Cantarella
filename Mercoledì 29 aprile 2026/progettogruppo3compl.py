from abc import ABC, abstractmethod

from datetime import datetime



class Elettrodomestico(ABC): # classe astratta
    
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str): # costruttore con parametri, con controllo sull'anno di acquisto
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto


    @property # getter e setter per marca, modello, anno_acquisto e guasto, con controllo sull'anno di acquisto
    def marca(self):
        return self.__marca


    @marca.setter
    def marca(self, valore):
        # Controllo: stringa non vuota
        if isinstance(valore, str) and valore.strip():
            self.__marca = valore.strip()
        else:
            raise ValueError("Errore: La marca deve essere una stringa valida.")


    @property


    def modello(self):
        return self.__modello

    @modello.setter
    def modello(self, valore):
        # Controllo: stringa non vuota
        if isinstance(valore, str) and valore.strip():
            self.__modello = valore.strip()
        else:
            raise ValueError("Errore: Il modello deve essere una stringa valida.")


    @property
    
    def anno_acquisto(self):
        return self.__anno_acquisto



    @anno_acquisto.setter # controllo sull'anno di acquisto, non può essere nel futuro
    def anno_acquisto(self, valore):
        anno_attuale = datetime.today().year
        if valore <= anno_attuale:
            self.__anno_acquisto = valore
        else:
            print(f"Errore: L'anno {valore} è nel futuro!")
            self.__anno_acquisto = anno_attuale



    @property
    def guasto(self):
        return self.__guasto


    @guasto.setter
    def guasto(self, valore):
        if isinstance(valore, str) and valore.strip():
            self.__guasto = valore.strip()
        else:
            self.__guasto = "Guasto non specificato"


    @abstractmethod
    def descrizione(self):
        pass

    @abstractmethod
    def stima_costo_base(self):
        pass
    
  
  
    
class Lavatrice(Elettrodomestico):
    

    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init(marca, modello, anno_acquisto, guasto)
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga

    def get_capacita_kg(self):
        return self.capacita_kg

    def get_giri_centrifuga(self):
        return self.giri_centrifuga

    def descrizione(self):
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self):
        if self.__capacita_kg > 8:
            return 90
        return 60
    


class Frigorifero(Elettrodomestico):
    

    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):
        super().__init(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer

    def get_litri(self):
        return self.litri

    def get_ha_freezer(self):
        return self.ha_freezer

    def descrizione(self):
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self):
        base = 70
        if self.ha_freezer:
            base += 20
        if self.litri > 300:
            base += 15
        return base



class Forno(Elettrodomestico):
    

    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato

    def get_tipo_alimentazione(self):
        return self.tipo_alimentazione

    def get_ha_ventilato(self):
        return self.ha_ventilato

    def descrizione(self):
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self):
        base = 65
        if self.tipo_alimentazione == "gas":
            base += 25
        if self.ha_ventilato:
            base += 10
        return base
    
    
class TicketRiparazione:
    

    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "aperto"
        self.__note = []


    def get_id_ticket(self):                        
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def set_stato(self, stato):
        self.__stato = stato

    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    def calcola_preventivo(self, *voci_extra):
        totale = self.__elettrodomestico.stima_costo_base()
        totale += sum(voci_extra)
        return totale
    
    
    
class Officina:



    def init(self, nome):
        self.nome = nome
        self.tickets = []

    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)

    def chiudi_ticket(self, id_ticket):
        for ticket in self.tickets:
            if ticket.get_id_ticket() == id_ticket:
                ticket.set_stato("chiuso")
                return True
        return False


    def stampa_ticket_aperti(self):
        for ticket in self.tickets:
            if ticket.get_stato() != "chiuso":
            print(f"ID: {ticket.get_id_ticket()} "
                  f"Tipo: {ticket.get_elettrodomestico().tipo} "
                  f"Stato: {ticket.get_stato()}")


    def totale_preventivi(self):
        totale = 0
        for ticket in self.tickets:
            totale += ticket.calcola_preventivo()
        return totale


    def statistiche_per_tipo(self):                # uso type
        lavatrici = 0
        frigoriferi = 0
        forni = 0

        for ticket in self.tickets:
            elettro = ticket.get_elettrodomestico()

            if isinstance(elettro, Lavatrice):
                lavatrici += 1
            elif isinstance(elettro, Frigorifero):
                frigoriferi += 1
            elif isinstance(elettro, Forno):
                forni += 1



print(f"Numero di lavatrici in riparazione: {lavatrici}")
print(f"Numero di frigoriferi in riparazione: {frigoriferi}")
print(f"Numero di forni in riparazione: {forni}")   
    
    

