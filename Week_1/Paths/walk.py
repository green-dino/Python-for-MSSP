import os
import hashlib

def hash_file(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)  # Read in 64k chunks
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def walk_path(root_dir):
    """
    Traverse a directory tree and hash each file encountered.
    """
    file_count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = hash_file(file_path)
                print(f"File: {file_path}, Hash: {file_hash}")
                file_count += 1
            except Exception as e:
                print(f"Error hashing file {file_path}: {e}")
    return file_count

def main():
    root_dir = input("Enter the root directory path: ")
    if os.path.isdir(root_dir):
        num_files_processed = walk_path(root_dir)
        print(f"Total files processed: {num_files_processed}")
    else:
        print("Invalid directory path.")

if __name__ == "__main__":
    main()
