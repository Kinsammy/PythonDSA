import math


def even_digit_count(digit):
    counter = 0
    while digit > 0:
        counter += 1
        digit //= 10
    return counter


def findEven(elements):
    count = 0
    for index in range(0, len(elements)):
        even = even_digit_count(elements[index])
        if even % 2 == 0:
            count += 1
    return count


if __name__ == '__main__':
    numbers = [12, 345, 2, 6, 7896]
    print(findEven(numbers))
