# 同时对一个账户进行操作,当天余额*2
from time import sleep

import redis

poor =redis.ConnectionPool(host='127.0.0.1',port ='6379',db=1) #建立连接池
r =redis.Redis(connection_pool=poor)


def double_count(user_id):
    key ='account_%s'%user_id
    with r.pipeline(transaction=True) as pipe:
        while True:#如果redis中执行事物的键被修改了,就不执行,(希望我的事物一定要被执行),
            try:#在python中,如果事物不执行,会报异常
                pipe.watch(key)#监控键key的值是否发生改变
                value =int(r.get(key))#获取键的值
                value *= 2
                print('new value is %s'%value)
                print('sheep is start')
                sleep(20)
                print('sheep is end')
                pipe.multi()#开始事物
                pipe.get(key,value)
                pipe.execute()#执行事物
                break
            except redis.WatchError as e:
                print('value changed')
                continue
        return int(r.get(key))


if __name__ == '__main__':
    print(double_count('tesu'))



