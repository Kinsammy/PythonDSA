import math


def is_armstrong(number):
    original_number = number
    new_number = 0
    while number > 0:
        rem = number % 10
        cube_of_number = math.pow(rem, 3)
        new_number += cube_of_number
        number //= 10
    if new_number == original_number:
        return True


if __name__ == '__main__':
    num = int(input("Enter a number to know if is armstrong or not:: "))
    print(is_armstrong(num))
    # Todo To know all the armstrong number from 100 to 1000
    # for numbers in range(100, 1000):
    #     if is_armstrong(numbers):
    #         print(numbers)
    #
    #
