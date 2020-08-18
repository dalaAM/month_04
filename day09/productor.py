import redis

r =redis.Redis(host='127.0.0.1',port=6379,db=0)
# key_list =r.keys('*')
# print(key_list)

task ='%s_%s_%s_%s'%('sendMail','123@tedu.com','456@tedu.com','hello.world')
r.lpush('pylist1',task)
