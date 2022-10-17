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
from importlib import import_module
from importlib.util import LazyLoader
from importlib.util import   find_spec
from  typing import List,Union,Tuple


class Apps:

    def __init__(self,INSERT_APP=None):
        """

        :param INSERT_APP:
        """

        self.app_insert = None
        if not INSERT_APP:
            self.app_insert = INSERT_APP
        else:
            raise


        self._dict_package = defaultdict(dict)



    def append(self,app_list) -> Union[list,tuple]:
        class_list = None

        for x in app_list:
            # spec_import = find_spec(x)
            # print(spec_import.submodule_search_locations)
            print(import_module(x))
            import_md = import_module(x)
            lazy = LazyLoader(import_md)


            class_list = [x for x in dir(import_md)]



            # if spec_import:
            #     exp_import = import_module(spec_import.name)
            #     print(exp_import)
            #     self._dict_package[spec_import.name] = spec_import.origin
            #     print(self._dict_package)
            #     print(spec_import.origin)
                # cls = hasattr(spec_import, "selenium")
                # print(cls)
            # else:
            #     raise

                # cls(app_name, app_module)


            # # ex = import_module(x)
            # if ex:
            #     pass
            # else:
            #     raise



        return app_list


