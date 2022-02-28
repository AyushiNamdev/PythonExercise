class Other(object):

    def override(self):
        print ("Other override()")
    def implicit(self):
        print("Other implicit()")
    def altered(self):
        print ("other altered()")

class child(object):

    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("Child override()")
    def altered(self):
        print("child, before other altered()")
        self.other.altered()
        print("Child, after other altered()")

son = child()
son.implicit()
son.override()
son.altered()