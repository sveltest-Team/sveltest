#!/usr/bin/env python
#-*- coding:utf-8 -*-


import pymysql


class DBConnect(object):
    """
    数据库连接驱动
    """

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.database = "data"
        self.charset = "utf8"
        self.password = "gfl123456"
        self.port = 3306


    def connect_db(self):
        """
        内置的数据库驱动连接
        :return:
        """
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset,
            # port=self.port,

        )


# 为了后续兼容
db_connect = DBConnect
