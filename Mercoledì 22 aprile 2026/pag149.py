class MembroSquadra:
    
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        print(f"Nome: {self.nome}, Età: {self.eta}")
        
        

class Giocatore(MembroSquadra):
    
    
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia

    def descrivi(self):
        super().descrivi()
        print(f"Ruolo: {self.ruolo}, Numero maglia: {self.numero_maglia}")

    def gioca_partita(self):
        print(f"{self.nome} (numero {self.numero_maglia}) sta giocando come {self.ruolo}!")
        
        