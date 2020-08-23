import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
r.hset('h2', 'uname', 'tedu')

# b'tedu'
print(r.hget('h2', 'uname'))
# 设置多个字段值时，第二个参数是一个字典
r.hmset('h2',{'age':22,'desc':'it edu'})
# {b'uname': b'tedu', b'age': b'22', b'desc': b'it edu'}
print(r.hgetall('h2'))
print(r.hkeys('h2'))
print(r.hvals('h2'))