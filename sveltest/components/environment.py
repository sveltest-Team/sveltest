#!/usr/bin/env python
#-*- coding:utf-8 -*-




class BasicEnvironment(object):
    """基础环境控制器"""


    def environment(self, env):
        """

        """
        raise NotImplementedError(".environment() must be overridden.")

    def environment_execute(self, env):
        """
        """
        pass


class DefaultEnvironment(BasicEnvironment):

    def environment(self, env):

        pass

    def get_environment(self):

        # x = OpenExecl(r'F:\multiplex\src\multiplex\data\test.xlsx')
        # setattr(dataSource,"DATA_SOURCE",x.get_rows_all())
        # print("xxxx====xxxx",getattr(dataSource, "DATA_SOURCE"))
        return 1

    def environment_execute(self,env):
        pass



