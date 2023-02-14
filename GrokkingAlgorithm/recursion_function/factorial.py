def factorial(number):
    if number == 1:
        # base case
        return 1
    else:
        # recursive case
        return number * factorial(number - 1)


if __name__ == '__main__':
    user = int(input("enter a number to find the factorial: "))
    print("The Factoria of %d is: %d" % (user, factorial(user)))