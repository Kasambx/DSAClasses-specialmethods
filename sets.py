#creating a set 
Days = set(["Mon","Tue","Wed","Thur","Fri",'Sat'])
Months = {'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'}
Dates = {21,22,23}
print(Days)
print(Months)
print(Dates )

#accesing variables in a set
for i in Months :
    print(i)
for i in Days :
    print(i)
for i in Dates :
    print(i)

#adding items to a set
Days.add("Great")
print(Days)

#removing items from a set
Days.discard("Great")
print(Days)


#union of sets
Allsets= Days|Months|Dates
print(Allsets)

#intersection of sets using &
#only common elemnts are displayed
Days1 = {1,3,4,5,6}
Days2 = {1,3,4,5,6,7,8,7,8,9,9,6,45}
print(Days1&Days2)

#difference of sets using -
#only uncommon elemnts are displayed
print(Days2 -Days1)

#symmetric difference of sets using ^
#only uncommon elemnts are displayed
print(Days2 ^Days1)


#compare sets
Days1 = {1,3,4,5,6}
Days2 = {1,3,4,5,6,7,8,7,8,9,9,6,45}
print(Days1 == Days2)
print(Days1 <= Days2)
print(Days1 >= Days2)



