import pandas as pd
from prettytable import PrettyTable

def create_dataframe(csv_file):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None

def list_available_controls(df):
    # Create a pretty table
    table = PrettyTable(['Index', 'Identifier'])

    # Populate the pretty table with available control identifiers
    for i, control in enumerate(df['identifier'], start=1):
        table.add_row([i, control])

    # Print the pretty table
    print("Available Controls:")
    print(table)

def get_user_choice():
    while True:
        choice = input("Enter your choice: ").strip()
        if choice.isdigit():
            return int(choice)
        else:
            print("Invalid input. Please enter a number.")

def compare_controls(df):
    # Display available controls
    list_available_controls(df)
    
    # User selects controls for comparison
    selected_controls_indices = input("Enter control numbers (comma-separated): ")
    selected_controls_indices = [int(idx.strip()) for idx in selected_controls_indices.split(',')]

    # Validate selected control numbers
    if any(idx < 1 or idx > len(df) for idx in selected_controls_indices):
        print("Invalid control number(s).")
        return

    # Filter DataFrame for the specified identifiers
    selected_controls = df.iloc[[idx - 1 for idx in selected_controls_indices]]

    # Create a pretty table for the selected controls
    table = PrettyTable()
    table.field_names = selected_controls.columns
    for index, control in selected_controls.iterrows():
        table.add_row(control)

    # Print the pretty table
    print("Selected Controls:")
    print(table)


def get_related_controls(df):
    # Display available controls
    list_available_controls(df)
    
    # User selects a control
    selected_control_index = int(input("Enter control number: ").strip())

    # Validate selected control number
    if selected_control_index < 1 or selected_control_index > len(df):
        print("Invalid control number.")
        return

    # Filter DataFrame for the specified control
    selected_control = df.iloc[selected_control_index - 1]

    # Display related controls
    related_identifiers = selected_control['related'].split(',')
    related_controls = df[df['identifier'].isin(related_identifiers)]

    # Check if any related controls were found
    if related_controls.empty:
        print("No related controls found.")
    else:
        # Create a pretty table for the related controls
        table = PrettyTable(related_controls.columns)
        for index, control in related_controls.iterrows():
            table.add_row(control)

        # Print the pretty table
        print("Related Controls:")
        print(table)


def analyze_related_controls(df):
    # Count frequency of related controls
    related_controls_freq = df['related'].str.split(',').explode().value_counts()

    # Create a pretty table for the related controls frequency
    table = PrettyTable(['Identifier', 'Frequency'])
    for identifier, frequency in related_controls_freq.items():
        table.add_row([identifier, frequency])

    # Print the pretty table
    print("Related Controls Frequency:")
    print(table)

# Example usage
csv_file = "controls.csv"
df = create_dataframe(csv_file)

if df is not None:
    while True:
        print("\nChoose an action:")
        print("1. List available controls")
        print("2. Compare controls")
        print("3. Get related controls for a control")
        print("4. Analyze related controls frequency")
        print("5. Exit")

        choice = get_user_choice()

        if choice == 1:
            list_available_controls(df)
        elif choice == 2:
            compare_controls(df)
        elif choice == 3:
            get_related_controls(df)
        elif choice == 4:
            analyze_related_controls(df)
        elif choice == 5:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose again.")
