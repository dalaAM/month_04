import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')
task = '%s_%s_%s_%s' % ('sendMail', '123@tedu.cn', '456@tedu.cn', 'hello world')
r.lpush('pylist1',task)