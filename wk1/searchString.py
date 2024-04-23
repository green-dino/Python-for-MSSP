# Define a function named process_string which takes a string as input
def process_string(input_str):
    # Step 2: Convert the string to lowercase
    input_str_lower = input_str.lower()  # Convert the input string to lowercase and store it in input_str_lower

    # Step 3: Count the number of characters in the string
    num_characters = len(input_str)  # Count the number of characters in the original input string

    # Step 4: Count the number of words in the string
    words = input_str_lower.split()  # Split the lowercase string into words and store them in the 'words' list
    num_words = len(words)  # Count the number of words in the 'words' list

    # Step 5: Sort the words in alphabetical order
    sorted_words = sorted(words)  # Sort the list of words alphabetically

    # Return the lowercase string, number of characters, number of words, and sorted words
    return input_str_lower, num_characters, num_words, sorted_words

# Ask the user to input a string and store it in the variable 'input_string'
input_string = input("Enter a string: ")  

# Call the process_string function with the input string
# Unpack the returned values into variables: lowercase_string, character_count, word_count, sorted_words
lowercase_string, character_count, word_count, sorted_words = process_string(input_string)

# Output the results
print("String in lowercase:", lowercase_string)  # Print the input string converted to lowercase
print("Number of characters:", character_count)  # Print the number of characters in the input string
print("Number of words:", word_count)  # Print the number of words in the input string
print("Sorted words:", sorted_words)  # Print the words in the input string sorted alphabetically
