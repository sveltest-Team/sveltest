#!/usr/bin/env python
# -*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/16
import pymysql
from sveltest.bin.conf import settings
from sveltest.components.dblib.dbORM.connect import db_connect
from sveltest.components.dblib.dbORM.fields import AutoField, VarcharField, IntegerField, BigIntegerField, TextField
from sveltest.components.dblib.dbORM.orm_enumeration import (Field_SQL, SQL_DDL)
from sveltest.components.dblib.dbORM.query import QuerySet
from sveltest.components.dblib.dbORM.modelbase import ModelMetaClass
from typing import (Optional, List, Tuple, Dict, NoReturn)

from sveltest.components.jinja_template import StringTemplate

db_info = getattr(settings, "DATABASE")

sql_ = StringTemplate(SQL_DDL)


class BaseModel(dict, metaclass=ModelMetaClass, ):

    def __init__(self, **kv):

        super(BaseModel, self).__init__(**kv)
        self.db_connect = db_connect().connect_db()
        self._db_info = self.db_connect.cursor(cursor=pymysql.cursors.DictCursor)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Model has not key %s" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def _getattribute(self):
        fields = []
        params = []
        get_fields = []

        for k, v in self.__mapping__.items():
            # 添加对应字段的名称
            # print(k,v.char)
            if getattr(self, k, None):

                fields.append(v.char)
                get_fields.append(k)
                # 获取对应字段的参数并添加到参数列表中
                params.append(getattr(self, k, None))
            else:
                fields.append(v.char)

        return fields, params, get_fields

    def save(self):
        """用于保持表数据"""
        val = self._getattribute()[-2:]

        fields = [str(x) for x in val[-1]]  # 存放get接收的字段名称
        params = [str(x) for x in val[0]]  # 接收存放get字段的值
        con = {}
        for i, vr in enumerate(params):
            if isinstance(vr, str):
                con[fields[i]] = f'"{vr}"'
            else:
                con[fields[i]] = vr

        try:
            self._db_info.execute(
                sql_.get_string("INSERT_VAL").render(
                    table_name=self.__table__,
                    insert_val=con,
                ).rstrip(','))
            self.db_connect.commit()
        except Exception as e:
            raise Exception(e)
            return

        # self._db_info.close()

    def create_or_update(self):
        pass

    def create_data(self):
        pass

    def drop_database(self):
        """
        删除已存在的表
        :return:
        """

        return self._db_info.execute(
            sql_.get_string("DROP").render(
                table_name=self.__table__,
            )
        )


    def add_comment(self, name: Optional[str]):
        add_comment_table_ddl = "alter table %s comment '%s'" % (self.__table__, name)
        try:
            s = self._db_info.execute(add_comment_table_ddl)
            if s == 0:
                return True
        except Exception as e:
            return False

    @property
    def objects(self):
        """
        删除表数据一条
        """
        return ActionDB(self.__table__, db_connect=self.db_connect, _db_info=self._db_info)

    def create_db(self):
        """

        :return:
        """

        create_db_ddl = ""

        for i in self._getattribute()[0]:
            create_db_ddl = create_db_ddl + " ".join(i) + ","

        rs_ = create_db_ddl.rstrip(",")

        # attr_set['__auto_increment_default__'] = attr_set.get('Meta').auto_increment_default #自增长默认值

        try:
            s = self._db_info.execute(
                sql_.get_string("CREATE").render(
                    table_name=self.__table__,
                    table_field=rs_,
                    comment=self.__verbose_name__
                )
            )
            if s == 0:
                return True
        except Exception as e:
            print(e)
            return False


