import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0)
rask1 = r.hset('h1','sex','m')
rask2 = r.hmset('h2',{'uname':'liwei','age':18,'sex':'m'})
print(r.hgetall('h1'))
print(r.hgetall('h2'))

