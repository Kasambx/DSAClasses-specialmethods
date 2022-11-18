#array
from array import *
array = array('b', [1,2,3,4,5,6])
for i in array :
    print(i)

#adding using the key
array.insert(1,80)
print(array)

#deleting an element
array.remove(80)
print(array)

#finding the position of the element
print(array.index(5))

#updating the array
array[5] = 100 
print(array)








