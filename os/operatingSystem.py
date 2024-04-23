import sys
import os
import psutil
import socket


# Function to retrieve and print memory information
def print_memory_info():
    mem_info = psutil.virtual_memory()
    print("Memory Information:")
    print("Total Memory:", mem_info.total)
    print("Available Memory:", mem_info.available)
    print("Used Memory:", mem_info.used)
    print("Free Memory:", mem_info.free)
    print()


# Function to determine disk usage of the current directory
def print_disk_usage():
    disk_usage = psutil.disk_usage(os.getcwd())
    print("Disk Usage:")
    print("Total Disk Space:", disk_usage.total)
    print("Used Disk Space:", disk_usage.used)
    print("Free Disk Space:", disk_usage.free)
    print()


# Function to provide detailed information about specific files in the directory
def print_file_info(directory="."):
    print("File Information:")
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_stat = os.stat(file_path)
            print("File:", file)
            print("Size:", file_stat.st_size, "bytes")
            print("Permissions:", oct(file_stat.st_mode)[-3:])
            print("Creation Time:", file_stat.st_ctime)
            print("Modification Time:", file_stat.st_mtime)
            print()


# Function to retrieve and print process information
def print_process_info():
    print("Process Information:")
    for proc in psutil.process_iter():
        try:
            process_info = proc.as_dict(attrs=['pid', 'name', 'cpu_percent', 'memory_percent'])
            print("PID:", process_info['pid'])
            print("Name:", process_info['name'])
            print("CPU Percent:", process_info['cpu_percent'])
            print("Memory Percent:", process_info['memory_percent'])
            print()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


# Function to obtain network information
def print_network_info():
    print("Network Information:")
    print("Hostname:", socket.gethostname())
    print("IP Address:", socket.gethostbyname(socket.gethostname()))
    print("Network Interfaces:")
    for interface, addrs in psutil.net_if_addrs().items():
        print(f"- {interface}:")
        for addr in addrs:
            print(f"  - {addr}")
    print()


# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. Print Memory Information")
        print("2. Print Disk Usage")
        print("3. Print File Information")
        print("4. Print Process Information")
        print("5. Print Network Information")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print_memory_info()
        elif choice == '2':
            print_disk_usage()
        elif choice == '3':
            print_file_info()
        elif choice == '4':
            print_process_info()
        elif choice == '5':
            print_network_info()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

