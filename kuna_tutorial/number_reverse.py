def reverse(number):
    isNegative = False
    if number < 0:
        isNegative = True
        number *= -1
    reverse_num = 0
    while number > 0:
        rem = number % 10
        number //= 10
        reverse_num = reverse_num * 10 + rem
    if isNegative:
        reverse_num *= -1
    return reverse_num


if __name__ == '__main__':
    num = 1534236469
    print(reverse(num))
