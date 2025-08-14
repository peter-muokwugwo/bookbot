# 📚 BookBot

BookBot is a simple Python program that analyzes text files (like classic books) and provides a report on the word count and character frequency.

## 🚀 Features
- Reads a `.txt` file.
- Counts the total number of words.
- Counts the occurrences of each character (case-insensitive).
- Generates a simple, human-readable report.

## 📂 Project Structure
```
bookbot/
│
|
│── frankenstein.txt      # Sample text file
│
└── main.py                   # Main program logic
```

## 🛠 How It Works
1. **Read the file** – The program loads the text file 
2. **Word count** – It counts the total number of words.
3. **Character frequency** – It counts how many times each character appears.
4. **Report** – Prints the results to the console.

Example of generated report:
```
--Begin report on frankenstein.txt
77986 words found in the document
The 'a' character was found 48622 times
The 'b' character was found 9132 times
...
--End report--
```

## 📜 Code Overview
- `main()` – The entry point that runs the analysis.
- `get_text(path)` – Reads and returns file contents.
- `word_count(text)` – Counts the words in the text.
- `char_count(string)` – Counts occurrences of each character (lowercased).
- `print_report(text)` – Generates and prints the summary report.

## ▶️ Usage
1. Place your `.txt` file inside the `books` folder.
2. Update the `path` variable in `main()` to point to your file.
3. Run the program:
```bash
python main.py
```

## 📌 Requirements
- Python 3.6+
- A `.txt` file to analyze (UTF-8 encoded)

## 📝 Notes
- Character counting includes spaces, punctuation, and special characters.
- Reports are printed directly to the terminal.

---
