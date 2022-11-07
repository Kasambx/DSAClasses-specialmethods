# creating a dictionary
d = {'One':1, 'Two':2, 'Three':3}
print(d)

# adding keys and values 
d['Four']= 4
print(d)

#adding multiple values using update 
d.update({'Five':5, 'Six':6})
print(d)

#testing the occurence of a value in a tuple using in operator
print('seven' in d)
print('Six' in d)

#sorting dictionaries 
sorted(list(d)) # sorts keys
print(d)

sorted(list(d.values()))  # sort values 
print(d)


# key and reverse argumenst in sorted() method
sorted(list(d), key = d.__getitem__)
print(sorted((d), key = d.__getitem__))

d2 ={'one':'uno' , 'two':'deux', 'three':'trois', 'four': 'quatre', 'five':
'cinq', 'six':'six'}
print(d2)

sorted(d2, key=d2.__getitem__)
print(d2)


[d2[i] for i in sorted(d2, key = d2.__getitem__)]
print(d2)


#Dictionaries for text analysis
def wordcount (fname):
    try:
        fhand=open (fname)
    except:
        print("file cannot be opened")
        exit()

    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word]+= 1
    return(count) 

