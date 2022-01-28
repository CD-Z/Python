from datetime import datetime
import time
import random

import redis

r = redis.StrictRedis(host='10.115.2.20', port=6379, db=0, charset='utf-8', decode_responses=True)


def read_random(num):
    start_time = time.time()
    start_process_time = time.process_time()
    for i in range(num):
        number = random.randint(0, 1000000)
        r.get(f"key-{number}")
    print(f"It took {time.time()-start_time}s and the Process time took {(time.process_time()-start_process_time) * 1000}ms to read {num} keyvalues")


read_random(10)
read_random(100)
read_random(1000)
read_random(10000)
read_random(100000)

