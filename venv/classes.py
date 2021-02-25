""" Classes:
--> Single file per class OR Multiple classes can be contained in 1 file

--> Inheritance: derived/child class can use attributes and methods of parent class
--> Multiple Inheritance: derived/child class can inherit attributes and methods from more than one class
--> Polymorphism: derived/child classes can override class methods of parent class

Class Features:
--> Class Variables: for use by all the methods in the class
--> Instance Variables: for use by the specific method in which the variable is declared/created

_init_ method:
sets attributes for an object at object creation; is a constructor

_init_ method is not required BUT is generally used to set default state of object when it is created
 The _init_ method is the first method for a class

 ** the word constructor is another word that can be used to refer to the _init_ method

self:
Self-referencing variable
Used to reference the object that is constructed by the init method

"""

class Person:
    def __init__(self, firstname, lastname, health, status):
        """ initialize attributes to be used in/available for all c
        class methods in this class, and for class objects created
        by this class. """
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        """ All people introduce themselves """
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad right now".format(self.firstname))


    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif slef.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()



