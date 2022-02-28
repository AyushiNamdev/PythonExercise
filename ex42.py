## Animal is-a object

class Animal():
    pass

##dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## dog has a name
        self.name = name

##cat is a animal

class Cat(Animal):
    def __init__(self,name):
        ##cat has a name
        self.name = name

## person is an object

class Person(object):
    def __init__(self, name):
        ## person has a name
        self.name = name

        ## person has a pet of some kind
        self.pet = None

## employee is-a person

class Employee(Person):

    def __init__(self, name, salary):
        # i think subclass or employee's parameter
        super(Employee, self).__init__(name)
        self.salary = salary

##fish is a object
class Fish(object):
    pass

#salmon is a fish
class Salmon(Fish):
    pass

#halibut is a fish
class Halubut(Fish):
    pass

##is a

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan

#has a

frank = Employee("Frank", 1200000)

#has a
frank.pet = rover

#is a
flipper = Fish()

##is a
crouse = Salmon()

##is a
harry = Halubut()