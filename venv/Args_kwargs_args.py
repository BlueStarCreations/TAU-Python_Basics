
# Postitional Arguments

def user_info(name, age, city):
   ''' This function prints name, age, city from an atgument
   provided to the function.'''

   print("{} is {} years old, from {}".format(name, age, city))


user_info("Rose", 58, "Mountain View")

# You get an error indicating its missing required positional argument
#user_info(40, "San Jose")


# Keyword arguments

def user_info(name, age=0, city="Tucson"):
    print("{} is {} years old, from {}". format(name, age, city))

user_info("Summer")

user_info(age=56, name="Kadeem")


""" *args --> Allows for unlimited variables to be passed into a
function without defining them ahead of time

def add(*args):
    print(sum(args))
"""

''' **kwargs --> Allows for unlimited keyword arguments to be
passed into a function without defining them ahead of time 

def application(**kwargs):
    print(**kwargs)
    
application(name="Jess", email="mail@mail.com")
application(name = "Susan", surname = "Johnson", age=45)

'''

""" Combining arg types: 
All 3 argument types can be used in a single function.  They must be
used in order: formal positional arguments, *args, **kwargs

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}.  Her emai is {}.".format(fname, lname, company, email))
 
application("Susan", "Winters", "mail@mail.com", "TeachCode.org", 7500, hire_date = "September 2010")   
"""


def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}.  Her emai is {}.".format(fname, lname, company, email))


application("Susan", "Winters", "mail@mail.com", "TeachCode.org", 7500, hire_date="September 2010")