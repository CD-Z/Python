import redis

r = redis.StrictRedis(host='10.115.2.20', port=6379, db=0, charset='utf-8', decode_responses=True)

r.set('key-001', 'Python ist einfach zu erlernen.')
r.set('key-002', 'Python ermöglicht schnelles entwickeln')

print(r.get('key-001'))
