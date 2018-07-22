#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor , as_completed
import time ,arrow
import ipProxyPool

print(ipProxyPool.getProxyIp())
print(ipProxyPool.getProxyIpList())



# exit(0)
#
# task_list =proxy_ip_pool.read('ip.txt')
# print(task_list)
#
# pool=ThreadPoolExecutor(max_workers=5)
# all_task =list()
#
#
#
# s = time.time()
# all_task =[ pool.submit(proxy_ip_pool.checkip,t) for t in task_list ]
# for x in as_completed(all_task):
# 	data = x.result()
# 	print('地址：',bool(data))
# e = s - time.time()
# print('总用时：',e)


# s = time.time()
# for t in pool.map(proxy_ip_pool.checkip,task_list):
# 	print(t)
# e = s - time.time()
# print('总用时：',e)


# thread_list = ['a','b','c','d','e','f']
#
#
# #------------map---------
# print('---------map--------')
# t = time.time()
# future =  pool.map(task,thread_list)
# for f in future:
#     print('执行结果',f)
#     time.sleep(0.1)
# e = time.time()  - t
# print(e)
#
# #----------submit--------
# print('--------submit--------')
# t = time.time()
# future = pool.submit(task,thread_list)
# for f in future.result():
#     print('执行结果',f)
#     time.sleep(0.1)
# e = time.time() - t
# print(future.result() )
# print(e)