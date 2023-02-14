def reverse(number):
    reverse_num = 0
    while number > 0:
        rem = number % 10
        number //=10
        reverse_num = reverse_num * 10 + rem
    print(reverse_num)


if __name__ == '__main__':
    num = 654321
    reverse(num)
