#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/16

from sveltest.components.dblib.dbORM.fields import (
    IntegerField, AutoField, VarcharField, BigIntegerField, TextField
)


class ModelMetaClass(type):
    """

    """
    def __new__(cls, name, bases, attr_set):
        """

        """

        # 用於存储映射类型属性
        mapping_set = dict()

        if name == 'BaseModel':
            return type.__new__(cls, name, bases, attr_set)

        for k, v in attr_set.items():
            # 判断是否是对应的 字段类型

            if isinstance(v, IntegerField) or isinstance(v,AutoField) \
                    or isinstance(v,VarcharField) or isinstance(v,BigIntegerField)\
                    or isinstance(v,TextField):
                # 将key进行设置成类属性
                setattr(v, 'char', [k,v.db()])
                mapping_set[k] = v


        # 删除这些已经在字典中存储的属性
        for k in mapping_set.keys():
            attr_set.pop(k)


        # 保存属性和列的映射关系
        attr_set['__mapping__'] = mapping_set

        # 获取用户定义的表名
        attr_set['__table__'] = attr_set.get('Meta').table

        try:
            attr_set['__verbose_name__'] = attr_set.get('Meta').verbose_name
        except:
            attr_set['__verbose_name__'] = None

        try:
            attr_set['__auto_increment_default__'] = attr_set.get('Meta').auto_increment_default
        except:
            attr_set['__auto_increment_default__'] = None

        return type.__new__(cls, name, bases, attr_set)


