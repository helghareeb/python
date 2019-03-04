# بسم الله الرحمن الرحيم

def fib(start, stop):
    a,b = start,1       # Mutliple Assignment
    while a < stop:     # While Block
        print(a)
        a, b = b, a+b

fib(0,10)
