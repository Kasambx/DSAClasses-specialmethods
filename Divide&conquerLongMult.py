#implementation of the kasatsuba algorithim 
from math import log10
import random 
import math
def karatsuba(x,y):

    #The base case for recursion 
    if x<10 or y<10 :
        return x*y

    #sets n, the number of digits in the highest input number 
    n = max (init (log10(x)+ 1 ), init (log10(y)+1))

    #rounds up n/2
    n_2 = int(math.ceil( n/2.o))
    #adds 1 if n is uneven
    n = n if n% 2 == 0 else n+1

    #splits the input numbers 
    a,b = divmod(x, 10**n_2)
    c,d = divmod(y, 10**n_2)

    #applies the three recursive steps 
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba((a+b),(c+d)) - ac - bd 

    #performs the multiplication 
    return ((10**n)*ac) + bd + ((1**n_2)*(ad_bc ))

    def test(): 
        for i in range(1000):
        x = random.randint(1,10**5)
        y = random.randint(1,10**5)
        expected = x * y
        result = karatsuba(x, y)
        if result != expected:
            return("failed")
    return('ok')