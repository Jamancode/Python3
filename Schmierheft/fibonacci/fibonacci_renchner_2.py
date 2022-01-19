def fib1 (n) :
    if n == 1 or n == 2:
        return 1
    return fib1 (n-1) + fib1 (n-2)


def fib2(n) :
    a, b =1, 1
    for i in range(n-1) :
        a,b = b, a+b
    return a

for i in range (1,64) :
    print (fib2(i))        

#fib
print (3445+999)