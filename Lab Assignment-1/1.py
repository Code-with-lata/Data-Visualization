# Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen

def read_and_display(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = "anudip.txt"
read_and_display(filename)
