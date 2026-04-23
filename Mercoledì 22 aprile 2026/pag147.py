class Animale:
    
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def fai_suono(self):
            print(f"{self.nome} ha {self.eta} fa un suono generico")
            
            
class Leone(Animale):
    def fai_suono(self):
        print (f"{self.nome} ha {self.eta} anni e sta ruggendo")
    def caccia(self):
        print (f"{self.nome} ha {self.eta} anni e sta cacciando una giraffa")


class Pappagallo(Animale):
    def fai_suono(self):
        print (f"{self.nome} ha {self.eta} anni e imita")
        
        
class Coccodrillo(Animale):
    def fai_suono(self):
        print (f"{self.nome} ha {self.eta} anni e come fa?")
        
        


leone = Leone("Vincenzo", 29) 
pappagallo = Pappagallo("Mirko", 31)
coccodrillo = Coccodrillo("Edoardo", 25)


leone.fai_suono()
leone.caccia()
pappagallo.fai_suono()
coccodrillo.fai_suono()