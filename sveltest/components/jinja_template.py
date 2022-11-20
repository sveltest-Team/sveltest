#!/usr/bin/env python
#-*- coding:utf-8 -*-

from typing import (Optional, Dict)

from jinja2 import (DictLoader, Environment,FileSystemLoader)


class JinJaTemplate:

    def __init__(self,temp_dir=Optional[str]):
        # 创建一个包加载器对象
        self.env = Environment(loader=FileSystemLoader(
            temp_dir.replace("\\","/")
        ))



    def get_template(self,t:Optional[str]):
        """

        :param t:
        :return:
        """
        return self.env.get_template(t)



class StringTemplate:
    def __init__(self,temp:Optional[Dict]):

        self.loader = DictLoader(temp)
        self.env = Environment(loader=self.loader)
        # template = env.get_template("index.html")

        # print(template.render(name="TEST"))
    def get_string(self,t:Optional[str]):
        """

        :param t:
        :return:
        """
        return self.env.get_template(t)


