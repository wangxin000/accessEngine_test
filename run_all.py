#! /usr/bin/python
# -*- coding: utf-8 -*
import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_email

logging.info("================================== 测试开始 ==================================")
suite = unittest.defaultTestLoader.discover(test_path)

with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="接口自动化测试报告（接入引擎）", description="测试执行情况描述：", tester="王欣").run(suite)

send_email(report_file)  # 从配置文件中读取

logging.info("================================== 测试结束 ==================================")
#print "邮件发送成功"