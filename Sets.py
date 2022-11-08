s = {'xy', 2 ,(6,9)}
s1 = {'Kasamba', 1,4, 6,(4,8)}

print(s)
print(s1)
print(s-s1)
#lem()
print(len(s1))

#s.copy()
print(s.copy())

#s.difference()
print(s.difference(s1))

#s.intersection(t)
print(s.intersection(s1))

#s.isdisjoint(t)
print(s.isdisjoint(s1))

#s.issubset(t)
print(s.issubset(s1))

#s.issupersetK(t)
print(s.issuperset(s1))

#s,symmetric_difference(t)
print(s.symmetric_difference(s1))

#s.union()
print(s.union(s1))

#looping through operators in a set
for i in s1 : 
    print(i) 
  

        # immutable sets /frozenset
#adding a set to another set 
# produces an error 
#s1.add(s) #sets cannot be used as members of others sets because they are mutable hence they are not hashable

#adding a frozen set to another set 
s1.add(frozenset(s))
print(s1)

# using frozenset as a key to a dictionary
fs1 = frozenset(s1) 
fs2 = frozenset(s)
print(fs1)
print(fs2)


