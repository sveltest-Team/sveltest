#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2021/12/10


import pymysql
from sveltest.components.dblib.sql import DBConnect


class DBConnectMysSQL(DBConnect):
    """

    """
    def all(self,table):
        sql = "SELECT * FROM %s"%table
        cursor_data = self.connect_db().cursor(cursor=pymysql.cursors.DictCursor)
        cursor_data.execute(sql)
        data = cursor_data.fetchall()

        self.connect_db().commit()
        self.connect_db().close()
        return data

    def get(self,table,pk):
        sql = "SELECT * FROM %s WHERE id=%s"%(table,pk)
        cursor_data = self.connect_db().cursor(cursor=pymysql.cursors.DictCursor)
        cursor_data.execute(sql)
        data = cursor_data.fetchall()

        self.connect_db().commit()
        self.connect_db().close()
        return data

mysql_db = DBConnectMysSQL



if __name__ == '__main__':
    db = DBConnectMysSQL()
    x = db.get("user",'1')
    print(x)
