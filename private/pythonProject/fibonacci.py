def make_Input():
    try:
        num = int(input("Enter the index of a Fibonacci number:"))
    except:
        make_Input()
    if num < 0:
        num = 0
    return num

def getFibonacci(number):
    fibonacci = [0, 1]
    for x in range(2, number + 1):
        fibonacci = fibonacci + [fibonacci[x - 2] + fibonacci[x - 1]]
    return fibonacci[number]


print(getFibonacci(make_Input()))
