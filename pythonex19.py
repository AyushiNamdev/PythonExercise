def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("you had %d cheese!" %cheese_count)
    print("You have %d boxex of crackers" %boxes_of_crackers)
    print("Man that' enough for a party")
    print("get a blanker.\n")

print("W can just give the fucntion numbers directly")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)
