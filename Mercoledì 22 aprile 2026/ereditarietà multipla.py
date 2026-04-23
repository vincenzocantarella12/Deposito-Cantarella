class Veicolo:
    
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def mostra_info(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")
        

class DotazioniSpeciali:
    
    
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', ' .join(self.dotazioni)}")
            
class AutoSportiva(Veicolo, DotazioniSpeciali):
    
    
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo. __init__(self, marca, modello)                # con il punto richiami il costruttore
        DotazioniSpeciali. __init__ (self, dotazioni)
        self.cavalli = cavalli
        
    def mostra_info(self):
        super().mostra_info()                      # o super o self prende solo la prima classe ereditata (super)
        print (f"Potenza: {self.cavalli}")
        self.mostra_dotazioni()
        
auto_sportiva = AutoSportiva("Ferrari", "F8", ["Controllo Trazione", "Airbag laterali", "ABS"], 720)   # parentesi quadre per definire una lista, se no va ad intero


auto_sportiva.mostra_info()


     
        
        
    
        

        
    
        
    