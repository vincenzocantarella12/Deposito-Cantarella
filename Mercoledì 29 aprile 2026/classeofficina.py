class Officina:
    
    
    def __init__(self, nome):
        self.nome = nome
        self.tickets = []


    def aggiungi_ticket(self, ticket):
        self.tickets.append(ticket)


    def chiudi_ticket(self, id_ticket):
        for ticket in self.tickets:
            if ticket.id_ticket == id_ticket:
                ticket.stato = "chiuso"
                return True
        return False


    def stampa_ticket_aperti(self):
        for ticket in self.tickets:
            if ticket.stato != "chiuso":
                print(f"ID: {ticket.id_ticket} | "
                      f"Tipo: {ticket.elettrodomestico.tipo} | "
                      f"Stato: {ticket.stato}")


    def totale_preventivi(self):
        totale = 0
        for ticket in self.tickets:
            totale += ticket.preventivo
        return totale

    def statistiche_per_tipo(self):
        lavatrici = 0
        frigoriferi = 0
        forni = 0



        for ticket in self.tickets:
            elettro = ticket.elettrodomestico

            if isinstance(elettro, Lavatrice):
                lavatrici += 1
            elif isinstance(elettro, Frigorifero):
                frigoriferi += 1
            elif isinstance(elettro, Forno):
                forni += 1


print(f"Numero di lavatrici in riparazione: {lavatrici}")
print(f"Numero di frigoriferi in riparazione: {frigoriferi}")
print(f"Numero di forni in riparazione: {forni}")

