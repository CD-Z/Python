def print_sum(num1, num2):
    sum_ = num1 + num2
    product = num1 * num2
    if product > 700:
        print(f'The result is {product}')
    else:
        print('The result is', sum_)


def print_sum_of_nums():
    print("")
    print(f"Printing current and previous number sum in a range(")
    num = str(input())
    print(")")
    if num.isnumeric():
        num = int(num)
        if num <= 0:
            print("Number must be above 0.")
        for i in range(0, num):
            if i == 0:
                print(f"Current Number {i} Previous Number {i} Sum: {i}")
            else:
                print(f"Current Number {i} Previous Number {i - 1} Sum: {i + i - 1}")
        print("Want to do it again?")
        answer = 0
        while answer == 0:
            text = input()
            if text.casefold() == "yes" or text.casefold() == "y":
                answer = 1
                print_sum_of_nums()
            elif text.casefold() == "no" or text.casefold() == "n":
                answer = 1
                print("Bye!")
            else:
                print("Only answer with Yes or No.")
    else:
        print(f"{num} is not a Number!")
        print("Input must be a number. Please try again.")
        print_sum_of_nums()


print_sum(40, 30)
print_sum_of_nums()