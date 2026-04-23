""" class Automobile:
    
    numero_ruote = 4               #attributo di classe
    
    def __init__(self, marca, modello):      # costruttore 
        self.marca = marca                   # attributo di istanza
        self.modello = modello               # attributo di istanza
        
    def stampa_info(self):
        print(f"L'automobile è una {self.marca} {self.modello}")
        
auto1 = Automobile("Nissan", "Juke")           #Creazione di un'istanza della classe Automobile
auto2 = Automobile("Fiat", "Panda")
auto3 = Automobile("Lamborghini", "Gallardo")

auto1.marca = "Mercedes"                        #Modifica dell'attributo di istanza 'marca' dell'oggetto auto1
auto1.modello = "Classe E"

auto2.marca = "Ferrari"                         #Modifica dell'attributo di istanza 'marca' dell'oggetto auto2
auto2.modello = "F40"

auto3.marca = "Porsche"                         #Modifica dell'attributo di istanza 'marca' dell'oggetto auto3
auto3.modello = "911"

auto1.stampa_info()                             #Chiamata al metodo per stampare le informazioni dell'auto1
auto2.stampa_info()                             #Chiamata al metodo per stampare le informazioni
auto3.stampa_info()                             #Chiamata al metodo per stampare le informazioni


auto1.numero_ruote = 6                         #Modifica dell'attributo di classe 'numero_ruote' per l'oggetto auto1
print(f"numero_ruote: {auto1.numero_ruote}")
print(f"numero_ruote: {auto2.numero_ruote}")   #Stampa del valore dell'attributo di classe 'numero_ruote' per l'oggetto auto2
print(f"numero_ruote: {auto3.numero_ruote}")   #Stampa del valore dell'attributo di classe 'numero_ruote' per l'oggetto auto3 """

 


    