""" #STR REPR

class Libro:
    
    
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
    
    def __str__(self):                                                             # informazioni più semplice per utente
        return f"titolo: {self.titolo}, autore: {self.autore}"
    
    def __repr__(self):                                                                     # informazioni più tecniche con repr per sviluppatore ritorna una stringa
        return f"Libro(titolo[self]: {self.titolo} - autore[self]: {self.autore})"
        
l1 = Libro("Boccata D'Aria", "George Orwell")


print(l1)         #  richiama str più rapida e veloce 
print(repr(l1))


#LEN 


class Squadra:
    
    
    def __init__(self, giocatori: list[str]):
        self.giocatori = giocatori
        
    def __len__(self):                     # serve per semplificare e ritorna l'informazione esistente 
        return len(self.giocatori)


squadra = Squadra(["Pippo", "Caio", "Mirko"])
print(len(squadra))



# EQ


class Prodotto:
    
    
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo
    
    def __eq__(self, altro):                   #altro è p2 
        if not isinstance(altro, Prodotto):               #e' un istanza di prodotto ? se una classe  o sottoclasse se è un istanza di prodotto 
            return False
        
        return self.nome == altro.nome and self.prezzo == altro.prezzo


p1 = Prodotto("Tablet", 120)
p2 = Prodotto("Tablet", 120)


print(p1==p2) """


# GET ATTRIBUTE



class Persona:
    
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    
    def __getattribute__(self, attributo):
        print(f" Sto accedendo all' attributo {attributo} ")
        return super().__getattribute__(attributo)
    
p = Persona("Marta", 23)

print(p.nome)
print(p.eta)



 
        