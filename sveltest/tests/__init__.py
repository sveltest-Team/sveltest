#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/10/19
import functools

from sveltest.support.common import ObjectDict

from sveltest.bin.conf import settings


def env(cls):
    @functools.wraps(cls)
    def wrapper_(*args,**kwargs):
        c_name = cls.__name__
        cls.obj = ObjectDict(settings.ENVIRONMENT_CLASSES_CONFIG)
        print(cls.obj.DEFAULT_ENVIRONMENT_NAME)
        print(cls.obj)
        return cls()

    return wrapper_




@env
class D():
    def test(self):
        print(self.obj)

x = D()
print(x.test(666))
