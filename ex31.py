print("you enter a dark room with two doors. which door?")

door = input(">")

if door == "1":
    print("there is a giant bear here eating cheesecake, what do you do?")
    print("1. take the cke")
    print("2. scream at the bear")

    bear = input(">")

    if bear == "1":
        print("the bear eats your face off")
    elif bear == "2":
        print("the bear eats your legs off")
    else:
        print("doing %s is better" %bear)

elif door == "2":
    print("you stare into the endless abyss at retina")
    print("1. bluberries")
    print("2. yellow jacker")
    print("3. understanding revolvers yelling melodies")

    insanity = input(">")

    if insanity == "1" or insanity =="2":
        print("Your body sirvives powere by a mind of jello")
    else:
        print("the insanity roots your eyes into a pool of much")
else:
    print("you stumble around and fall on a knife and die")