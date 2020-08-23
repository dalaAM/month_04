import redis
import time

pool = redis.ConnectionPool(host='127.0.0.1', db=1, port=6379, password='123456')
r = redis.Redis(connection_pool=pool)


def double_count(user_id):
    key = 'account_%s' % (user_id)
    with r.pipeline(transaction=True) as pipe:
        while True:
            try:
                # 监控键key的值是否发生改变
                pipe.watch(key)
                # 获取key的值×2，输出
                value = int(r.get(key))
                value *= 2
                print('new value is %s' % value)
                # 为了给在 客户端修改key的值留点儿时间，sleep 20秒
                print('--sleep is start--')
                time.sleep(20)
                print('--sleep is over--')
                # 开始事务
                pipe.multi()
                pipe.set(key, value)
                # 执行事务
                pipe.execute()
                break
            except redis.WatchError:
                print('value changed')
                continue
    return int(r.get(key))


if __name__ == '__main__':
    print(double_count('tedu'))
