import time

import redis


pool = redis.ConnectionPool(host = '127.0.0.1',db=0,port=6379)
r = redis.Redis(connection_pool=pool)

def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i+1
        p.set(key, value)
    p.execute()

def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i+1
        r.set(key, value)

if __name__ == '__main__':
    t1 =time.time()
    withpipeline(r)
    t2 =time.time()
    print('withpipeline time is %s'%(t2 -t1))

    t3 = time.time()
    withoutpipeline(r)
    t4 = time.time()
    print('withoutpipe time is %s' % (t4 - t3))
