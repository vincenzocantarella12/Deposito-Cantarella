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


