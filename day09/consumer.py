import redis

r =redis.Redis(host='127.0.0.1',port='6379',db=0)
while True:
    task = r.brpop('pylist1','3')
    print(task)
    if task:
        task_data =task[1]
        task_str = task_data.decode()
        print(task_str)
        # task_list =task_str.slict('_')
        print('可以接收数据')
    else:
        print('没有接收数据')
