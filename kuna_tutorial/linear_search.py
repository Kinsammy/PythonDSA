def search(numbers, element):
    for index in range(len(numbers)):
        if numbers[index] == element:
            return "Seen"
        else:
            return


if __name__ == '__main__':
    nums = [18, 19, 14, 17, 18]
    print(search(nums, 14))
