class Parent(object):
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def altered(self):
        print("child, before parent altered()")
        super(Child,self).altered()
        print("child, sfter parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
