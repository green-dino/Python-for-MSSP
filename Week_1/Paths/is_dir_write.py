import argparse
import os

def validate_directory_writable(directory):
    """
    Validate a directory path as existing and writable.
    """
    if not os.path.isdir(directory):
        raise argparse.ArgumentTypeError(f"Invalid directory: {directory} does not exist.")
    if not os.access(directory, os.W_OK):
        raise argparse.ArgumentTypeError(f"Invalid directory: {directory} is not writable.")
    return directory

def main():
    parser = argparse.ArgumentParser(description="Validate a directory path.")
    parser.add_argument("directory", nargs='?', type=validate_directory_writable, help="Path to the directory to validate")
    args = parser.parse_args()

    if not args.directory:
        while True:
            directory = input("Enter the directory path to validate: ")
            try:
                validated_directory = validate_directory_writable(directory)
                break
            except argparse.ArgumentTypeError as e:
                print(e)
    else:
        validated_directory = args.directory

    print(f"Valid writable directory: {validated_directory}")

if __name__ == "__main__":
    main()
