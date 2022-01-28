import redis


def get_fibonacci(number):
    fibonacci = [0, 1]
    for x in range(2, number + 1):
        fibonacci = fibonacci + [fibonacci[x - 2] + fibonacci[x - 1]]
    return fibonacci[number]


r = redis.StrictRedis(host='10.115.2.20', port=6379, db=0, charset='utf-8', decode_responses=True)
wanted_num = int(input("Enter the index of a Fibonacci number:"))
print(get_fibonacci(wanted_num))

for i in range(wanted_num + 1):
    r.set(f"f-{i}", get_fibonacci(i))
