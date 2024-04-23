# Iteration over a Sequence
print("Iteration over a Sequence:")
for i in range(5):
    print(i)
print()

# Generating Lists
print("Generating Lists:")
even_numbers = list(range(2, 11, 2))
print("Even Numbers from 2 to 10:", even_numbers)
print()

# Indexing Lists
print("Indexing Lists:")
my_list = ['a', 'b', 'c', 'd', 'e']
for i in range(len(my_list)):
    print("Index:", i, "Value:", my_list[i])
print()

# Conditional Iteration
print("Conditional Iteration:")
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
print()

# Slicing
print("Slicing:")
r = range(10)
print("Slice of range(10) from index 2 to 5:", r[2:6])
print()

# Arithmetic Progression
print("Arithmetic Progression:")
start = 0
stop = 100
step = 10
for i in range(start, stop, step):
    print(i)
print()

# Nested Loops
print("Nested Loops:")
for i in range(3):
    for j in range(2):
        print(i, j)
