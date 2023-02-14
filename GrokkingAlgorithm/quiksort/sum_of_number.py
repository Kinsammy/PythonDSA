def arr_sum(user_input):
    total = 0
    for index in user_input:
        total += index
    return total


if __name__ == '__main__':
    print("The total of the array is: %d" % arr_sum([1, 2, 3, 4, 5]))
