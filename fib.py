def fib(n):    # write Fibonacci series up to n
    a = 0
    b = 1
    while b < n:
        print(b, end=' ')
        a = b
        b = a+b
    print()

fib(76)

def fibs(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

fibs(76)