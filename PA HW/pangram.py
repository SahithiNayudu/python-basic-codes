import string
sentence = input("Enter a sentence: ").lower()
if all(letter in sentence for letter in string.ascii_lowercase):
    print("It is a pangram")
else:
    print("It is not a pangram")
