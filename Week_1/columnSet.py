# Define the maximum number of words per row
MAX_WORDS_PER_ROW = 5

# Pangrams: List containing multiple pangrams
pangrams = [
    "The quick brown fox jumped over the lazy dog here are more words to keep the list of words",
    "How vexingly quick daft zebras jump!",
    "The five boxing wizards jump quickly.",
    "The quick brown fox jumps over the lazy dog."
]

# Initialize an empty set to store unique words
unique_words_set = set()

# Process each pangram individually to create a set of unique words
for pangram in pangrams:
    # Convert pangram to lowercase and split into words
    word_list = pangram.lower().split()
    # Add words to the set
    unique_words_set.update(word_list)

# Convert the set back to a list to preserve unique words
word_list = list(unique_words_set)

# Sort the list alphabetically
word_list.sort()

# Initialize a counter for printing words in columns
cnt = 0

# Print the resulting word list in columns
print("Resulting Word List in Columns\n")

# Iterate through each word in the sorted word list
for eachWord in word_list:
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
