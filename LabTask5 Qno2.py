sentence = input("Enter a sentence: ")

characters = len(sentence)
words = len(sentence.split())
vowels = 0
spaces = 0
digits = 0

for char in sentence:
    if char.lower() in "aeiou":
        vowels += 1

    if char == " ":
        spaces += 1

    if char.isdigit():
        digits += 1

print("\nNumber of characters:", characters)
print("Number of words:", words)
print("Number of vowels:", vowels)
print("Number of spaces:", spaces)
print("Number of digits:", digits)