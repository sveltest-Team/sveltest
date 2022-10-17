#!/usr/bin/env python
#-*- coding:utf-8 -*-

import importlib
import os

from selenium import webdriver


import unittest

# class GetSettings:
#
#     def __init__(self):
#         os.environ.setdefault('settings', 'sweet.lib.unit.common.settings')
#
#     def setting_api(self):
#         from sweet.config.conf import settings
#         from easydict import EasyDict as edict
#         return edict(getattr(settings,"MULTIPLEX_CONFIG"))
#
# api_settings = GetSettings().setting_api()

# 扩展程序列表
class TestCaseView(unittest.TestCase):
    # Environment controller
    # 环境控制器
    # environment_classes = None
    # Assertion validator
    # 断言验证器
    # assertion_validator_classes = None
    # Test executor
    # 测试执行器
    # test_executor_classes = None
    # Logger
    # 日志器
    # logger_classes = None
    # Version controller
    # 版本控制器
    # version_controller_classes = None
    # Session authenticator
    # 认证器
    # authenticator_classes = api_settings.AUTHENTICATOR_CLASSES.CLASSES
    # Data drive
    # 数据驱动器
    #:TODO 暂未完成的功能
    # datadriver_classes = api_settings.DATA_DRIVER_CLASSES

    def __init__(self,methodName='runTest'):
        """

        :param methodName:
        """
        super(TestCaseView, self).__init__(methodName=methodName)
        self.data_driver = None



    # def beforeCreate(self):
    #     print("6666")
    #     self._run_datadriver()

    # def created(self):
    #
    #     self._run_authenticator()


    # def get_data(self):
    #     from sweet.config.conf import settings
    #
    #     return getattr(settings,"TEST_DATA")

    # def get_testview_description(self):
    #     """
    #     获取测试用例的方法描述
    #     :return:
    #     """
    #
    #
    # def get_authenticators(self):
    #     """
    #     Instantiates and returns the list of authenticators that this view can use.
    #     """
    #     return [auth() for auth in self.authenticator_classes]
    #
    # def _run_authenticator(self):
    #     """
    #
    #     :return:
    #     """
    #     # set_auth = self.authenticator_classes
    #     if isinstance(self.authenticator_classes,list):
    #         try:
    #             set_auth = self.get_authenticators()
    #             if len(set_auth) >= 1:
    #                 self.auth = {"token":2}
    #                 self.get_authenticators()[0].authenticate(self.auth)
    #         except:
    #             # 废弃
    #             # module = importlib.import_module(self.authenticator_classes[0])
    #             module = ImportString().import_string(self.authenticator_classes[0])
    #             module().authenticate_header(True)

    # def get_datadrivers(self):
    #     """
    #
    #     :return:
    #     """
    #     return [data() for data in self.datadriver_classes]
    #
    #
    # def _run_datadriver(self):
    #     """
    #
    #     :return:
    #     """
    #     if isinstance(self.datadriver_classes,list):
    #         try:
    #             set_data = self.get_datadrivers()
    #             if len(set_data) >= 1:
    #                     self.get_datadrivers()[0].datadrvier(data=1)
    #
    #         except:
    #             # 废弃
    #             # module = importlib.import_module(self.authenticator_classes[0])
    #             module = ImportString().import_string(self.datadriver_classes[0])
    #             print("=============>",module)
    #             module().datadrvier_execute(True)
    #
    #


# class APITestCaseView(TestCaseView,Client):
#     """
#     """
#     def __init__(self,methodName='runTest'):
#         super(APITestCaseView, self).__init__(methodName=methodName)
#         self.header_token = False
#         self._get_public = None
#         self._token = None
#         self.headers = {}
#         self._get_auth_config()
#


class UITestCaseView(TestCaseView):
    def __init__(self,methodName='runTest'):
        super(UITestCaseView, self).__init__(methodName=methodName)




    # def chrome(self):
    #     driver = webdriver.Chrome()
    #     self.driver = pageElement(driver)
    #     return self.driver
    #
    # def open(self,path=None):
    #     self.chrome().open(path)



# class APPTestView(TestView,Client):
#     def __init__(self,methodName='runTest'):
#         super(APPTestView, self).__init__(methodName=methodName)
#
# class QTTestView(TestView,Client):
#     def __init__(self,methodName='runTest'):
#         super(QTTestView, self).__init__(methodName=methodName)
#
# class GenericTestView(APITestView,UITestView,APPTestView,QTTestView):
#     def __init__(self,methodName='runTest'):
#         super(GenericTestView, self).__init__(methodName=methodName)




class ImportString:
    """
    使用字符串进行动态导入模块
    """
    def import_string(self,dotted_path):
        """
        Import a dotted module path and return the attribute/class designated by the
        last name in the path. Raise ImportError if the import failed.
        """
        try:
            module_path, class_name = dotted_path.rsplit('.', 1)
        except ValueError as err:
            raise ImportError("%s doesn't look like a module path" % dotted_path) from err

        module = importlib.import_module(module_path)

        try:
            return getattr(module, class_name)
        except AttributeError as err:
            raise ImportError('Module "%s" does not define a "%s" attribute/class' % (
                module_path, class_name)
                              ) from err

