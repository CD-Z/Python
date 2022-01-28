import redis

r = redis.StrictRedis(host='10.115.2.20', port=6379, db=0, charset='utf-8', decode_responses=True)

for counter in range(1000000):
    r.set(f"key-{counter}", f"automated inserted value (key-{counter})")