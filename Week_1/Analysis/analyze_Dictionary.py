def read_py_file(py_file):
    """
    Reads a Python file containing dictionaries and extracts the dictionaries.

    Args:
    - py_file: The path to the Python file.

    Returns:
    - A list of dictionaries extracted from the Python file.
    """
    extracted_dicts = []
    with open(py_file, 'r') as file:
        exec(file.read(), globals())  # Execute the Python code in the file
        extracted_dicts.extend(data)
    return extracted_dicts

def analyze_dictionaries(data):
    """
    Analyzes the dictionaries extracted from the Python file.

    Args:
    - data: A list of dictionaries.

    Returns:
    - A dictionary containing analysis results.
    """
    analysis_results = {}

    # Number of dictionaries
    num_dicts = len(data)
    analysis_results['num_dicts'] = num_dicts

    # List of all keys
    all_keys = set()
    for d in data:
        all_keys.update(d.keys())
    analysis_results['all_keys'] = list(all_keys)

    # Relationships between keys
    relationships = {}
    for key1 in all_keys:
        relationships[key1] = {}
        for key2 in all_keys:
            common_dicts = sum(1 for d in data if key1 in d and key2 in d)
            relationships[key1][key2] = common_dicts
    analysis_results['relationships'] = relationships

    return analysis_results

def print_analysis_results(analysis_results):
    """
    Prints the analysis results.

    Args:
    - analysis_results: A dictionary containing analysis results.
    """
    print("Number of dictionaries:", analysis_results['num_dicts'])
    print("All keys:", analysis_results['all_keys'])
    print("Relationships between keys:")
    for key1, rels in analysis_results['relationships'].items():
        print(f"- {key1}:")
        for key2, common_dicts in rels.items():
            print(f"  - {key2}: {common_dicts} common dictionaries")

def main():
    # Path to the Python file containing dictionaries
    py_file = 'output.py'
    
    # Read dictionaries from the Python file
    data = read_py_file(py_file)

    # Analyze the dictionaries
    analysis_results = analyze_dictionaries(data)

    # Print the analysis results
    print_analysis_results(analysis_results)

if __name__ == "__main__":
    main()
