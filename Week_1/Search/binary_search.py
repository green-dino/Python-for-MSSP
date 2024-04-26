import argparse
import logging

# Setup logging
logging.basicConfig(filename='search_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def search_keywords(keyword_file, binary_file, verbose):
    try:
        # Read keywords
        with open(keyword_file, 'r') as kf:
            keywords = set(kf.read().split())

        # Read binary file
        with open(binary_file, 'rb') as bf:
            binary_data = bf.read()

        # Search for keywords in binary data
        results = {}
        for keyword in keywords:
            index = binary_data.find(keyword.encode())
            if index != -1:
                results[keyword] = {
                    'offset': index,
                    'context': binary_data[max(0, index - 20):index + len(keyword) + 20].decode(errors='replace')
                }

        # Print search results
        if verbose:
            print("Search Results:")
            for keyword, result in results.items():
                print(f"Keyword: {keyword}")
                print(f"Offset: {result['offset']}")
                print(f"Context: {result['context']}")
                print()

        # Log search success
        logging.info("Search completed successfully.")

    except FileNotFoundError as e:
        # Log file not found error
        logging.error(f"File not found: {e.filename}")

    except Exception as e:
        # Log other errors
        logging.error(f"An error occurred: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Search for keywords in a binary file.")
    parser.add_argument("keyword_file", help="File containing keywords")
    parser.add_argument("binary_file", help="Binary file to search")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    args = parser.parse_args()

    # Perform search
    search_keywords(args.keyword_file, args.binary_file, args.verbose)

if __name__ == "__main__":
    main()
