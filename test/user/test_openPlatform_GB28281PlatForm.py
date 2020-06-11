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


class TestOpenGB28181PlatForm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
         pass

    # GB28282国标平台
    def test_open_GB28181Platform(self):
        request_message_GB28181Platform = {
            "deviceManage": True,
            "id": 7500,
            "ip": "192.168.12.95",
            "name": "intellif_gb28181_server",  # 云天 国标28181平台name
            "other": "{\n\t\"userID\" : \"44000000000000001234\"\n}\n",
            "password": "123456",
            "port": 10005,
            "serverId": "",
            "type": 10004,  # 云天 国标28181平台type
            "userName": "wangxin"

        }
        # 初始化thrift客户端
        transport = TSocket.TSocket(Access_Thrift_Ip, Access_Thrift_Port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = IFaaService.Client(protocol)

        transport.open()

        return_message = client.openPlatformAccess(json.dumps(request_message_GB28181Platform))
        result = json.loads(return_message)
        print return_message
        self.assertEqual("OK", result['respMessage'])  # 断言
        transport.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)