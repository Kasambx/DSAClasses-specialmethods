#collections
#ADT 
#Deques
from collections import deque 

dq = deque('abc') # creates deque (['a','b','c'])
dq.append ('d') # adds d
print(dq)

dq.appendleft('s') # appends to the left 
print(dq)
dq.extend('efg') # adding multiple items to the deque
print(dq)
dq.extendleft('xyz') # adding multiple items to the left
print(dq)
dq

print(dq.pop())  #returns & removes item form the right
print(dq)

print(dq.popleft()) # returns and retrieves items from the left
print(dq)