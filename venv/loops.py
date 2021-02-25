# Loops are useful construct for when you want to repeat the same actions any number of times.

""" For Loops: --> is useful when you want to iterate over each item in a list.  It allows you to repeat your
action for every item in the list or for a specified number of items in the list. """

fruits = ["apple", "orange", "pear", "cherries", "grapes"]

for fruit in fruits:
    print("Would you like {} ?".format(fruit))


# OR you can use the variable "i" instead of "fruit"

for i in fruits:
    print("Would you like {} ?".format(i))

for number in range(1, 11):
    print("Number {}".format(number))


""" While Loop: --> Will run any time a condition remains true. """

temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1

""" Loop Controls: 
Break: --> End the loop. Go to the next statement in the program (outside the loop)
Continue: --> Skips current part of the loop. Moves to the next part of the loop
Pass: --> Skips any part of the loop where "pass" appears.  Best used for testing code.

"""

temp_f = 45
while temp_f > 32:
    print ("The water is {} degrees. ".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

for number in range(1, 14):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))

for number in range(1, 12):
    if number == 3:
        pass
    else:
        print("The number is {}.".format(number))


