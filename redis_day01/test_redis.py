import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
# 列车0库中所有的键
key_list = r.keys('*')
print(key_list)
# 通用命令
print(r.exists('l1'))
print(r.exists('l5'))
# 字符串类型
r.set('name1','mazhguo',100)
print(r.get('name1'))
# 列表类型
r.lpush('pyl1','a','b','c','d')
print(r.lrange('pyl1', 0, -1))
r.ltrim('pyl1',0,1)
print(r.lrange('pyl1', 0, -1))
r.rpop('pyl1')
print(r.lrange('pyl1', 0, -1))
