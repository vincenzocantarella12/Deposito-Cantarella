# CLASSE VISITA


class Visita:
    
    
    def __init__(self, paziente, medico, data):
        self.paziente = paziente
        self.medico = medico
        self.data = data
        self.accettata = False

    def accetta(self):
        self.accettata = True     
    
     
           