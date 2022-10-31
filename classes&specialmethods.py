#classes in python
class Employee(object):
    numEmployee = 0
    def __init__(self,name, rate):
        self.owed = 0
        self.name =name 
        self.rate = rate 
        Employee.numEmployee +=1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.owed += numHours * self.rate
        return("%.2f hours worked" % numHours)

    def pay(self):
        self.owed = 0
        return("payed %s " % self.name) 
 
emp1= Employee("Kasamba", 72.5)
emp2 = Employee("Junior", 90.7)
print(Employee.numEmployee)
print(emp1.hours(70))
print(emp1.owed)
print(emp1.pay())

#special methods
class my_class():
    def __init__(self, greet):
        self.greet = greet
    def __repr__(self):
        return 'a custom object (%r)' %(self.greet)

a=my_class("giday")
print(a)
