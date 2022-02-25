from sys import argv

script, filename = argv

print("W are going to erase %r." %filename)
print("If you dont want that, hit ctrl-c (^C).")
print("If you do want that, hit return")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input()
line2 = input()
line3 = input()

print("I'm going to write these to the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we close it")
target.close()