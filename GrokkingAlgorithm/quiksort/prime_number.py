if __name__ == '__main__':
    number = int(input("Enter a number: "))
    prime_counter = 2

    while prime_counter < number:
        if number % prime_counter == 0:
            print("It not a prime number!")
            break
        prime_counter += 1
    else:
        print("it a prime number!")
