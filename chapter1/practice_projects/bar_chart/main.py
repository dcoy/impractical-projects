"""Poor Man's Bar Chart"""
import sys
import pprint
from collections import defaultdict

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
TEXT = sys.argv[1]

def main():
    """Compare common letters in a sentence
       with common letters in a dict, return
       bar chart."""
    mapped_chars = defaultdict(list)

    for char in TEXT:
        char = char.lower()
        if char in ALPHABET:
            mapped_chars[char].append(char)

    print(f"Here's your text: {TEXT}:")
    pprint.pprint(mapped_chars, width=110)

if __name__ == "__main__":
    main()
