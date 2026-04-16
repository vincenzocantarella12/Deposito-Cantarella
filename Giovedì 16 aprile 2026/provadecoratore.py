#DECORATORE
    
def decoratore(funzione):
  def wrapper():
    print("Prima della funzione")
    funzione()
    print("Dopo la funzione")
  return wrapper  

@decoratore
def saluta():
    print("Ciao, mondo!")
saluta() 


