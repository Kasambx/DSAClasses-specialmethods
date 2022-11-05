#Built in data types
# Numeric types 
#working with deciamls 
import decimal
x = decimal.Decimal(3.14); y= decimal.Decimal(2.74)
z= x * y
print(z)

import fractions 
fractions.Fraction(3, 4) # creates the fraction 3/4

fractions.Fraction(0, 5) # creates the fraction from a float
fractions.Fraction(".25") # creates the fraction from a string