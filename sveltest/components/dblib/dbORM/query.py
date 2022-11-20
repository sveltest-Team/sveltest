#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/16
from typing import Optional, List

import pymysql


from sveltest.components.dblib.dbORM.connect import db_connect
from sveltest.components.dblib.dbORM.orm_enumeration import SQL_DDL
from sveltest.components.jinja_template import StringTemplate

sql_ = StringTemplate(SQL_DDL)

class Cache:
    """临时缓存"""
    def __new__(cls, *args, **kwargs):
        return


cache = Cache



class QueryDict:

    def __init__(self,kv,t):
        self.kv = kv
        self.t = t

    def __str__(self):
        try:
            return "<%s:%s>"%(self.t,self.kv["id"])
        except:
            return "<%s:%s>"%(self.t,None)

    def value(self,field):
        return self.kv[field]




class QuerySet:
    """
    """
    def __init__(self, table, db_connect, _db_info):
        """

        """
        self.table = table
        self.db_connect = db_connect
        self._db_info = _db_info
        self.order_by_ddl = False


        # super(QuerySet, self).__init__(kv)



    # def __getattr__(self, key):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         raise AttributeError("Model has not key %s" % key)
    #
    # def __setattr__(self, key, value):
    #     # if key == "table" or key == "kv":
    #     #     pass
    #     # else:
    #         self[key] = value



    def order_by(self, fields: Optional[List[str]]):

        expression = ''
        for d in fields:
            if d.startswith("-"):
                expression = expression + d.lstrip("-") + ' DESC,'
            else:
                expression = expression + d + ' ASC,'

        self.order_by_ddl = (sql_.get_string('_ORDER_BY').render(
            table_name=self.table,
            expression=expression.rstrip(","),
            order_by=True
        ))

        # 排序
        return self



    def _getattribute(self,**kwargs):
        self.table = kwargs


    def data_cache(self):
        return


    def filter(self,**kwargs):
        """
        进行过滤筛选
        :param kwargs:
        :return:
        """
        fields = [] # 存放get接收的字段名称
        params = [] # 接收存放get字段的值

        if len(kwargs) > 1:
            print(len(kwargs))

        for k,v in kwargs.items():
            fields.append(k)
            params.append(str(v))

        select_dml = "select * from %s where %s=%s"%(self.table,''.join(fields),''.join(params))
        db_ct = db_connect().connect_db()
        _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)
        # print(_db_info)
        _db_info.execute(select_dml)

        table_fields = _db_info.description
        data = _db_info.fetchone()
        db_ct.commit()
        _db_info.close()


        setattr(cache,"data",data)
        setattr(cache,"field",kwargs)
        setattr(cache,"table",self.table)
        setattr(cache,"type",0)
        if data:
            d = QuerySet(data)
            d.pop("table")
            d.pop("kv")
            return d
        else:
            raise Exception("不存在")



    def all(self,**kwargs):
        """获取"""
        fields = [] # 存放get接收的字段名称
        params = [] # 接收存放get字段的值

        for k, v in kwargs.items():
            fields.append(k)
            params.append(str(v))

        select_dml = "select * from %s " % self.table

        db_ct = db_connect().connect_db()
        _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)
        _db_info.execute(select_dml)

        data = _db_info.fetchall()

        db_ct.commit()
        _db_info.close()

        class db:
            def __init__(self,table):
                self.table = table

            def __str__(self):
                return str([QueryDict(x, self.table) for x in data])

            def count(self):
                return len(data)

            @property
            def data(self):
                r = []
                for x in data:
                    x = QuerySet(x, self.table)
                    x.pop("table")
                    r.append(x)

                return r

        return db(self.table)



    def value(self,key):
        """
        获取指定字段的值
        :param key:
        :return:
        """
        cache_ = getattr(cache,"data")
        return cache_[key]

    def delete(self):
        """
        获取指定字段的值
        :param key:
        :return:
        """
        cache_ = getattr(cache,"field")
        table = getattr(cache,"table")
        type = getattr(cache,"type")

        if type == 0:
            filed_ = []
            val = []
            for x in cache_:
                filed_.append(x)
                val.append(str(cache_[x]))

            del_db = "delete from %s where %s=%s"%(table,''.join(filed_),''.join(val))

            db_ct = db_connect().connect_db()
            _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)

            x = _db_info.execute(del_db)
            db_ct.commit()
            _db_info.close()
            db_ct.close()

            return x

    def get(self, **pk):
        """
        用于直接获取一条数据
        :param kwargs: 指定相应的字段与值
        :return:
        """

        fields = [] # 存放get接收的字段名称
        params = [] # 接收存放get字段的值

        for k,v in pk.items():
            fields.append(k)
            params.append(str(v))


        select_dml = "select * from %s where %s=%s"%(self.table,''.join(fields),''.join(params))
        db_ct = db_connect().connect_db()
        _db_info = db_ct.cursor(cursor=pymysql.cursors.DictCursor)

        _db_info.execute(select_dml)

        data = _db_info.fetchone()

        db_ct.commit()
        _db_info.close()

        setattr(cache,"data",data)
        setattr(cache,"field",pk)
        setattr(cache,"table",self.table)
        setattr(cache,"type",0)
        if data:
            d = QuerySet(data)
            d.pop("table")
            d.pop("kv")
            return d
        else:
            raise Exception("不存在")
