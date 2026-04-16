def fibonacci(n):
    a,b = 0,1
    
    while a < n:
        yield a                         # yield è un ripetitore che restituisce un valore e sospende l'esecuzione della funzione, riprendendo da dove era stata interrotta alla successiva chiamata.
        a,b = b, a + b
        
    print("Fine della sequenza")  #aggiunto io per vedere quando finisce la sequenza
for num in fibonacci(35):
    print(num)

