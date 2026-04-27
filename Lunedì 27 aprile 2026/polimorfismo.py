""" class origine():
    
    
    def lavoro():
        pass
    
    
    
class lavoratore_manuale(origine):
    
    def lavoro():
        #modalita 1
        pass
    
    
    
class lavoratore_digitale(origine):
    
    def lavoro():
        #modalità 2
        pass
    
    
    
class lavoratore_nullafacente(origine):
        pass
    
    
    
def fai_lavorare(lavoratore: origine):
    lavoratore.lavoro() """ 







class origine():
    
    def lavoro(self):
        print("Sto facendo un lavoro generico")


class lavoratore_manuale(origine):
    
    def lavoro(self):
        # modalità 1
        print("Sto facendo un lavoro manuale")


class lavoratore_digitale(origine):
    
    def lavoro(self):
        # modalità 2
        print("Sto facendo un lavoro digitale")


class lavoratore_nullafacente(origine):
    pass


def fai_lavorare(lavoratore: origine):
    lavoratore.lavoro()


# Test
a = lavoratore_manuale()
b = lavoratore_digitale()
c = lavoratore_nullafacente()

fai_lavorare(a)
fai_lavorare(b)
fai_lavorare(c)