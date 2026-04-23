""" # ESERCIZIO 1

class Punto:
    
    
    def __init__(self, x, y):         # definisco i 2 attributi
        self.x = x
        self.y = y

    def muovi(self, dx, dy):           # metodo per muovere il punto
        self.x += dx
        self.y += dy

    def distanza_da_origine(self):                      # calcolo la distanza teorema di Pitagora
        return (self.x**2 + self.y**2) ** 0.5
    
    
    # come utilizzare la classe Punto
    
p = Punto(3, 4)                            # coordinate iniziali 

print("Prima:", p.x, p.y)
print("Distanza:", p.distanza_da_origine())

p.muovi(1, 8)                             # aggiungo dei valori

print("Dopo:", p.x, p.y)
print("Nuova distanza:", p.distanza_da_origine())                #printo la nuova distanza """



#ESERCIZIO 2


class Libro:
    

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def stampa_info(self):
        print(f"Il libro '{self.titolo}' è stato scritto da '{self.autore}' e ha {self.pagine} pagine.")



libro1 = Libro("Harry Potter 1", "J.K. Rowling", 1178)
libro2 = Libro("Harry Potter 2", "J.K. Rowling", 1342)

libro1.stampa_info()
libro2.stampa_info() 




