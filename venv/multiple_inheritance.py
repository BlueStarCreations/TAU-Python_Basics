
"""
Multiple Inderitance:
When one class inherits from multiple classes, and is able to use
attributes and methods from both classes.

Pro: include Ability to reuse small amounts of code in multiple classes and mix-ins.
Cons: include the Order of inheritance matters.  Inheriting from multiple classes can become
quite complicated depending on the number of the classes, names of the class methods and other factors,
including common attributes shared among multiple parent classes.

There can be more maintenance involved when refactoring code that is using multiple inheritance.

There are 2 ways to do multiple inheritance in Python.

1st: is not Pythonic, and requires a bit more maintenance.  However, it's easier to see exactly what's happening.
2nd: way is to continue to use the "super" method as you did in single inheritance.
However, this method can be complicated and quite confusing.

1st method is used below.

class Animal():
    def __init__(self, sound, look):
        ....

class Place():
    def __init__(self, climate, lat, lon):
        ...

class Mammal(Animal, Place):
    def __init__(self, sound, look, lat, lon, food)
        Animal.__init__(self, sound, look)
        Place.__init__(self, climate, lat, lon)
        self.food = food

"""

# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))


# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirts(self):
        print("{} {} on sale!".format(self.color, self.name))


Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirts()














