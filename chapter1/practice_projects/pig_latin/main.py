"""Pig latin generator"""
import re

def main():
    """Main function to convert user provided input to pig latin"""

    consonant_append = "ay"
    vowel_append = "way"

    print("Let's write some pig latin!\n")

    user_word = input("Please provide a word or sentence:\n\n")

    if re.match("[^aeiou]", user_word):
        print(f"{user_word[1:]}{user_word[:1]}{consonant_append}")
    else:
        print(f"{user_word}{vowel_append}")


if __name__ == "__main__":
    main()
