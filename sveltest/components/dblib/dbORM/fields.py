#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/11/16
from sveltest.components.dblib.dbORM.orm_enumeration import  Field_SQL

from sveltest.components.jinja_template import StringTemplate
from typing import (Dict,Optional,Tuple,List,Union)

jk = StringTemplate(Field_SQL)

class Field(object):
    """

    """

    def __init__(self, verbose_name=None, name=None, primary_key=False,
                 max_len=None, unique=False, blank=False, null=False,
                 db_index=False, rel=None,
                 default=None,
                 editable=True,
                 serialize=True, unique_for_date=None, unique_for_month=None,
                 unique_for_year=None, choices=None, help_text='', db_column=None,
                 db_tablespace=None, auto_created=False, validators=(),
                 error_messages=None):
        """

        :param verbose_name:
        :param name:
        :param primary_key:
        :param max_len:
        :param unique:
        :param blank:
        :param null:
        :param db_index:
        :param rel:
        :param default:
        :param editable:
        :param serialize:
        :param unique_for_date:
        :param unique_for_month:
        :param unique_for_year:
        :param choices:
        :param help_text:
        :param db_column:
        :param db_tablespace:
        :param auto_created:
        :param validators:
        :param error_messages:
        """
        self.name = name
        self.verbose_name = verbose_name  # May be set by set_attributes_from_name
        self.primary_key = primary_key
        self.max_len, self._unique = max_len, unique
        self.blank, self.null = blank, null
        self.remote_field = rel
        self.is_relation = self.remote_field is not None
        self.default = default
        self.editable = editable
        self.serialize = serialize
        self.unique_for_date = unique_for_date
        self.unique_for_month = unique_for_month
        self.unique_for_year = unique_for_year
        # if isinstance(choices, collections.abc.Iterator):
        #     choices = list(choices)
        self.choices = choices
        self.help_text = help_text
        self.db_index = db_index
        self.db_column = db_column
        self._db_tablespace = db_tablespace
        self.auto_created = auto_created


    def get_string(self,field_type:Optional[str]="Integer",
                   max_len:Optional[int]=10,type:Optional[str]="longtext",
                   default:Optional[Union[str,int]]=None,verbose_name:Optional[Union[str,int]]=None,
                   primary_key:bool=False,auto_increment:bool=False,null:Optional[bool]=True,unique:Optional[bool]=False
                   ):

        return jk.get_string(field_type).render(max_len=max_len, default=default, verbose_name=verbose_name, primary_key=primary_key,
                                              auto_increment=auto_increment,null=null,unique=unique,type=type)

class IntegerField(Field):

    def __init__(self,
                   max_len:Optional[int]=10,
                   default:Optional[Union[str,int]]=None,verbose_name:Optional[Union[str,int]]=None,
                   primary_key:bool=False,auto_increment:bool=False,null=True,unique:Optional[bool]=False):
        super(IntegerField, self).__init__(null=null,default=default,
                                           # unique=unique
                                           )
        self.max_len = max_len
        self.default = default
        self.verbose_name = verbose_name
        self.primary_key = primary_key
        self.auto_increment = auto_increment
        self.null = null
        self.unique = unique

    def db(self):

        return self.get_string(
            max_len=self.max_len,field_type="Integer",default=self.default,verbose_name=self.verbose_name,primary_key=self.primary_key,
            auto_increment=self.auto_increment,null=self.null,unique=self.unique
        )

        # if min_value is not None:
        #     if not isinstance(min_value, numbers.Integral):
        #         raise ValueError("min_value must be int")
        #     elif min_value < 0:
        #         raise ValueError("min_value must be positive int")
        # if max_value is not None:
        #     if not isinstance(max_value, numbers.Integral):
        #         raise ValueError("max_value must be int")
        #     elif max_value < 0:
        #         raise ValueError("max_value must be positive int")
        # if min_value is not None and max_value is not None:
        #     if min_value > max_value:
        #         raise ValueError("min_value must be smaller than max_value")
        #



    # def __get__(self, instance, owner):
    #     return self._value

    # def __set__(self, instance, value):
    #     if not isinstance(value, numbers.Integral):
    #         raise ValueError("int value need")
    #     if value < self.min_value or value > self.max_value:
    #         raise ValueError("value must between min_value and max_value")
    #     self._value = value

