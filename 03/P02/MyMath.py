# بسم الله الرحمن الرحيم

def my_fib(start, stop):
    a = start
    b = 1

    while a < stop:
        print(a)
        a,b = b, a+b

my_fib(0, 10) 