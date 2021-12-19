# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from functools import reduce


# Press the green button in the gutter to run the script.
def is_prime(num):
    if num > 1:
        for e in range(2, int(num / 2) + 1):
            if (num % e) == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    numbers = range(98)

    numbers = list(map(lambda x: x + 2, numbers))
    i = 0
    while i < len(numbers):
        z = numbers[i]
        numbers = list(filter(lambda x: x % numbers[i] != 0, numbers))
        i += 1
        numbers.append(z)
        numbers.sort()

    print(numbers)

    numbers = range(100000)
    numbers_prime = list(filter(is_prime, numbers))
    sum_of_primes = reduce(lambda x, y: x + y, numbers_prime)
    print(sum_of_primes)

