from pathlib import Path
import string


def main():
    path = "frankenstein.txt"
    text = get_text(path)
    # print(text)
    unique_char = char_count(text)
    print(unique_char)

    count = word_count(text)
    print(count)
    print_report(text)


def char_count(string_data):
    lower_char = string_data.lower()
    char_dict = {}

    for char in lower_char:
        if char in char_dict:
            if char in string.ascii_lowercase:
                char_dict[char] += 1
        else:
            char_dict[char] = 1
    sorted_char_dict = dict(
        sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

    return sorted_char_dict


def get_text(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {path}")
        return ""


def word_count(text):
    return len(text.split())


def print_report(text, source_filename="document.txt", save_to_file=True):
    char_freq = char_count(text)
    words = word_count(text)

    report_lines = []
    report_lines.append(f"--Begin report on {source_filename}")
    report_lines.append(f"{words} was found in the document.")

    for char, count in char_freq.items():
        report_lines.append(f"The '{char}' character was found {count} times")

    report_lines.append("--End report--")

    for line in report_lines:
        print(line)

    if save_to_file:
        report_filename = f"report_{Path(source_filename).stem}.txt"
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))
        print(f"\nReport saved to '{report_filename}")


if __name__ == "__main__":
    main()
