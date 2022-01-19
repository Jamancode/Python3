def fib1(n) :
    if n == 1 or n == 2:
        return 1
    return fib1 (n-1) + fib1(n-2)    

for i in range (1,60) :
    print (fib1 (i))
