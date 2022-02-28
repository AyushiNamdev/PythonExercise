people = 30
cars = 40
buses = 15

if cars> people:
    print("we should take cars")
elif cars>people:
    print("dont take care")
else:
    print("cant decide")

if buses >cars:
    print("too many buses")
elif buses < cars:
    print("too many cars")
else:
    print("we still cant decide")

if people> buses:
    print("alright, lets just take the buses")
else:
    print("fine, let's stay home")