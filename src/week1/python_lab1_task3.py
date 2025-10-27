"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""


def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    return len(text), len(text.split()), "python" in text.lower()


if __name__ == "__main__":
    text = input("Enter sentence: ")
    length, count, contains = analyze_sentence(text)
    print(
        f"Length of text: {length}, word count: {count}, whetger 'Python' appears in text: {contains}"
    )
    pass
