string = input("Enter a string: ")
reversestring = string[::-1]
if string == reversestring:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
