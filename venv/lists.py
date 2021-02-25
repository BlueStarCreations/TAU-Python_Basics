""" Lists: --> Collection of data,
 Can contain any/all data types in a single list
 Can contain other collections (lists, dictionaries, tuples) as list items
 Mutable (items can be added, removed, changed)
 Maintain order (can use index to find an item)"""


# List methods:
# Add to list

fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

print(fruits, years)


fruits.append("oranges")
print(fruits)

fruits.extend(years)
print(fruits)

# Remove from list

fruits.remove("oranges")
print(fruits)

fruits.pop(0)
print(fruits)

fruits.pop(-1)
print(fruits)

# Can't sort the fruit list because it can only be used with like items
#fruits.sort()
#print(fruits)


numbers = [5, 1945, 6, 17, 87, 75.67, 20.86877]
numbers.sort()
print(numbers)


# Checking membership in a list:

frts = ["apples", "peaches", "apples", "pears", "apples"]
yrs = [3, "1998", 2.5, 987, "1994"]

print("apple" in frts)
print("apples" in frts)

print(frts.count("apples"))
print(frts.count("apple"))

print(frts.index("apples"))