class ActionDB:

    def __init__(self, table, db_connect, _db_info):
        self.table = table
        self.db_connect = db_connect
        self._db_info = _db_info
        self.type = type
        self.expression = ""
        self.stop = 0
        self.__filter_ddl = False
        self.__order_by_ddl = False
        self.__group_by_ddl = False
        self.__having_ddl = False
        self.all_ = ''

    def null(self,fields:Optional[List[str]],isnull=True,):
        """判断为空的数据"""

        for x in fields:
            if isnull:
                self.expression = self.expression + f"{x} is null,"
            else:
                self.expression = self.expression + f"{x} is not null,"

        self.__filter_ddl = (sql_.get_string('_WHERE').render(
            table_name=self.table,
            expression=self.expression.rstrip(",").replace(",", " and "),
            filter=True
        ))


        return self

    def filter(self, **kwargs):
        """
        exclude !=
        """
        # exclude
        self.stop = 0
        for k in kwargs:
            if k.endswith("exclude"):
                self.expression = self.expression + f"{k.split('_')[0]}!={kwargs[k]},"
            elif k.endswith("gt"):#大于
                self.expression = self.expression + f"{k.split('_')[0]}>{kwargs[k]},"
            elif k.endswith("gte"):#大于等于
                self.expression = self.expression + f"{k.split('_')[0]}>={kwargs[k]},"
            elif k.endswith("lt"):#小于
                self.expression = self.expression + f"{k.split('_')[0]}<{kwargs[k]},"
            elif k.endswith("lte"):#小于等于
                self.expression = self.expression + f"{k.split('_')[0]}<={kwargs[k]},"
            elif k.endswith("in"):#存在于
                self.expression = self.expression + f"{k.split('_')[0]}in{kwargs[k]},"
            elif k.endswith("_range"):#范围查询
                self.expression = self.expression + f"{k.split('_')[0]} BETWEEN {kwargs[k][0]} and {kwargs[k][-1]},"
            elif k.endswith("_irange"):#范围查询 不存在于某个范围
                self.expression = self.expression + f"{k.split('_')[0]} NOT BETWEEN {kwargs[k][0]} and {kwargs[k][-1]},"
            else:
                self.expression = self.expression + f"{k.split('_')[0]}={kwargs[k]},"

        self.__filter_ddl = (sql_.get_string('_WHERE').render(
            table_name=self.table,
            expression=self.expression.rstrip(",").replace(",", " and "),
            filter=True
        ))

        return self

    def order_by(self, fields: Optional[List[str]]):
        expression = ''
        for d in fields:
            if d.startswith("-"):
                expression = expression + d.lstrip("-") + ' DESC,'
            else:
                expression = expression + d + ' ASC,'

        self.__order_by_ddl = (sql_.get_string('_ORDER_BY').render(
            table_name=self.table,
            expression=expression.rstrip(","),
            order_by=True
        ))

        # 排序
        return self

    def group_by(self, fields: Optional[List[str]]):
        # 分组查询
        expression = ''
        for d in fields:
             expression = expression + d+','

        self.__group_by_ddl = (sql_.get_string('_GROUP_BY').render(
            table_name=self.table,
            expression=expression.rstrip(","),
            group_by=True
        ))
        return self

    def having(self,**kwargs):
        """分组后进过滤"""
        self.stop = 0
        for k in kwargs:
            if k.endswith("exclude"):
                self.expression = self.expression + f"{k.split('_')[0]}!='{kwargs[k]}',"
            elif k.endswith("gt"):  # 大于
                self.expression = self.expression + f"{k.split('_')[0]}>'{kwargs[k]}',"
            elif k.endswith("gte"):  # 大于等于
                self.expression = self.expression + f"{k.split('_')[0]}>='{kwargs[k]}',"
            elif k.endswith("lt"):  # 小于
                self.expression = self.expression + f"{k.split('_')[0]}<'{kwargs[k]}',"
            elif k.endswith("lte"):  # 小于等于
                self.expression = self.expression + f"{k.split('_')[0]}<='{kwargs[k]}',"
            elif k.endswith("in"):  # 存在于
                self.expression = self.expression + f"{k.split('_')[0]}in'{kwargs[k]}',"
            elif k.endswith("_range"):  # 范围查询
                self.expression = self.expression + f"{k.split('_')[0]} BETWEEN '{kwargs[k][0]}' and '{kwargs[k][-1]}',"
            elif k.endswith("_irange"):  # 范围查询 不存在于某个范围
                self.expression = self.expression + f"{k.split('_')[0]} NOT BETWEEN '{kwargs[k][0]}' and '{kwargs[k][-1]}',"
            else:
                self.expression = self.expression + f"{k.split('_')[0]}='{kwargs[k]}',"

        self.__having_ddl = (sql_.get_string('_HAVING').render(
            table_name=self.table,
            expression=self.expression.rstrip(",").replace(",", " and "),
            having=True
        ))

        print(self.__having_ddl)

        return self


    def limit(self, end:int,start:int=0,):
        # 分页
        return self.data()[start:end]

    def count(self, **kwargs):

        return len(self.data())

    def distinct(self,fields:Optional[List[str]]=None):
        "去重查询"
        if fields:
            j = ",".join(fields)

        else:
            j =False

        try:
            self._db_info.execute(sql_.get_string('DISTINCT').render(
                    table_field=j,
                    table_name=self.table,
                ))
            return self._db_info.fetchall()
        except Exception as e:
            return e




    def delete(self):
        try:
            self._db_info.execute(sql_.get_string('DELETE').render(
                table_name=self.table,
                _WHERE=self.__filter_ddl
            ))
            self.db_connect.commit()
            return True
        except Exception as e:
            return e

    def update(self, **kwargs):

        con = {}
        for k, vr in kwargs.items():
            if isinstance(vr, str):
                con[k] = f'"{vr}"'
            else:
                con[k] = vr

        try:
            self._db_info.execute(
                sql_.get_string('UPDATE').render(
                    table_name=self.table,
                    update_val=con,
                    _WHERE=self.__filter_ddl
                ).rstrip(",")
            )
            self.db_connect.commit()
            return True
        except Exception as e:
            raise Exception(e)

    def truncate(self):
        """将一个表数据全部清空，但仍保留该表"""
        try:
            self._db_info.execute(sql_.get_string('TRUNCATE').render(
                table_name=self.table,
            )
            )
            self.db_connect.commit()
            return True
        except Exception as e:
            return e

    def all(self):
        """查询所有表数据"""

        self.all_ = sql_.get_string('SELECT').render(
                table_name=self.table
            )
        return self

    def __frist(self):
        """查询所有表数据"""


        return sql_.get_string('SELECT').render(
            table_name=self.table
        )

    def data(self):
        print(sql_.get_string('DELETE_JOIN').render(
                    SQL_MAIN=self.all_ if self.all_ else self.__frist(),
                    _ORDER_BY=self.__order_by_ddl,
                    _GROUP_BY=self.__group_by_ddl,
                    _WHERE=self.__filter_ddl,
                    _HAVING=self.__having_ddl
                ))
        try:
            self._db_info.execute(
                sql_.get_string('DELETE_JOIN').render(
                    SQL_MAIN=self.all_ if self.all_ else self.__frist(),
                    _ORDER_BY=self.__order_by_ddl,
                    _GROUP_BY=self.__group_by_ddl,
                    _HAVING=self.__having_ddl,
                    _WHERE=self.__filter_ddl
                )
            )
            return self._db_info.fetchall()
        except Exception as e:
            return e


