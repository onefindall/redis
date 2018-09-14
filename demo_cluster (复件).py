from rediscluster import *

def main():
    try:
        # 构建所有的节点,redis会使用CRC16算法,将键和值写到某个节点上
        start_nodes = [
            {'host': '127.0.0.1', 'port': '7000'},
            {'host': '127.0.0.1', 'port': '7003'},
            {'host': '127.0.0.1', 'port': '7001'},

        ]

        # 构建StrictRedisCluster对象
        src = StrictRedisCluster(startup_nodes=start_nodes,decode_responses=True)
        # 设置键为name,值为itheima 的数据
        result =src.set('name','itheima')
        print(result)

        # 获取键为name
        name =src.get('name')
        print(name)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
