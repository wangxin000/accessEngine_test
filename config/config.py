#! /usr/bin/python
# -*- coding: utf-8 -*
import logging
import os

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）

data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'test')   # 用例目录

log_file = os.path.join(prj_path, 'log', 'log.txt')  # 更改路径到log目录下
report_file = os.path.join(prj_path, 'report', 'report.html')  # 更改路径到report目录下

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_passwd = '123456'
db = 'api_test'

# 邮件配置
smtp_server = 'imap.exmail.qq.com'
smtp_user = 'wang.xin@intellif.com'
smtp_password = 'Admin_123'

sender = smtp_user  # 发件人
#receiver = 'wang.xin@intellif.com'  # 收件人
receiver = ['wang.xin@intellif.com',"peng.jidong@intellif.com","xiao.fen@intellif.com","li.zhiyuan@intellif.com","luo.zexuan@intellif.com","zhong.bin@intellif.com","engine_team@intellif.com"]  # 多人收件
subject = '接入引擎接口自动化测试报告'  # 邮件主题

#接入引擎信息
AccessEngine_ip = "192.168.13.210"
AccessEngine_port = 7788
