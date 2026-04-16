n = int(input("Quanti numeri della sequenza di Fibonacci vuoi vedere? "))

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
        
fibonacci(n)
