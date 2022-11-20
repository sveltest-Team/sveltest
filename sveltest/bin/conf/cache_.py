#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/10/31

from typing import Optional,Union,Dict



"""
基于内存缓存
"""
import time


class Value:
    def __init__(self, value, put_time, expired):
        """
        缓存值对象

        :param value: 具体的值
        :param put_time: 放入缓存的时间
        :param expired: 缓存失效时间
        """
        self.value = value
        self.put_time = put_time
        self.expired = expired



class CacheBase:
    exec_ = 0

    def __init__(self):
        self.__cache = {}
        self.__cache_all = {}

    def set(self, k, v, expired):
        """
        将值放入缓存中

        :param k: 缓存的 key
        :param v: 缓存值
        :param expired: 缓存失效时间，单位秒(s)
        """
        current_timestamp = int(time.time())  # 获取当前时间戳 10 位 秒级
        value = Value(v, current_timestamp, expired)
        self.__cache[k] = value
        self.__cache_all[k] = v


    def check(self, k):
        """
        检查缓存是否可用

        :param k: 缓存 key
        :return: True or False
        """
        current_timestamp = int(time.time())
        value = self.__cache.get(k, None)

        if value is None:
            return False
        differ = current_timestamp - value.put_time

        if differ > value.expired:
            del self.__cache[k]
            del self.__cache_all[k]
            return False
        return True

    def get(self, k:Optional[str]=None):
        """
        通过缓存key获取值

        :param k: key
        :return: value
        """
        if k:
            if self.check(k):
                return self.__cache[k].value
            return None
        else:
            return self.__cache_all


cache_base = CacheBase()








