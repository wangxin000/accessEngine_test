#! /usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import requests
import json
import sys
sys.path.append("../..")  # 提升2级到项目根目录下
from config.config import *  # 从项目路径下导入
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info  # 从项目路径下导入
#! /usr/bin/python
# -*- coding: utf-8 -*
import sys
import json
import base64
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from IFaaService import IFaaService
from IFaaService.ttypes import *
from IFaaService.constants import *




Access_Thrift_Ip = AccessEngine_ip
Access_Thrift_Port = AccessEngine_port


class TestOpenDataGateWay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
         pass

    #打开数据网关第三方平台
    def test_open_DataGateway(self):

        request_message_DataGateway = {
            "deviceManage": True,  # 是否需要上报平台设备列表
            "id": 10100,  # 平台ID  t_base_platform_type中的id？还是t_third_platform_info中的id？
            "ip": "192.168.11.42",  # 平台地址
            "name": "deep_eye",  # 平台类型名称
            "other": "{\n\t\"userID\" : \"44000000000000000004\"\n}\n",  # 其他信息
            "password": "admin1234",  # 平台登录密码
            "port": 3019,  # 平台端口
            "serverId": "20001",  # ？？？？
            "type": 10006,  # 平台类型编号, 视图库=10003, 华为ivs=10001, 深目数据网关=20006
            "userName": "admin"  # 平台用户名
        }
        # 初始化thrift客户端
        self.type = type
        transport = TSocket.TSocket(Access_Thrift_Ip, Access_Thrift_Port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = IFaaService.Client(protocol)

        transport.open()

        return_message = client.openPlatformAccess(json.dumps(request_message_DataGateway))
        result = json.loads(return_message)
        print return_message
        self.assertEqual("OK", result['respMessage'])  # 断言
        transport.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)