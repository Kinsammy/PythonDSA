def digit_count(number):
    count = 0
    while number > 0:
        rem = number % 10
        if rem == 5:
            count += 1
        number //= 10
    print(count)


if __name__ == '__main__':
    num = 1255765
    digit_count(num)
