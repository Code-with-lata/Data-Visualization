# Write a Python program that opens a file and handle FileNotFoundError exception if file does not exist.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

# Example usage
file_path = 'example.txt'
read_file(file_path)
