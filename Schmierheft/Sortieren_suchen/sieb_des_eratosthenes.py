from math import sqrt, ceil           #primzahlen generator

def eratosthenes(n):
    gestrichen = [False]*n
    gestrichen[:2] = [True, True]
    for i in range(2,ceil(sqrt(n))):
        if  not gestrichen[i]:
            for j in range(i**2,n,i):
                gestrichen[j] = True

    for i,gestr in enumerate(gestrichen):
        if not gestr:
            print(i)            

import time
eratosthenes(2000)           