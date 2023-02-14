def find_smallest(numbers):
    smallest = numbers[0]
    smallest_index = 0
    for index in range(1, len(numbers)):
        if numbers[index] < smallest:
            smallest = numbers[index]
            smallest_index = index
    return smallest_index



def selection_sort(numbers):
    new_number = []
    for index in range(len(numbers)):
        smallest = find_smallest(numbers)
        new_number.append(numbers.pop(smallest))
    return new_number


if __name__ == '__main__':
    user_input = [5, 3, 6, 2, 10]
    print(selection_sort(user_input))