# TRUNCATE [TABLE] 表名
if __name__ == '__main__':
    # 创建表模型
    class UserModel(BaseModel):
        id = AutoField(verbose_name="虚拟主键")
        name = VarcharField(default=1, )
        age = IntegerField(null=False, default=0, unique=True)
        data = BigIntegerField(null=False, default=0, unique=True, max_len=20)
        text = TextField(null=False, default=0, max_len=100)

        class Meta:
            table = "user01"
            # verbose_name = "表说明"
            # COMMENT='用户表';


    # 向表user添加数据
    dbc = UserModel(text="666", age=6, data=7, name="777")
    # dbc.create_db()
    # dbc.save()
    # print(dbc.objects.filter(age_gt=1).data())
    # 修改age不等于0，name值为7
    # dbc.objects.filter(age_exclude=0).update(name="7",)
    # 分页查询，对应SQL limit
    # dbc.objects.all().limit(2)
    # 获取查询到的数据总数
    # dbc.objects.all().count()
    # 去重
    # print(dbc.objects.distinct(fields=["name", "data"]))
    # print(dbc.objects.distinct(fields=["text"]))
    # 范围查询 查询age不为3至5的数据
    # print(dbc.objects.null(fields=["t"],isnull=False).data())
    print(dbc.objects.group_by(fields=['name']).having(name="小尚").data())
    # dbc.add_comment(name='ky')
    # 删除当前表

    # orm 不等于 （exclude）
    #
    # __ 大于
    #
    # __ 大于等于
    #
    # __ 小于
    #
    # __小于等于

    # dbc.update()
