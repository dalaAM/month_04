
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
r.zadd('z11',{'liwei':300,'lanlele':100,'sunzhiguo':550,'zhanghan':600})
print(r.zrange('z11', 0, -1, withscores=True))
print(r.zrevrange('z11', 0, -1, withscores=True))
print(r.zcard('z11'))
r.zadd('z12',{'liwei':200})
print(r.zinterstore('z23', 2, 'z12', 'z11'))






