#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/5/28


import base64
import os

import redis
from typing import Tuple, List, Dict, Union


# TODO: 未完成
class Base64(object):

    def __init__(self,imgPath):
        self.imgPath = imgPath


    def encode(self):
        pass

    def decode(self):
        pass



    def save(self,filePath=None):
        """
        :param filePath:
        :return:
        """
        with open(self.imgPath,"rb") as f:#转为二进制格式
            base64_data = base64.b64encode(f.read())#使用base64进行加密
            file=open(filePath,'wt')
            #写成文本格式
            file.write(base64_data.decode())
            file.close()





class FastRedis:
    def __init__(self,host:str="127.0.0.1",port:Union[int,str]=6379,
                 db:str=0,decode_responses:bool=True,password:Union[str,int]=None
                 ):
        self.pool =  redis.ConnectionPool(
            host=host, port=port,
            password=password,db=db,
            decode_responses=decode_responses
        )


    def _connect(self):
        # self.pool = redis.Redis(self.pool,host='localhost', port=6379, db=0,charset="utf-8")
        return redis.Redis(connection_pool=self.pool)


    def flushall(self):
        """清空redis"""
        return self._connect().flushall()

    def native(self):
        """
        原生redis
        """
        return redis.Redis(connection_pool=self.pool)


fa =FastRedis()
# fa.()



class StringRedis(FastRedis):
    def __init__(self):
        super(StringRedis,self).__init__()
        self.redis = self._connect()


    def set(self,key:Union[int,str,float,bool],value:Union[Dict,int,str,float,bool]) -> Union[Dict,int]:
        """设置字符串
        nx:为TRUE时则会进行将name的value进行更换
        """
        if self.redis.set(key, value, nx=True):
            return True
        else:
            return {"status":0,"message":f"{key}已存在数据库"}
#
#     def get(self,key):
#         return self.redis.get(key)
#
#     def null_set(self,key,value):
#         """当key不存在为True"""
#         return self.redis.setnx(key, value)
#
#     def setTime(self,key,value,time):
#         """指定时间key会变为null
#         time 可以为s 可以为timedate对象
#         """
#         return self.redis.setex(key,time,value)
#
#     def sets(self,*args, **kwargs):
#         """一次设置多个键
#         1、k1=1
#         2、{k1:"1"}
#         """
#         return self.redis.mset(*args, **kwargs)
#     def gets(self,*args, **kwargs):
#         """一次设置多个键
#         1、k1=1
#         2、gets("k2","set")
#         """
#         return self.redis.mget(*args, **kwargs)
#
#     def reset(self,ke, value):
#         """设置新的值、获取原来的值"""
#         return self.redis.getset(ke, value)
#
#     def getBit(self,key,start,stop):
#         """安装字节进行获取值"""
#         return self.redis.getrange(key,start,stop)
#
#     def length(self,key):
#         """获取key的字节长度、中文为3个字符"""
#         return self.redis.strlen(key)
#
#     def autoCount(self,key,count,type=0):
#         """key值自增"""
#         if type == 0:
#             return self.redis.incr(key,count)
#         else:
#             return self.redis.incrbyfloat(key,count)
#
#     def autoDecr(self,key,count,type=0):
#         """key值自减"""
#         if type == 0:
#             return self.redis.decr(key,count)
#         else:
#             return self.redis.incrbyfloat(key,count)
#
#
#     def addString(self,key,text):
#         """key值追加字符串"""
#         return self.redis.append(key,text)
#
# class HashRedis(TankRedis):
#     def __init__(self):
#         super(HashRedis,self).__init__()
#         self.redis = self.connect()
#
#
#     def hmset(self,key,field,value):
#        """ 单个增加 - -修改(单个取出) - -没有就新增，有的话就修改"""
#        return self.redis.hset(key,field,value)
#
#
#     def hget(self,key,field):
#         return self.redis.hget(key, field)
#
#     def getKeys(self,key):
#         return self.redis.hkeys(key)
#
#     def keys(self,name, keys, *args):
#         return self.redis.hmget(name, keys, *args)
#
#     def add(self,name, key, value):
#         """只能新建"""
#         return self.redis.hsetnx(name,key,value)
#
#     def setAdds(self,name, set_:dict):
#         """添加字典类型"""
#         return self.redis.hmset(name,set_)
#
#     def getAll(self,name):
#         return self.redis.hgetall(name)
#
#     def length(self,name):
#         """hlen(name) 获取键值对长度"""
#         return self.redis.hlen(name)
#
#     def values(self,name):
#         """获取所有值"""
#         return self.redis.hvals(name)
#
#     def ists(self,name,key):
#         """查询某个key是否存在"""
#         return self.redis.hexists(name, key)
#
#     def delKey(self,name,*keys):
#         """删除指定的键值对"""
#         return self.redis.hdel(name,*keys)
#
#
#     def autoCount(self,name,key,count):
#         """key值自增减 int"""
#         return self.redis.hincrby(name,key,amount=count)
#
#     def autoFloat(self,name,key,count):
#         """key值自增减  float"""
#
#         return self.redis.hincrbyfloat(name,key,count)
