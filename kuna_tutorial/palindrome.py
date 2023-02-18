def palindrome_number(number):
    temp = number
    reverse_number = 0
    while number > 0:
        rem = number % 10
        reverse_number = reverse_number * 10 + rem
        number //= 10
    if reverse_number == temp:
        print(f"{reverse_number} is a palindrome number")
    else:
        print(f"{reverse_number} is not a palindrome number")


def palindrome_string(letter):
    string = letter
    new_letter = ""
    for char in range(len(letter)):
        new_letter += letter[char]
        print(new_letter)
    if new_letter == string:
        print(f"{new_letter} is a palindrome letter")
    else:
        print(f"{new_letter} is not a palindrome letter")


if __name__ == '__main__':
    num = int(input("Enter a number to know if is palindrome or not\n"))
    palindrome_number(num)

    name  = "madami"
    palindrome_string(name)
