class Prodotto:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
    
    
class Elettronica(Prodotto):
    
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)             # utilizzo il super per prendre ciò che mi serve
        self.garanzia = garanzia
        
    def descrizione(self):
        print(f"{self.nome} (garanzia {self.garanzia} anni)")
        
        
        
        
class Abbigliamento(Prodotto):
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale
        
    def descrizione(self):
        print(f"{self.nome} in {self.materiale}")
        
        

class Fabbrica:
    
    
    def __init__(self):
        self.inventario = {}                        # dizionario per il numero di prodotti
        
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto.nome in self.inventario:
            self.inventario[prodotto.nome]["quantita"] += quantita
        else:
            self.inventario[prodotto.nome] = {
                "prodotto": prodotto,
                "quantita": quantita
            }
        print(f"Aggiunti {quantita} {prodotto.nome}")
        
        
    
    def vendi_prodotto(self, nome, quantita):                                             # capire se c'è disponibilità
        if nome in self.inventario and self.inventario[nome]["quantita"] >= quantita:
            
            prodotto = self.inventario[nome]["prodotto"]
            self.inventario[nome]["quantita"] -= quantita
            
            profitto = prodotto.calcola_profitto() * quantita
            print(f"Venduti {quantita} {nome}. Profitto: {profitto}€")
        else:
            print("Prodotto non disponibile o quantità insufficiente")
            
            
    
    def resi_prodotto(self, nome, quantita):
        if nome in self.inventario:
            self.inventario[nome]["quantita"] += quantita
            print(f"Resi {quantita} {nome}")
        else:
            print("Prodotto non trovato")
            
            
            
            
            
tablet = Elettronica("Tablet Oppo", 300, 500, 2)
jeans = Abbigliamento("Jeans Levis", 10, 25, "seta")


fabbrica = Fabbrica()


fabbrica.aggiungi_prodotto(tablet, 5)
fabbrica.aggiungi_prodotto(jeans, 10)


fabbrica.vendi_prodotto("Tablet Oppo", 2)
fabbrica.vendi_prodotto("Jeans Levis", 3)


fabbrica.resi_prodotto("Jeans Levis", 1)

            