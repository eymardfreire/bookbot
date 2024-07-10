def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  # Convert to lowercase
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def generate_report(word_count, char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_chars:
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

with open('books/frankenstein.txt', 'r') as file:
    contents = file.read()
    print(contents)

word_count = count_words(contents)
char_count = count_characters(contents)
generate_report(word_count, char_count)
