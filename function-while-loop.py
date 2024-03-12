# Write a function digit() which lets the user input an integer in a variable named number. If number is even, then it should print the result of number/2. If number is odd, then digit() should print and return 3 * number + 1. The program should keep calling the function digit() on the number until it returns a 1.


def digit(number):
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            print(number, "If condition")
        else:
            number = number * 3 + 1
        print(number, "Else condition")

    return number

number = int(input("Enter a number: "))
digit(number)
