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



import os
import importlib
from sveltest.bin.conf import global_settings


class Settings():
    # 初始化项目配置信息
    def __init__(self):
        # 遍历默认的配置文件，并将配置信息添加到，配置对象当中
        for setting in dir(global_settings):
            # 判断是否是大写
            if setting.isupper():
                # 通过反射添加值
                setattr(self, setting, getattr(global_settings, setting))

            # 获取用户的模块字符串
        try:
            mod = os.environ.get('SVELTEST_TEST_SETTINGS_MODULE')

            # importlib可以通过字符串进行导入模块
            module = importlib.import_module(mod)

            # 遍历用户配置文件，并将配置信息添加到对象中，如果重复会覆盖之前系统的配置信息
            for setting in dir(module):

                if setting.isupper():
                    setattr(self, setting, getattr(module, setting))

        except:
            pass


settings = Settings()



