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
    
    
    
    
    
    
    
    class ControlloMilitare:
        
        

    def __init__(self):
        self.unita_registrate = []

    def registra_unita(self, unita):
        self.unita_registrate.append(unita)

    def mostra_unita(self):
        for u in self.unita_registrate:
            print(u)

    def dettagli_unita(self, nome):
        for u in self.unita_registrate:
            if u.nome == nome:
                print(u.nome, u.numero_soldati)
                return
        print("Unità non trovata")