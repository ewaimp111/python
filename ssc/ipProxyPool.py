#!/usr/bin/python
# -*- coding: utf-8 -*-


import threading
import time
import random
import requests
import datetime
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor,as_completed
import net_init_
import sys,os


targeturl = 'http://www.baidu.com'
proxy_ip_list =[]
ip_path = 'ip.txt'

"""
1、抓取西刺代理网站的代理ip
2、并根据指定的目标url,对抓取到ip的有效性进行验证
3、最后存到指定的path
"""

# ------------------------------------------------------文档处理--------------------------------------------------------
# 写入文档
def write(path,data = []):
    with open(path,'a') as f:
        for l in data:
            print(l)
            f.writelines(l)
            f.write('\n')
# 清空文档
def clear(path):
    with open(path, 'w') as f:
        f.truncate()
# 读取文档
def read(path):
    with open(path, 'r') as f:
        txt = []
        for s in f.readlines():
            txt.append(s.strip())
    return txt
# ----------------------------------------------------------------------------------------------------------------------
# 计算时间差,格式: 时分秒
def __gettimediff(start,end):
    seconds = (end - start).seconds
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff
# ----------------------------------------------------------------------------------------------------------------------
# 返回一个随机的请求头 headers

# -----------------------------------------------------检查ip是否可用----------------------------------------------------
def checkip(ip):
    headers =net_init_.getheaders()  # 定制请求头
    proxies = {"http": "http://"+ip, "https": "http://"+ip}  # 代理ip
    #print(proxies['http'])
    #print(proxies['https']) #http://119.10.67.144:808
    try:
        #time.sleep(3)
        response=requests.get(url=targeturl,proxies=proxies,headers=headers,timeout=15).status_code
        if response == 200 :
            return ''
        else:
            return ip
    except:
        return ip


#-------------------------------------------------------获取代理方法----------------------------------------------------
# 免费代理 XiciDaili
x = 0
def findip(type,pagenum): # ip类型,页码,目标url,存放ip的路径
    list={'1': 'http://www.xicidaili.com/nt/', # xicidaili国内普通代理
          '2': 'http://www.xicidaili.com/nn/', # xicidaili国内高匿代理
          '3': 'http://www.xicidaili.com/wn/', # xicidaili国内https代理
          '4': 'http://www.xicidaili.com/wt/'} # xicidaili国外http代理
    url=list[str(type)]+str(pagenum) # 配置url
    headers = net_init_.getheaders() # 定制请求头
    html=requests.get(url=url,headers=headers,timeout = 5).text
    soup=BeautifulSoup(html,'lxml')
    all=soup.find_all('tr',class_='odd')

    for i in all:
        t=i.find_all('td')
        ip=t[1].text+':'+t[2].text
        addr = '地  址  : '+ t[3].text
        typ  = '类  型  : '+t[4].text
        https ='h t t p : '+t[5].text
        able  ='有效期  : '+t[8].text
        td  =  '时  间  : '+t[9].text

        is_avail = checkip(ip)
        if is_avail != '':

            write(path =ip_path,text = ip)
            print('-------正在爬取第{}个--------'.format(x))
            print(ip)
            print(''.join( addr.split('\n')))
            print(typ)
            print(https)
            print(able)
            print(td)

# -----------------------------------------------------测试ip是否可用----------------------------------------------------
def testip(ip):
    headers =net_init_.getheaders()  # 定制请求头
    proxies = {"http": "http://"+ip, "https": "https://"+ip}  # 代理ip
    # print(proxies['http'])
    # print(proxies['https']) #http://119.10.67.144:808
    try :
        #time.sleep(3)
        response=requests.get(url=targeturl,proxies=proxies,headers=headers,timeout=15)
        response.encoding ='utf-8'
        if response.status_code == 200 :
            print(response.text)
        else:
            print('测试ip失败，ip地址不可用--')
    except Exception as E:
        print('语法错误：',E)
#-----------------------------------------------------多线程抓取ip入口---------------------------------------------------
def getNetProxyIpList():
     os.remove('ip.txt') # 爬取前清空文档
     print('删除代理池ip文件，从网络从新获取。。。')
     start = datetime.datetime.now() # 开始时间
     threads=[]
     for type in range(4):   # 四种类型ip,每种类型取前三页,共12条线程
         time.sleep(random.randint(3,10))
         for pagenum in range(1):  #获取页数
             t = threading.Thread(target=findip,args=(type+1,pagenum+1,path))
             threads.append(t)
     print('开始爬取代理ip')
     for s in threads: # 开启多线程爬取
         s.start()

     for e in threads: # 等待所有线程结束
         e.join()
     print('爬取完成')
     end = datetime.datetime.now() # 结束时间
     diff = __gettimediff(start, end)  # 计算耗时
     ips = read(ip_path)  # 读取爬到的ip数量
     print('一共爬取代理ip: %s 个,共耗时: %s \n' % (len(ips), diff))
     write(ip_path,ips)
     return ips


# 过滤无效代理ip
def filterProxyIpList(threadcount = 5):
    global proxy_ip_list
    proxy_ip_list = read(ip_path)
    print('----代理池IP地址共计：' , len(proxy_ip_list) , ' 个')
    print(proxy_ip_list)
    all_task = []

    pool = ThreadPoolExecutor(threadcount)
    all_task =[pool.submit(checkip,ip) for ip in proxy_ip_list ]
    for t in as_completed(all_task):
        r = t.result()
        if r != '':
            print(r,' 地址已失效')
            proxy_ip_list.pop(proxy_ip_list.index(r))
        else:
            print('可用')
    #删除IP。txt文件
    os.remove('ip.txt')
    time.sleep(1)
    #重新写入新的可用ip地址
    write('ip.txt',proxy_ip_list)
    time.sleep(1)
    print('----代理池可用IP地址 ：' , len(proxy_ip_list) , ' 个')
    print(proxy_ip_list)

#-------------------------------------------------------调用-----------------------------------------------------------

# 定时执行更新可用代理IP地址
def timerFilterProxyIpList(intvaltime = 5 ,intvalcount= 10):
    for i in range(intvalcount):
        print('当前执行第 {} 次,总执行次数 {} 次'.format(i+1,intvalcount))
        s = intvaltime
        for j in range(intvaltime):
            s -= 1
            time.sleep(1)
            sys.stdout.write('\r  剩余执行时间 {}'.format(s))
        sys.stdout.flush()
        print()

        #过滤不可用的代理ip地址
        filterProxyIpList(5)

        # 代理池少于2个地址从新获取
        if len(proxy_ip_list) <= 2 :
            # 从网络获取代理ip列表
            getNetProxyIpList('ip.txt')




#获取可用代理池IP列表
def getProxyIpList():
    l = []
    with open(ip_path , 'r') as f :
        for line in f.readlines() :
            l.append(line.strip())
        return l

#获取随机可用代理ip地址
def getProxyIp():
    _proxylist = getProxyIpList()

    print('------可用ip列表------')
    print(_proxylist)
    for _ip in _proxylist:
        if checkip(_ip) == str('') :
            #print('___ ' + _ip)
            return  _ip
            break
        else:
            continue


if __name__ == '__main__':
    timerFilterProxyIpList(intvaltime=10, intvalcount=50)

    # ip = getProxyIp()
    # print('获取的随机代理ip：' , ip)
    # testip(ip)
