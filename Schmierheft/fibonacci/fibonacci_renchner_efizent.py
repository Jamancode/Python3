def fib1 (n) :
    if n == 1 or n == 2:
        return 1
    return fib1 (n-1) + fib1 (n-2)


def fib2(n) :
    a, b =1, 1
    for i in range(n-1) :
        a,b = b, a+b
    return a

for i in range (1,90) :
    print (fib2(i))        

# fibonacci kann man efizent oder nicht so efizent berechnen,
# teste hierzu die print ausgaben von fib1 und fib2 aus. Hier siehst du das fib2 sehr schnell angezeigt wird. 
# hingegen fib1 ab schritt 35 immer langsamer wird!