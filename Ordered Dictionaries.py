#Ordered Dictionaries 
from collections import Counter
from collections import OrderedDict
#creating a counter from a iterable
c1 = Counter('anysequence')
# counter creation from mapping 
c2= Counter({'a':1,'c':1,'e':3})
#creating counter from keyword arguments
c4=Counter(a=1, c=1, e=3)

print(c1)

ct = Counter()
ct.update('abca') #populates the object
print(ct)
ct.update ({'a':3}) #updates the 'a' count
print(ct)

#creating an iterator out of a counter object by using elements() method
for item in ct:
    print('%s:%d' % (item, ct[item]))

# ----------Ordered dictionaries--------------

ct.update({"a":-3,"b":-2,"d":3, "e":2})
sorted(ct.elements())  # return a sorted list
print(sorted(ct.elements()) )

print(ct.most_common())
ct.subtract({'a':2})
print(ct)

#creating a sorted dict using sorted method
od1= OrderedDict()
od1['one'] = 1
od1['two'] = 2
od2 = OrderedDict() 
od1['two'] = 2
od2['one'] = 1

print(od2==od1)


