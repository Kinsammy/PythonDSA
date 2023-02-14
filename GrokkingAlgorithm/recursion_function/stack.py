def greet2(name):
    print("How are you , " + name + "?")


def bye():
    print("Ok bye!")


def greet(name):
    print("Hello, " + name + "!")
    greet2(name)
    print("Getting rady to say goo bye...")
    bye()


if __name__ == '__main__':
    user = input("Enter your name: ")
    print(greet(user))


