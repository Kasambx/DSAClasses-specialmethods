

from collections import Counter
#creating a counter from a iterable
c1 = Counter('anysequence')
# counter creation from mapping 
c2= Counter({'a':1,'c':1,'e':3})
#creating counter from keyword arguments
c4=Counter(a=1, c=1, e=3)

print(c1)


#counters return 0 when they miss a value unlike a dictionary which returns key error
ct = Counter()
ct.update('abca') #populates the object
print(ct)
ct.update ({'a':3}) #updates the 'a' count
print(ct)

#creating an iterator out of a counter object by using elements() method
for item in ct:
    print('%s:%d' % (item, ct[item]))





