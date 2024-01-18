if __name__ == '__main__':

    answer = 0
    while True:
        operator = input("Enter operator:: ")
        operator.strip()
        num1 = int(input("Enter first num:: "))
        num2 = int(input("Enter second num:: "))
        if operator == '+' or '-' or '//' or '*' or '%':
            if operator == '+':
                answer = num1 + num2
            if operator == '-':
                answer = num1 - num2
            if operator == '*':
                answer = num1 * num2
            if operator == '//':
                if num2 != 0:
                    answer = num1 // num2
            if operator == '%':
                answer = num1 % num2
        elif operator == 'x' or 'X':
            break
        else:
            print("invalid operator!")
    print(f'The anser ::{ answer}')



