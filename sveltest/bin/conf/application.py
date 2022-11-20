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

from collections import defaultdict
# from importlib import import_module
# from importlib.util import LazyLoader
from importlib.util import   find_spec
from  typing import List,Union,Tuple,Optional
from datetime import timedelta, datetime

from sveltest.bin.conf.appconfig import ImportString, importString
from sveltest.components.dblib import ShelveBase



# def auth_app(arg=None,**kwargs):
#     def fun(cls):
#         def wrapper(**kwargs):
#             app_loader()
#             return cls
#         return wrapper(**kwargs)
#     return fun
#


cache = ShelveBase()


class Apps:

    def __init__(self,INSERT_APP=None):
        """

        :param INSERT_APP:
        """

        self.app_insert = None

        if not INSERT_APP:
            self.app_insert = INSERT_APP

        # from sveltest.bin.conf import settings

        # self.component(settings.VALIDATORS)

        self._dict_package = defaultdict(dict)

    def check_module(self,module_name:Optional[str]) -> find_spec:
        """

        """
        module_spec = find_spec(module_name)
        if module_spec is None:
            raise ImportError("Module :{} not found".format(module_name))
        else:
            return module_spec


    # 组件
    def component(self,app_list:Union[list,tuple,str]) -> Union[list,tuple]:
        """

        """

        class_list = None
        spec_ = importString.import_string(app_list)
        if hasattr(spec_,"authenticate"):
            cur_data = spec_().authenticate()
            cache.add("token", cur_data)
            cache.quit()
            return cur_data

        return app_list

    def append(self,app_list:Union[list,tuple,str]) -> Union[list,tuple]:
        """

        """


app_loader = Apps()



# @auth_app()
class AppConfig:
    def __init__(self):
        """app加载"""
