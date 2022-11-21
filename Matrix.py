#matrix
from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
   ['Wed',15,21,20,19],['Thu',11,20,22,21],
   ['Fri',18,17,23,22],['Sat',12,22,20,18],
   ['Sun',13,15,19,16]])
m = reshape(a,(7,5))
print(m)

#accessing variables in a matrix 
print(m[2][2])

#adding a row 
m_r = append(m,[['Avg',20,25,45,76]],0)
print(m_r)


#ading a column 
m_c = insert(m,[3],[[4],[3],[6],[9],[0],[1],[10]],1)
print(m_c)

#deleting a row 
m= delete(m,[5],0)
print(m)

#deleting a column
m = delete (m,[3], 0)
print(m)


#updating a row
m[2] = ['Sun',13,15,19,16]
print(m)












