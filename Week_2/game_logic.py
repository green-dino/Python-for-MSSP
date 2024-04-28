import random

def generate_board(pairs):
    selected_pairs = random.sample(list(pairs.items()), len(pairs) // 2)
    board = selected_pairs + selected_pairs
    random.shuffle(board)
    return board

def display_board(board):
    for i, (topic, _) in enumerate(board, start=1):
        print(f"{i}. {topic}")

def display_pair(topic, pairs):
    pair = random.choice(pairs[topic])
    print(f"\nPair for '{topic}': {pair}")

def display_questions(questions, topic):
    if topic in questions:
        print(f"\nQuestion for '{topic}': {questions[topic]}")
    else:
        print(f"\nNo question found for '{topic}'.")
