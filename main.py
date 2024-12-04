def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    # print(text)
    unique_char = char_count(text)
    print(unique_char)

    count = word_count(text)
    print(count)
    print_report(text)


def print_report(text):
    no_char = char_count(text)
    print(f"--Begin report on frankenstein.txt")
    words = word_count(text)
    print(f"{words} words found in the document ")
    for char in no_char:
        print(f"The '{char}' character was found {no_char[char]} times")
    print("--End report--")



def char_count(string):
    lower_char = string.lower()
    char_dict = {}

    for char in lower_char:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

    


def get_text(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    count = 0

    for word in text.split():
        count += 1
    return count




main()