def main():
    frankenstein_path = "books/frankenstein.txt"
    book_text = get_book_text(frankenstein_path)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_char_counts = sort_by_counts(char_counts)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for char_dict in sorted_char_counts:
        print(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times")



def count_words(text):
    list = text.split()
    return len(list)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(string):
    string = string.lower()
    letters = set(string)
    count_list = []

    for letter in letters:
        if letter.isalpha():
            count_list.append({"char": letter, "count": string.count(letter)})
    
    return count_list
    

def sort_on(dict):
    return dict["count"]

def sort_by_counts(count_list):
    count_list.sort(reverse = True, key=sort_on)
    return count_list



main()
