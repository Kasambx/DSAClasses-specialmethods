#Principles of Algorithim Design 
#Recursiona dn backtracking
#factorial
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

#Backtracking
def bitStr(n,s ):
    if n ==  1: return s
    return [digit + bits for digit in bitStr(1,s) for bits in bitStr(n-1 ,s)] 

print (bitStr(3,'abc'))
