#!/usr/bin/env python3
# -*- coding: gb2312 -*-
import smtplib
from email.header import Header  # ���������ʼ�ͷ���ʼ�����
from email.mime.text import MIMEText  # ��������ֻ�������ı����ʼ�������MIMEText����
import time
import random


receiver='ewaimp@icloud.com'
config1 = dict(server='smtp.qq.com',sender = '877135818@qq.com',receiver = receiver,
              username = '877135818@qq.com',password ='fibpzqlinfvfbcgb')
config2 = dict(server='smtp.qq.com',sender = 'ewaimp@21cn.com',receiver = receiver,
              username = 'ewaimp@qq.com',password ='mxxbajinemqtbegd')
config3 = dict(server='smtp.126.com',sender = 'ewaimp@126.com',receiver = receiver,
              username = 'ewaimp@126.com',password ='Sg0211589')

config_dict =[]
config_dict.append(config1)
config_dict.append(config2)
config_dict.append(config3)
random.random

#���ѡ��һ����������
config = random.choice(config_dict)

#config = config_dict[1]

# ��ʹ�õ����������ʼ���SMTP������
smtpServer=config['server']

# ������
sender = config['sender']

# ������
receiver = config['receiver']

# ����������û�������Ȩ�루���ǵ�¼��������룩
username=config['username']
password=config['password']

# print(config_dict[2])
# exit(0)

# ����һ��ʵ��
def sendMail(mail_title,mail_body):
    print('���ڹ����ʼ�������Ϣ....')
    message=MIMEText(mail_body,'plain','utf-8')  # �ʼ�����
    message['From']=sender  # �ʼ�����ʾ�ķ�����
    message['To'] = receiver # �ʼ�����ʾ���ռ���
    message['Subject']=Header(mail_title,'utf-8')  # �ʼ�����
    print('�ʼ������������.')
    try:

        smtp=smtplib.SMTP()  # ����һ������
        print('��������'+config['server']+'....')
        time.sleep(random.randint(1,5))
        smtp.connect(smtpServer)  # ���ӷ����ʼ��ķ�����
        print('������ɣ����ڵ�½....')
        smtp.login(username,password)  # ��¼������
        time.sleep(random.randint(5,10))
        print('��¼�ɹ���׼�������ʼ�.')
        print('���ڴ�'+sender+'�����ʼ�....')
        smtp.sendmail(sender,receiver,message.as_string())  # �����ʼ��������Ϣ������
        print("�ʼ����ͳɹ�.")
        return True
        print('�˳��ʼ�.')
        smtp.quit()
    except smtplib.SMTPException as e:
        print("�ʼ�����ʧ��.")
        print(e)
        return False

# sendMail('������͵��ʼ�','�������'+config['server'])