from game_logic import generate_board, display_board, display_pair, display_questions

def play_game(questions, pairs):
    board = generate_board(pairs)
    matched_pairs = []
    attempts = 0
    while len(matched_pairs) < len(board) // 2:
        display_board(board)
        try:
            choice = int(input("\nEnter the number of the topic you want to select (or 0 to exit): "))
            if choice == 0:
                print("Exiting game...")
                return
            elif 1 <= choice <= len(board):
                topic = board[choice - 1][0]
                print("\n1. Display Pair")
                print("2. Display Question")
                sub_choice = int(input("Enter your choice: "))
                if sub_choice == 1:
                    display_pair(topic, pairs)
                elif sub_choice == 2:
                    display_questions(questions, topic)
                else:
                    print("Invalid choice. Please enter 1 or 2.")
                input("\nPress Enter to continue...")
                attempts += 1
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
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

    print("Welcome to the Memory Game!\n")
    input("Press Enter to start the game...")
    play_game(questions, pairs)

if __name__ == "__main__":
    main()
