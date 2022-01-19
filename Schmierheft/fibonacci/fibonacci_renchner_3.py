def fib(n):
    a,b = 0,1
    for i in range(n-1):
        nächste_fib = a+b
        neue_a = b
        neue_b = nächste_fib
        a,b = neue_a, neue_b
    return b

def fibi(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b, a+b
    return b

def fibr(n):
    if n < 2: return n
    return fibr(n-1) + fibr(n-2)

def fibd(n,tiefe=0):
    print("   "*tiefe, n)
    if n < 2: return n
    return fibd(n-1,tiefe+1) + fibd(n-2,tiefe+1)

#print(fibd(13))            

def fibf(n,tiefe=0):
    print("   "*tiefe, n)
    if n < 2: return n
    a = fibf(n-1,tiefe+1)
    print("  "*tiefe,"Fib_n-1",a)

    b = fibf(n-2,tiefe+1)
    print("  "*tiefe,"Fib_n-2",b)
    return a+b

print(fibf(7))            



