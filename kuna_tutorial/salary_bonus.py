if __name__ == '__main__':

    salary = int(input("Enter salary: "))

    if salary > 10000:
        salary += 2000
    else:
        salary += 1000

    print(f"Your new salary is {salary}")
