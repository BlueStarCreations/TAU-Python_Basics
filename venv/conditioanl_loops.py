# Decision Trees:

# Comparison Operators

print(1 < 1)
print(1 <= 1)
print(1 > 1)
print(1 >= 1)
print(1 == 1)
print(1 != 1)

# if, elif, else  are control structures

# if --> shows codes that should run only if certain conditions are meet/present

name = input("What is your name? ")
if name == "Jessica":
    print("Hello, nice to see you {}".format(name))
elif name == "Danielle":
    print("Hello, you are a great person!")
elif name != "Mariah":
    print("You're not Mariah")
elif name == "Kingston":
    print("Hi, {}, let's have lunch soon!".format(name))
else:
    print("Have a nice day!")

""" elif --> shows codes that should run when conditions before are not met, and
 many conditions could possibly be met.
 elif code is run in the order that it appears """

""" else --> statement is used to colse out the if, elif, else code block and can comprise anything that
 you can think of that the user might not do.  """









