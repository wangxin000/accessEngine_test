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


class TestStartCameraTask(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
         pass

    # 开启摄像头任务
    def test_start_CameraTask(self):
        request_message_camera ={
        "cameras": [{
            "ipcAlg": "-1",
            "ipcFlag": "0",
            "sourceBank": "0",
            "ipcUser": "admin",
            "ipcRtspUri": "http://192.168.13.23:8080/ifstore000001/M00/D9/86/wKgNF16Nd3KEKz6aAAAAAG2qk3U776.mp4",
            "ipcAddr": "192.168.13.23",
            "bankId": "0f73ff92-d8fb-4bde-9f2a-98a5d2a37d2f",
            "cameraId": "88194",
            "taskFlag": "0",
            "ipcCapability": "3",
            "inStation": "0",
            "cameraCode": "",
            "ipcPort": "8000",
            "ability": "[{\"attribute\":[\"glasses\",\"gender\",\"race\",\"pose\",\"hat\",\"landmark\",\"age\",\"mask\",\"quality\"],\"target\":\"face\"},{\"attribute\":[\"coatPattern\",\"coatStyle\",\"gender\",\"angle\",\"bag\",\"ageStage\",\"hasCoat\",\"pantsStyle\",\"pantsPattern\",\"ride\",\"clothColor\"],\"target\":\"body\"},{\"attribute\":[\"call\",\"color\",\"belt\",\"marker\",\"plate\",\"type\",\"danger\",\"brand\",\"crash\"],\"target\":\"car\"}]",
            "nodeId": "0",
            "ipcType": "0",
            "ipcPassword": "ytlf1234",
            "stationId": "3"
          }]
        }


        # 初始化thrift客户端
        transport = TSocket.TSocket(Access_Thrift_Ip, Access_Thrift_Port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = IFaaService.Client(protocol)

        transport.open()

        # 调用打开第三方平台接口
        return_message = client.startTask(json.dumps(request_message_camera))
        result = json.loads(return_message)
        print return_message
        self.assertEqual("OK", result['respMessage'])  # 断言
        transport.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)