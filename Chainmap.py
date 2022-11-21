#chainmap
import collections
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = collections.ChainMap(dict1, dict2)

#create a single dictionary
print(chain.maps,'\n')

print('keys = {}'.format(list(chain.keys())))
print('values = {}'.format(list(chain.values())))
print()

#print all elements from the result
print('elements:')
for key,val in chain.items():
    print('{} = {}'.format(key,val))
print()


#find a specific value in the result
print("a in chain :{}".format(("b" in chain)))
print("c in chain :{}".format(("c" in chain)))