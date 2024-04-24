import csv

def read_csv_to_dict(csv_file):
    """
    Reads a CSV file and converts each row into a dictionary.

    Args:
    - csv_file: The path to the CSV file.

    Returns:
    - A list of dictionaries where each dictionary represents a row in the CSV file.
    """
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def write_dicts_to_py(data, output_file):
    """
    Writes a list of dictionaries to a Python file.

    Args:
    - data: A list of dictionaries.
    - output_file: The path to the output Python file.
    """
    with open(output_file, 'w') as file:
        file.write("data = [\n")
        for row in data:
            file.write("    {\n")
            for key, value in row.items():
                file.write(f"        '{key}': '{value}',\n")
            file.write("    },\n")
        file.write("]\n")

def main():
    # Path to the input CSV file
    input_csv_file = 'controls.csv'
    
    # Read CSV to dictionaries
    data = read_csv_to_dict(input_csv_file)

    # Path to the output Python file
    output_py_file = 'output.py'
    
    # Write dictionaries to Python file
    write_dicts_to_py(data, output_py_file)
    print("Python code successfully written to", output_py_file)

if __name__ == "__main__":
    main()
