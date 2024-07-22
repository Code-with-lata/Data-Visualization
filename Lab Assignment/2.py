def count_and_display_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f"Total number of words in '{filename}': {len(words)}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


filename = "anudip.txt"
count_and_display_words(filename)
