from functools import reduce

import redis


def make_input():
    num = 0
    try:
        num = int(input("Enter a number to get a factorial: "))
    except:
        make_input()
    if num < 0:
        print("Error: Ungültige Zahl")
        make_input()
    return num


def get_factorial(num):
    factorial = range(1, num + 1)
    if num == 0:
        return 1
    return reduce(lambda x, y: x * y, factorial)


def write_factorial():
    num = make_input()
    print(f"calculated result for number {num} = {get_factorial(num)}")


write_factorial()

# Second Part

r = redis.StrictRedis(host='10.115.2.20', port=6379, db=0, charset='utf-8', decode_responses=True)

for i in range(1, 21):
    r.set(f"fac-{i} ", get_factorial(i))

for i in range(1, 11):
    print(f"get fac-{i} from Redis: " + r.get(f"fac-{i} "))
print(f"get fac-20 from Redis: " + r.get(f"fac-20 "))
