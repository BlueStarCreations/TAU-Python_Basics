""" Dictionaries:
contents: --> key/value pairings
mutable: --> can be changed
order: --> maintain order of entry as of python 3.7
syntax: --> curly braces contain keys and values;
 keys and values are separated by colon  """


stuff = {"food": 15, "energy": 100, "enemies": 3}

# Look at what's in the dictionary
print(stuff.get("food"))

print(stuff.items())

print(stuff.keys())

# Remove items and insert keys and values

print(stuff.popitem())
print(stuff)


print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends", 123))
print(stuff)


new_items = {"rocks": 4, "arrows": 18}

stuff.update(new_items)
print(stuff)

new_items = {"rocks": 2, "arrows": 5}
stuff.update(new_items)
print(stuff)

# update and add at the same time

up_new = {"food": 3, "webs": 2}
stuff.update(up_new)
print(stuff)

# add items directly to update method to use it'

stuff.update(food = 450)
print(stuff)

stuff.update(food = 500, cookies = 8)
print(stuff)






