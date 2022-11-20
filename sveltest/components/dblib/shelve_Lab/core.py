#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/1
import os
import shelve
from pathlib import Path
from typing import (Optional,Union,Any)


class ShelveBase:


    def __init__(self,filename:Optional[str]=None,flag:str="c",protocol:Optional[Union[bool,int]]=None,
                 writeback:Optional[bool]=False):
        """

        """

        self.BASE_DIR = Path(__file__).resolve().parent

        if filename:
            self.__db = shelve.open(filename=filename, flag=flag, protocol=protocol,
                                    writeback=writeback)
        else:
            self.__db = shelve.open(filename=os.path.join(self.BASE_DIR, 'db_dir/cache').replace("\\", "/"), flag=flag,
                                    protocol=protocol, writeback=writeback)


    def add(self,k:Optional[str],v:Optional[Any]) -> bool:
        """

        """
        try:
            self.__db[k] = v
            return True
        except:
            return False

    def update(self,k:Optional[str],v:Optional[Any]) -> bool:
        pass


    def exists(self,k:Optional[str]) -> bool:
        if k in self.__db:
            return True
        else:
            return False

    def get(self,k:Optional[str]):
        try:
            return self.__db[k]
        except:
            return None

    def delete(self,k:Optional[str]) -> bool:
        try:
            del self.__db[k]
            return True
        except:
            return False

    def quit(self):
        self.__db.close()

    def clear(self,path:Optional[str]=None):
        """

        """
        for x,r,d in os.walk(path if path else self.BASE_DIR):
            for de in d:
                if str(de).endswith(".py"):
                    continue
                else:
                    if os.path.isfile(os.path.join(x,de).replace("\\","/")):
                        os.remove(os.path.join(x,de).replace("\\","/"))




if __name__ == '__main__':
    data_cache = ShelveBase()
    # data_cache.add(k="sveltest",v={"name":"自动化测试","type":0})
    # data_cache.add(k="自动化测试",v="sveltest框架")
    # data_cache.add(k="obj",v=data_cache)
    # # 添加一个key 并且给key赋值,如果存在则修改它的值
    # s.add("小明","1")
    # s.add("小明","2")
    # # 查看一个key是否存在于缓存(数据库)
    # print(s.exists("小明"))
    # # 获取一个key的值
    data_cache.clear()
    data_cache.clear(path="cache")

    # # 删除一个存在的key
    # s.delete("小明")
    # # 清理数据库缓存文件
    # # s.clear()
    # # 关闭并退出数据库
    # s.quit()
    #


