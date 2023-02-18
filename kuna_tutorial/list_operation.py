def maxValue(number):
    maxNum = number[0]
    for index in range(len(number)):
        if maxNum < number[index]:
            maxNum = number[index]
    return maxNum


def minValue(number):
    minNum = number[0]
    for index in range(len(number)):
        if minNum > number[index]:
            minNum = number[index]
    return minNum


def reverse_list(number):
    for i in range(len(number)):
        for j in range(len(number)):
            if number[i] < number[j]:
                temp = number[i]
                number[i] = number[j]
                number[j] = temp
    return number


if __name__ == '__main__':
    numbers = [32, 5, 7, 8, 3, 17, 6]
    num = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    print(f"{maxValue(numbers)} is the maximum number")
    print(f"{minValue(numbers)} is the minimum number")
    print(reverse_list(num))
