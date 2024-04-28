import random

def generate_board(questions, pairs):
    # Shuffle the pairs and select half of them for the board
    selected_pairs = random.sample(list(pairs.items()), len(pairs)//2)
    board = selected_pairs + selected_pairs
    random.shuffle(board)
    return board


def display_board(board):
    for i in range(len(board)):
        print(f"{i + 1}. {board[i][0]}")

def play_game(board):
    matched_pairs = []
    attempts = 0
    while len(matched_pairs) < len(board)//2:
        display_board(board)
        print("\nEnter the numbers of two cards you want to flip (e.g., 1 2): ")
        try:
            choice1, choice2 = map(int, input().split())
            if choice1 < 1 or choice1 > len(board) or choice2 < 1 or choice2 > len(board) or choice1 == choice2:
                print("Invalid input. Please enter valid numbers.")
                continue
            card1 = board[choice1 - 1]
            card2 = board[choice2 - 1]
            print(f"\n{card1[0]}: {card1[1]}")
            print(f"{card2[0]}: {card2[1]}")
            if card1[1] == card2[1]:
                matched_pairs.append(card1)
                matched_pairs.append(card2)
                print("\nYou found a match!")
            else:
                print("\nTry again!")
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    print(f"\nCongratulations! You found all the matches in {attempts} attempts.")

def main():
    # Define the questions and pairs
    questions = {
        "Memory Forensics": "What are the artifacts that can be found in memory forensics?",
        "Volatility": "What is Volatility and why is it used?",
        "Volatility Framework": "What components make up the Volatility framework?",
        "Address Spaces": "What types of address spaces does Volatility handle?",
        "Plugins": "What is the purpose of plugins in Volatility?",
        "Preserving the Digital Evidence": "Why is it important to preserve digital evidence?",
        "Software Tools": "What considerations should be made when selecting forensic tools?",
        "Dump Formats": "What are some common memory dump formats?",
    }

    # Pairs of concepts/terms with their descriptions
    pairs = {
        "Memory Forensics": ["Memory Artifacts", "Network connections", "Running processes", "User credentials", "Dynamically Linked Libraries", "Open Window Chat/Contents", "Process Registry Keys"],
        "Volatility": ["Why Volatility", "Open source GPLv2", "A single, cohesive framework", "Written in Python", "Runs on Windows, Linux or Mac analysis systems", "Extensible and scriptable API", "Comprehensive coverage of file formats", "Fast and Efficient algorithms", "Serious and powerful community", "What Volatility is Not"],
        "Volatility Framework": ["VTypes", "Overlays", "Objects and Classes", "Profiles", "Metadata", "System Call Information", "Constant Values", "Native Types", "System Map"],
        "Address Spaces": ["Virtual/Paged Address Spaces", "Physical Space Address"],
        "Plugins": ["Core Plugins", "Analysis plugins"],
        "Preserving the Digital Evidence": ["Decision Making Process", "Risks", "Atomicity", "When to Acquire Memory", "How to Acquire Memory"],
        "Software Tools": ["Tool Evaluation", "Tool Selection"],
        "Dump Formats": ["Raw Memory Dump", "Windows Crash Dump", "Windows Hibernation File", "HPAK Format", "VM Memory"],
    }

    # Generate the game board
    board = generate_board(questions, pairs)
    print("Welcome to the Memory Game!\n")
    input("Press Enter to start the game...")
    play_game(board)

if __name__ == "__main__":
    main()
