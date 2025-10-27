"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""


def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.strip())


def count_words(text):
    """Count number of words in a string."""
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for v in text.split():
        if v.isdigit():
            numbers.append(int(v))
    return numbers


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    sum, avg = 0, 0
    numbers = extract_numbers(text)
    for v in numbers:
        sum += v
    avg = sum / len(numbers)
    return count_characters(text), count_words(text), sum, avg


if __name__ == "__main__":
    text = input("Enter sentence: ")
    count_char, count_word, sum, avg = analyze_text(text)
    print(
        f"Character count: {count_char}, word count: {count_word}, sum of integers: {sum}, average of integers: {avg}"
    )
    pass
