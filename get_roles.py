from redis.sentinel import Sentinel
sentinel = Sentinel([('redis-cluster', 26379)], socket_timeout=0.1)
print("Master on {} ".format(sentinel.discover_master('mymaster')))
slaves = sentinel.discover_slaves('mymaster')
print("Slave on:")
for slave in slaves:
    print(slave)
