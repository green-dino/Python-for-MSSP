# Define the maximum number of words per row
MAX_WORDS_PER_ROW = 5

# Create a simple list
pangram  = "The quick brown fox jumped over the lazy dog here are more words to keep the list of words"

# Convert pangram to all lowercase
pangram  = pangram.lower()

# Create a list of words by splitting the pangram
wordList = pangram.split()

# Eliminate duplicates by converting the list to a set
wordSet  = set(wordList)

# Convert the set back to a list to preserve unique words
wordList = list(wordSet)

# Sort the list alphabetically
wordList.sort()

# Apply string manipulation functions

# Convert the entire pangram to uppercase
upper_case = pangram.upper()

# Capitalize the first letter of the pangram
capitalized = pangram.capitalize()

# Remove leading and trailing whitespace from the pangram
stripped = pangram.strip()

# Replace all occurrences of 'a' with 'z' in the pangram
replaced = pangram.replace('a', 'z')

# Initialize a counter for printing words in columns
cnt = 0

# Print the resulting word list in columns
print("Resulting Word List in Columns\n")

# Print the results of string manipulation functions
print("Uppercase:\n", upper_case)
print("Capitalized first Letter:\n", capitalized)
print("Stripped:\n", stripped)
print("Replaced 'a' for 'z':\n", replaced)

# Iterate through each word in the sorted word list
for eachWord in wordList:
    # Print each word with a fixed width of 15 characters
    print('{:15s}'.format(eachWord[0:15]), end='')  # Ensure that words longer than 15 characters are truncated
    
    # Increment the counter
    cnt += 1
    
    # Check if the maximum number of words per row has been reached
    if cnt >= MAX_WORDS_PER_ROW:
        # Move to the next line
        print()
        
        # Reset the counter
        cnt = 0
