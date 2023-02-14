def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return nums


if __name__ == '__main__':
    numbers = [5, 9, 7, 8, 4]
    print(two_sum(numbers, 9))
