def main():
    frankenstein_path = "books/frankenstein.txt"
    book_text = get_book_text(frankenstein_path)
    word_count = count_words(book_text)
    print(book_text)
    print(word_count)


def count_words(text):
    list = text.split()
    return len(list)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
