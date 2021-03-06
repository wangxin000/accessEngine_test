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


class TestCloseHuaweiIVS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
         pass

    # 打开华为IVS平台第三方平台
    def test_close_huaweiIVS(self):

        request_message_huaweiIVS = {

            "type": 10001,
            "id": 20000,
            "name": "hw_ivs"

        }

        # 初始化thrift客户端
        transport = TSocket.TSocket(Access_Thrift_Ip, Access_Thrift_Port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = IFaaService.Client(protocol)

        transport.open()

        # 调用打开第三方平台接口



        return_message = client.closePlatformAccess(json.dumps(request_message_huaweiIVS))

        print return_message

        transport.close()
if __name__ == '__main__':
    unittest.main(verbosity=2)