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




class BasicAuth(object):
    """基础认证器"""


    def authenticate(self, auth):
        """
        """
        raise NotImplementedError(".authenticate() must be overridden.")

    def authenticate_header(self, auth):
        """
        """
        pass




class TokenAuth(BasicAuth):
    """token 认证器"""


    def authenticate(self, auth):
        """
        :param auth:
        :return:
        """

        if auth:
            return self.authenticate_header(auth),True

    def authenticate_header(self,auth):
        """
        获取token
        :param auth:
        :return:
        """
        from easydict import EasyDict as edict
        from sveltest.bin.conf import settings
        mod = edict(getattr(settings, "MULTIPLEX_CONFIG"))
        for key in mod.AUTHENTICATOR_CLASSES:
            if key != 'CLASSES':
                return mod.AUTHENTICATOR_CLASSES[key]



if __name__ == '__main__':
    TokenAuth().authenticate(1)
