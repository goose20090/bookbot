def main():
    frankenstein_path = "books/frankenstein.txt"
    book_text = get_book_text(frankenstein_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    print(book_text)
    print(word_count)
    print(char_count)


def count_words(text):
    list = text.split()
    return len(list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(string):
    string = string.lower()
    letters = set(string)
    count_dict = {}

    for letter in letters:
        count_dict[letter] = string.count(letter)
    
    return count_dict

main()
