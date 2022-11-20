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
from sveltest.components.network.main import RequestBase

class BaseAuth:
    """
    所有认证器都需要基础这个类
    """

    def authenticate(self,):
        """
        进行重写该方法来实现认证
        """
        raise NotImplementedError(".authenticate() must be overridden.")

    def authenticate_header(self,):
        """
        """
        pass



