#!/usr/bin/env python
#-*- coding:utf-8 -*-



"""

                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|



"""


import unittest

from typing import (NoReturn, Optional)
from sveltest.components.network.main import RequestBase


class TestCase(unittest.TestCase):
    """基础类"""


    def __init__(self,methodName='runTest'):
        """

        """
        super(TestCase, self).__init__(methodName=methodName)


    def dispatch(self):

        pass



    def start_class(self) -> NoReturn:
        """"""
        pass

    def end_class(self) -> NoReturn:
        """
        """
        pass

    @classmethod
    def setUpClass(cls) -> NoReturn:
        cls().start_class()

    @classmethod
    def tearDownClass(cls) -> NoReturn :
        cls().end_class()

    def setUp(self) -> NoReturn :
        pass

    def tearDown(self) -> NoReturn :
        pass


    def run(self, result: Optional[unittest.result.TestResult] = ...) \
            -> Optional[unittest.result.TestResult]:

        return super().run(result)


class HttpTestCase(TestCase,RequestBase):
    """
    用于HTTP测试
    """

    def __init__(self,methodName='runTest'):
        """

        """
        super(HttpTestCase, self).__init__(methodName=methodName)
        self.get_auth_class()



    def initizlize_request(self):
        return None


class WebsocketTestCase(TestCase,RequestBase):
    """
    用于websocket测试
    """



class TestCaseSet(HttpTestCase,WebsocketTestCase):
    """
    用于HTTP测试
    """




if __name__ == '__main__':
    HttpTestCase()
