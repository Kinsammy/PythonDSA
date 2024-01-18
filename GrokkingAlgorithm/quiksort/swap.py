def swap(user_list):
    for index in range(len(user_list)):
        for i in range(len(user_list)):
            if user_list[index] < user_list[i]:
                temp = user_list[index]
                user_list[index] = user_list[i]
                user_list[i] = temp
    return user_list


if __name__ == '__main__':
    print(swap([3, 6, 1]))
