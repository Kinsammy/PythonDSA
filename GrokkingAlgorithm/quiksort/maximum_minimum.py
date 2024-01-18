def max_value(user_input):
    max_number = user_input[0]
    for index in user_input:
        if index > max_number:
            max_number = index
    return max_number


def min_value(user_input):
    min_number = user_input[0]
    for index in user_input:
        if index < min_number:
            min_number = index
    return min_number


if __name__ == '__main__':
    print("The maximum number is %d" % max_value([1, 3, 6, 9, 5]))
    print("The minimum number is %d" % min_value([3, 1, 6, 9, 5]))
