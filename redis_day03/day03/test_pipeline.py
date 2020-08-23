import redis
import time

# 创建连接池并连接到redis
pool = redis.ConnectionPool(host='127.0.0.1', db=0, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)


def withpipeline(r):  #使用流水线，1000命令一次通信
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i + 1
        p.set(key, value)
    p.execute()


def withoutpipeline(r):# 不使用流水线，1000个命令1000次通信
    for i in range(1000):
        key = 'test2' + str(i)
        value = i + 1
        r.set(key, value)


if __name__ == '__main__':
    # 没有使用流水线的时间消耗：time is 0.1609489917755127
    # 使用流水线的时间消耗：   time is 0.01903533935546875
    t1 = time.time()
    #withoutpipeline(r)
    withpipeline(r)
    t2 = time.time()
    print('time is %s' % (t2 - t1))