class BigIntegerField(Field):

    def __init__(self,
                   max_len:Optional[int]=10,
                   default:Optional[Union[str,int]]=None,verbose_name:Optional[Union[str,int]]=None,
                   primary_key:bool=False,auto_increment:bool=False,null=True,unique:Optional[bool]=False):
        super(BigIntegerField, self).__init__(null=null,default=default,
                                           # unique=unique
                                           )
        self.max_len = max_len
        self.default = default
        self.verbose_name = verbose_name
        self.primary_key = primary_key
        self.auto_increment = auto_increment
        self.null = null
        self.unique = unique

    def db(self):

        return self.get_string(
            max_len=self.max_len,field_type="Bigint",default=self.default,verbose_name=self.verbose_name,primary_key=self.primary_key,
            auto_increment=self.auto_increment,null=self.null,unique=self.unique
        )

        # if min_value is not None:
        #     if not isinstance(min_value, numbers.Integral):
        #         raise ValueError("min_value must be int")
        #     elif min_value < 0:
        #         raise ValueError("min_value must be positive int")
        # if max_value is not None:
        #     if not isinstance(max_value, numbers.Integral):
        #         raise ValueError("max_value must be int")
        #     elif max_value < 0:
        #         raise ValueError("max_value must be positive int")
        # if min_value is not None and max_value is not None:
        #     if min_value > max_value:
        #         raise ValueError("min_value must be smaller than max_value")
        #



    # def __get__(self, instance, owner):
    #     return self._value

    # def __set__(self, instance, value):
    #     if not isinstance(value, numbers.Integral):
    #         raise ValueError("int value need")
    #     if value < self.min_value or value > self.max_value:
    #         raise ValueError("value must between min_value and max_value")
    #     self._value = value


class TextField(Field):

    def __init__(self,
                 max_len:Optional[Union[int,str]]=1024,
                   default:Optional[Union[str,int]]=None,verbose_name:Optional[Union[str,int]]=None,
                   primary_key:bool=False,auto_increment:bool=False,null=True,):
        super(TextField, self).__init__(null=null,default=default,
                                           # unique=unique
                                           )
        self.default = default
        self.verbose_name = verbose_name
        self.primary_key = primary_key
        self.auto_increment = auto_increment
        self.null = null
        self.max_len = max_len

    def db(self):

        return self.get_string(
            max_len=False,
            field_type="default",type="longtext",default=None,verbose_name=self.verbose_name,primary_key=self.primary_key,
            auto_increment=self.auto_increment,null=self.null,
        )

        # if min_value is not None:
        #     if not isinstance(min_value, numbers.Integral):
        #         raise ValueError("min_value must be int")
        #     elif min_value < 0:
        #         raise ValueError("min_value must be positive int")
        # if max_value is not None:
        #     if not isinstance(max_value, numbers.Integral):
        #         raise ValueError("max_value must be int")
        #     elif max_value < 0:
        #         raise ValueError("max_value must be positive int")
        # if min_value is not None and max_value is not None:
        #     if min_value > max_value:
        #         raise ValueError("min_value must be smaller than max_value")
        #



    # def __get__(self, instance, owner):
    #     return self._value

    # def __set__(self, instance, value):
    #     if not isinstance(value, numbers.Integral):
    #         raise ValueError("int value need")
    #     if value < self.min_value or value > self.max_value:
    #         raise ValueError("value must between min_value and max_value")
    #     self._value = value


class FieldChar(Field):


    def name(self):
        return "INT"


    def _check_parm(self):
        """

        :return:
        """


class Argument:

    DB_ARGUMENT = {
        "DEFAULT_NULL":"DEFAULT NULL",
        "NOT_NULL":"NOT NULL"
    }

arg = Argument

class AutoField(Field):
    """

    """

    def __init__(self,
                   max_len:Optional[int]=10,
                   default:Optional[Union[str,int]]=None,verbose_name:Optional[Union[str,int]]=None
                   ,unique:Optional[bool]=False):
        super(AutoField, self).__init__(default=default,
                                           # unique=unique
                                           )
        self.max_len = max_len
        self.default = default
        self.verbose_name = verbose_name


    def db(self):

        return self.get_string(
            max_len=self.max_len, field_type="Integer", default=self.default, verbose_name=self.verbose_name,
            primary_key=True,
            auto_increment=True,null=False
        )




class VarcharField(Field):
    """
    """
    def __init__(self,
                   max_len:Optional[int]=10,
                   default:Optional[Union[str,int]]=None,verbose_name:Optional[Union[str,int]]=None,
                   primary_key:bool=False,null=False,unique:Optional[bool]=False):

        super(VarcharField, self).__init__(null=null,default=default,
                                           # unique=unique
                                           )
        self.max_len = max_len
        self.default = default
        self.verbose_name = verbose_name
        self.primary_key = primary_key
        self.null = null



    def db(self):

        return self.get_string(
            max_len=self.max_len, field_type="Varchar", default=self.default, verbose_name=self.verbose_name,
            primary_key=self.primary_key,null=self.null
        )
