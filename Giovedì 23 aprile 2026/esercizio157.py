class UnitaMilitare:
    
    
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
        
        

    def muovi(self):
        print(f"{self.nome} si sta muovendo.")

    def attacca(self):
        print(f"{self.nome} attacca il nemico")

    def ritira(self):
        print(f"{self.nome} si ritira strategicamente.")
        

# CLASSI DERIVATE


class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"{self.nome} costruisce una trincea.")


class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"{self.nome} calibra i cannoni.")


class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"{self.nome} esplora il terreno.")


class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"{self.nome} rifornisce le truppe.")


class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome} conduce una ricognizione.")
        
        


#eredita da classi derivate

   
            
            
    def __str__(self):
        return f"Unità: {self.nome}, Soldati: {self.numero_soldati}"

    
    def __repr__(self):
        return f"UnitaMilitare(nome='{self.nome}', numero_soldati={self.numero_soldati})"

    
    def __len__(self):
        return self.numero_soldati

    
    def __eq__(self, altro):
        if isinstance(altro, UnitaMilitare):
            return self.nome == altro.nome and altro.numero_soldati == altro.numero_soldati
        return False


    def __getattribute__(self, name):
        return super().__getattribute__(name)
    
    
            
            
    
    