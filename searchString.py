def process_string(input_str):
    # Step 2: Convert the string to lowercase
    input_str_lower = input_str.lower()

    # Step 3: Count the number of characters in the string
    num_characters = len(input_str)

    # Step 4: Count the number of words in the string
    words = input_str_lower.split()
    num_words = len(words)

    # Step 5: Sort the words in alphabetical order
    sorted_words = sorted(words)

    return input_str_lower, num_characters, num_words, sorted_words

# Input string
input_string = input("Enter a string: ")

# Process the string
lowercase_string, character_count, word_count, sorted_words = process_string(input_string)

# Output results
print("String in lowercase:", lowercase_string)
print("Number of characters:", character_count)
print("Number of words:", word_count)
print("Sorted words:", sorted_words)
