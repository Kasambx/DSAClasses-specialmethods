#namedtuples
from collections import defaultdict

dd = defaultdict(int)

words =str.split('red blue green red yellow blue red green green red')

for word in words :
    dd[word] +=1

print(dd)

from collections import namedtuple
space = namedtuple('space','x y z')
s1 = space(x= 2.0,y = 4.0, z = 10) # we can also use space (2.0,4.0,10)
print(s1.x * s1.y * s1.z) # gets the volume 


#using the as dict method to return an ordered Dict 
space2 = namedtuple('space2', 'x def z', rename = True)
s1 = space2(3,4,5)
print(s1._1)


#using the make() method to create a named tuple 
sl = [4,5,6]
print(space._make(sl))

