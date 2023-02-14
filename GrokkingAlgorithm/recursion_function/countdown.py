def countdown(number):
    print(number)
    if number <= 0:
        # base case
        return
    else:
        # recursive case
        countdown(number - 1)


if __name__ == '__main__':
    user_input = int(input("Enter a number to count down: "))
    print(countdown(user_input))