# Creating a dictionary manually
numbers_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
}

# Creating a dictionary using a comprehension
squares = {number: number**2 for number in range(1, 101)}

# Accessing dictionary elements
print("Accessing dictionary elements:")
print("Number 2 spelled out:", numbers_dict[2])
print("Square of 7:", squares[7])
print()

# Dictionary methods
print("Dictionary methods:")
print("Keys:", numbers_dict.keys())
print("Values:", numbers_dict.values())
print("Items:", numbers_dict.items())
print()

# Iterating over a dictionary
print("Iterating over a dictionary:")
print("Keys and Values:")
for key, value in numbers_dict.items():
    print("Key:", key, "| Value:", value)
print()

# Checking for existence of keys
print("Checking for existence of keys:")
print("Is 5 in the numbers_dict?", 5 in numbers_dict)
print("Is 4 in the numbers_dict?", 4 in numbers_dict)
print()

# Modifying dictionaries
print("Modifying dictionaries:")
# Adding a new key-value pair
numbers_dict[4] = 'four'
print("After adding 'four':", numbers_dict)
# Modifying an existing value
numbers_dict[2] = 'TWO'
print("After modifying 'two':", numbers_dict)
# Deleting a key-value pair
del numbers_dict[3]
print("After deleting 'three':", numbers_dict)
print()

# Clearing a dictionary
print("Clearing a dictionary:")
squares.clear()
print("Squares dictionary after clearing:", squares)
