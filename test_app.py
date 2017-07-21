import redis
from redis.sentinel import Sentinel
from time import sleep

r_addr = 'redis-sentinel'
r_port = '26379'

def redis_connect(sentinel_addr, sentinel_port):

  sentinel = Sentinel([(sentinel_addr, sentinel_port)], socket_timeout=0.1)
  master_ip = sentinel.discover_master('mymaster')[0]
  master_port = sentinel.discover_master('mymaster')[1]

  print("Found master on {}:{} ".format(master_ip,master_port))

  slaves = sentinel.discover_slaves('mymaster')

  print("Found slaves on:")

  for slave in slaves:
      print("     {}:{}".format(slave[0],slave[1]))

  conn = redis.StrictRedis(host=master_ip, port=master_port, db=0)
  return conn


try:
  myconn = redis_connect(r_addr, r_port)
except:
  print("Cant connect first time!")
  exit()

rand = 0

while True:
  try:
    key, val = "key" + str(rand), "val" + str(rand)
    rand += 1
    print("Trying set \'{}\' key  with \'{}\' value".format(key, val))

    if (myconn.set(key, val)):
       print("done")
    else:
       print("try again!")
       myconn = redis_connect(r_addr, r_port)

  except:
    print("Failed, try again!")
    myconn = redis_connect(r_addr, r_port)
  sleep(1)
