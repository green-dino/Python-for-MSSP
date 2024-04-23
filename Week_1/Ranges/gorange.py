# Basics of range

# Generating a list of numbers from 0 to 19
list_of_twenty = list(range(20))
print("This is a list of numbers from 0 to 19:", list_of_twenty)

# Generating a list of numbers from 0 to 39
list_of_forty = list(range(40))
print("This is a list of numbers from 0 to 39:\n", list_of_forty)

# Using the range function to generate a list of numbers with default start (0) and stop (5) parameters
print("Generating a list of numbers from 0 to 4:")
for i in range(5):
    print(i, end=" ")

# Using start (2), stop (11), and step (2) parameters to generate a list of even numbers
print("\nGenerating even numbers from 2 to 10:")
for i in range(2, 11, 2):
    print(i, end=" ")

# Generating numbers from 10 to 1 in reverse with a step of -1
print("\nGenerating numbers from 10 to 1 in reverse:")
for i in range(10, 0, -1):
    print(i, end=" ")
