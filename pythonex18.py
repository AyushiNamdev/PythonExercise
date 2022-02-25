def print_two(*args):  #created a function
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#we can do this like this
def print_two_again(arg1, arg2):
    print("arg1: %r,.arg2: %r" %(arg1,arg2))

#this just takes one argument
def print_one(arg1):
    print("agr1: %r" %arg1)

#this one takes no argument
def print_none():
    print("I got nothin")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()