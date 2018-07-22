#!/usr/bin/env python3
# -*- coding: gb2312 -*-

import random
import time
import sys
import threading

import requests

from sendmail import sendMail
import net_init_
import ipProxyPool

'''
��ipurl�ֵ��е���ҳ��ȡIP��ַ
������getNetIp() ��ȡ����url��ip
������getAll_NetIp() ��ȡ�����б���url�е�ip
������getNetIp_timer(count=5,times=60) ��ʱ��ȡȫ���ֵ��е�URL��ip
'''

# ��ѯ����ip����վ��ַ
# curl ipinfo.io/ip
# curl ipecho.net/plain
# curl http://icanhazip.com/

# ip�ֵ�

IPURL = {'1' : 'http://ipinfo.io/ip' , '2' : 'http://ipecho.net/plain' , '3' : 'http://icanhazip.com/'}


# ����һ�����������ͷ headers


def get_NetIp(urls , proxyip='') :
	headers = net_init_.getheaders()  # ��������ͷ
	# proxies = {"http": "http://"+ip, "https": "http://"+ip}  # ����ip
	proxies = {"http" : 'http://' + proxyip , 'https' : 'http://' + proxyip}  # ����ip
	try :
		if proxyip == '' :  # ���û��ʹ�ô���IP
			response = requests.get(url=urls , headers=headers , timeout=30)
		else :
			response = requests.get(url=urls , headers=headers , proxies=proxies , timeout=30)

		if response.status_code == 200 :
			s = response.text.strip().rstrip().lstrip()
			return s
		else :
			s = '��ȡIPʧ��!'
			print(s)
			return s
	except Exception as e :
		s = 'ip�������'
		print(s)
		return ''


ipdata = {}


def getAll_NetIp(proxyip ='') :
	for _url in IPURL.values() :
		if proxyip == '' :
			_ip = get_NetIp(_url)
		else :
			_ip = get_NetIp(_url , proxyip)
		print('�����ַ:' , proxyip)
		print('��ȡ��ַ��' , _url)
		print('ip�� ַ��' , _ip)
		ipdata.setdefault(_url , _ip)


def getNetIp_timer(count , times , proxyip='') :
	c = 0
	while c < count :
		c += 1
		print('\r��ʱ��ȡ����ip��ַ����� %d �� ��ִ�д���: %d' % (c , count))
		t = times
		while t > 0 :
			sys.stdout.write('\rʣ��ִ��ʱ�䣺%d' % (t))
			t -= 1
			time.sleep(1)
			if t <= 0 :
				break
		sys.stdout.flush()
		print('')
		if proxyip == '' :  # ���û��ʹ�ô���IP
			t = threading.Thread(target=getAll_NetIp)
		else :
			t = threading.Thread(target=getAll_NetIp , args=(proxyip ,))
		t.start()
		t.join()
		print('-' * 50)
		data = str(ipdata)  # sendMail('home ipaddress',data)


# print(get_NetIp(IPURL['3'],'221.7.255.168:8080')) #ʹ�ô���ipȥ��ȡ
# print(get_NetIp(IPURL['3']))  #��ʹ�ô���
# getAll_NetIp(proxyip='221.7.255.168:8080')
# sendMail('home ipaddress',data)


getNetIp_timer(count=5 , times=60 )

1,ipPut
2,getLanAddr
3,getWanAddr




# --------------------------------------------------
# proxyip_list = []
# proxyip_list = proxy_ip_pool.getProxyIp('ip.txt')
# print(proxyip_list)
# getNetIp_timer(count=5 , times=60 , proxyip=random.choice(proxyip_list))
