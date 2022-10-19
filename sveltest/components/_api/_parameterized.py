#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/28

"""
                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|
"""
# https://github.com/wolever/parameterized



import inspect
import json

from functools import wraps
# 数据驱动

from sveltest.components._core import Data
from sveltest.components.dblib.mysqldb import mysql_db
from sveltest.components.data.core import xml_json_loader
from sveltest.components.data.core import SvelteYaml

try:
    import yaml
except ImportError:  # pragma: no cover
    _have_yaml = False
else:
    _have_yaml = True


# 使用data
DATA_DRIVER = '%str_values'

DATA_LIST_DRIVER = '%values'

DATA_DICT_DRIVER = '%dict_data'

# json使用文件
FILE_DRIVER = '%file_path'

# 使用 yaml
YAML_LOADER_DRIVER = '%yaml_loader'

# 使用分词/解包
UNPACK_DRVER = '%unpack'

# 默认的大小写长度为5
index_len = 5




def unpack(func):
    """
    方法装饰器以添加解包特性。

    """
    setattr(func, UNPACK_DRVER, True)
    return func

def _check_data(data):
    return all(isinstance(i, (int, bool,str)) for i in data)

def _check_type(data):

    return all(isinstance(i,(tuple,list)) for i in data)

def _check_dict(data):

    return all(isinstance(i,(dict)) for i in data)

def char(*str_values):
    """
    接收数据原始数据
    """


    def wrapper(func):
        if _check_data(str_values):
            global index_len
            index_len = len(str(len(str_values)))
            setattr(func, DATA_DRIVER, str_values)
        else:
            raise Exception("不为字符串")
        return func
    return wrapper


mock_data = Data()


class MockChar:


    def __init__(self):
        pass


    @classmethod
    def enal(self,count=1,isupper=False):
        """
        英文单词
        :param mode:
        :param count:
        :param kwargs:
        :return:
        """


        if count >=1:
            data = [mock_data.alphabet(isupper=isupper) for x in range(count)]

        else:
            data = mock_data.alphabet()

        def wrapper(func):
            if _check_data(data):
                global index_len
                index_len = len(str(len(data)))
                setattr(func, DATA_DRIVER, data)
            else:
                raise Exception("不为字符串")
            return func

        return wrapper

    @classmethod
    def country(self,count=1,):
        """
        国家名称
        :param mode:
        :param count:
        :param kwargs:
        :return:
        """


        if count >=1:
            data = [mock_data.country() for x in range(count)]

        else:
            data = mock_data.country()

        def wrapper(func):
            if _check_data(data):
                global index_len
                index_len = len(str(len(data)))
                setattr(func, DATA_DRIVER, data)
            else:
                raise Exception("不为字符串")
            return func

        return wrapper

    @classmethod
    def city_suffix(self,count=1,):
        """
        国家名称
        :param mode:
        :param count:
        :param kwargs:
        :return:
        """


        if count >=1:
            data = [mock_data.city_suffix() for x in range(count)]

        else:
            data = mock_data.city_suffix()

        def wrapper(func):
            if _check_data(data):
                global index_len
                index_len = len(str(len(data)))
                setattr(func, DATA_DRIVER, data)
            else:
                raise Exception("不为字符串")
            return func

        return wrapper


    @classmethod
    def date(self,count=1,):
        """
        国家名称
        :param mode:
        :param count:
        :param kwargs:
        :return:
        """


        if count >=1:
            data = [mock_data.date() for x in range(count)]

        else:
            data = mock_data.date()

        def wrapper(func):
            if _check_data(data):
                global index_len
                index_len = len(str(len(data)))
                setattr(func, DATA_DRIVER, data)
            else:
                raise Exception("不为字符串")
            return func

        return wrapper



    def chars(self):
        pass

    def formdata(self,**kwargs):
        try:
            if kwargs["parameters"]:
                pass
        except:
            print("异常")



# def mock_char():
#     """
#     接收数据原始数据
#     """
#
#     data = ("60",6,5)
#
#
#
#     def wrapper(func):
#         if check_data(data):
#             global index_len
#             index_len = len(str(len(data)))
#             setattr(func, DATA_DRIVER, data)
#         else:
#             raise Exception("不为字符串")
#         return func
#     return wrapper
#


def extends(*values):
    """
    接收一组列表数据
    :param data:
    :return:
    """
    def wrapper(func):
        if _check_type(values):
            global index_len
            index_len = len(str(len(values)))
            setattr(func, DATA_LIST_DRIVER, values)
        else:
            raise Exception("不为列表")
        return func
    return wrapper



def serialization(*dict_data):
    """
    进行接收一组字典类型
    :param data:
    :return:
    """

    def wrapper(func):
        if _check_dict(dict_data):
            global index_len
            index_len = len(str(len(dict_data)))
            setattr(func, DATA_DICT_DRIVER, dict_data)
        else:
            raise Exception("不为字典类型")
        return func
    return wrapper


# def set_char():
#     char("1","2","3")

# def extends(data:list):
#     """
#     接收一组元组数据数据
#     :param data:
#     :return:
#     """
#     global index_len
#     index_len = len(str(len(data)))
#     return add_data(data)


class FileData:

    def __init__(self,):
        pass


    @classmethod
    def text(self,file,model=";"):
        """
        对文本文件中的内容进行读取并且进行参数化操作
        :param file:
        :param log:
        :return:
        """
        with open(file=file,mode="r",encoding="utf-8") as text:
            jdata = text.readlines()

        _data = []
        for i,v in enumerate(jdata):
            c = v.rstrip("\n")
            s = c.split(model)
            _data.append(s)

        def wrapper(func):
            if _check_type(_data):
                global index_len
                index_len = len(str(len(_data)))
                setattr(func, DATA_LIST_DRIVER, _data)
            else:
                raise Exception("不为列表")
            return func

        return wrapper


    def ini(self,file,log=";"):
        pass

    @classmethod
    def json(self,file):
        with open(file, 'r',encoding="utf-8") as f:
            json_data = json.load(f)

        def wrapper(func):
            if _check_dict(json_data):
                global index_len
                index_len = len(str(len(json_data)))
                setattr(func, DATA_DICT_DRIVER, json_data)
            else:
                raise Exception("不为json")
            return func

        return wrapper

    @classmethod
    def xml(self,file):

        xml_data = xml_json_loader(file)
        print(type(xml_data))
        # with open(file, 'r',encoding="utf-8") as f:
        #     json_data = json.load(f)

        def wrapper(func):
            # if check_dict(xml_data):
            global index_len
            index_len = len(str(len(xml_data)))
            setattr(func, DATA_DICT_DRIVER, xml_data)
            # else:
            #     raise Exception("不为json")
            return func

        return wrapper

    @classmethod
    def yaml(self,file):

        yaml_data = SvelteYaml().load(file)

        def wrapper(func):
            # if check_dict(xml_data):
            global index_len
            index_len = len(str(len(yaml_data)))
            # setattr(func, DATA_DICT_DRIVER, yaml_data)
            setattr(func, DATA_DICT_DRIVER, yaml_data)
            # else:
            #     raise Exception("不为json")
            return func

        return wrapper



def mysql(table=None):

    if table is None:
        raise  Exception("请指定需要驱动的数据库表")

    else:

        data_mysql = mysql_db().all(table=table)
        print("===data_mysql=>",list(data_mysql))

        def wrapper(func):

            global index_len
            index_len = len(str(len(data_mysql)))
            setattr(func, DATA_DICT_DRIVER, data_mysql)

            return func

        return wrapper



#
#
# a = {
#     "user_info": {
#         "id": 12,
#         "name": "Tom",
#         "age": 12,
#         "height": 160,
#         "score": 100,
#         "variance": 12
#     }
# }
#
#
# # json转xml函数
# def json_to_xml(json_str):
#     # xmltodict库的unparse()json转xml
#     # 参数pretty 是格式化xml
#     xml_str = xmltodict.unparse(json_str, pretty=1)
#     return xml_str


def generate_test_name(name, value, index=0):
    """
    生成/组装一个新的测试用例名称
    :param name: 传递的方法名
    :param value: 方法名参数
    :param index: 索引
    :return:
    """

    _index = index

    index = "{0:0{1}}".format(index + 1, index_len)

    if isinstance(value,int) or isinstance(value,str) or isinstance(value,bool):


        try:
            value = str(value)
        except UnicodeEncodeError:
            # 为兼容 python 2
            value = value.encode('ascii', 'backslashreplace')

        return "{0}_{1}".format(name, index)

    if isinstance(value,dict):
        # 数据为字典类型
        try:
            value = value["title"]  # case_name作为value值
        except:
            value = _index + 1

            # print("在使用json或dict类型时你需要在你的数据中带有 key 为title的元素")
            # raise Exception()

    # 其他
    if isinstance(value,list) or isinstance(value,tuple):
        # 如果为list则进行去元素的第一个值进行作为测试用例的名称

        test_name = "{0}_{1}_{2}".format(name, index, value[0])

        return test_name


    test_name = "{0}_{1}".format(name, value)

    return test_name


def set_testcase_data(func, newName, case_docs, *args, **kwargs):
    """
    为每个测试用例提供测试数据
    :param func:
    :param new_name:
    :param test_data_docstring:
    :param args:
    :param kwargs:
    :return:
    """

    @wraps(func)
    def wrapper(self):

        return func(self,*args, **kwargs)
    # 进行获取新的测试用例名
    wrapper.__name__ = newName



    # 被包装的测试方法
    wrapper.__wrapped__ = func
    # 如果存在被包装的方法就设置 方法的文档描述

    # 如果测试方法没有设置描述
    if case_docs is not None:
        wrapper.__doc__ = case_docs
    else:
        pass
        # 如果测试用例方法有存在描述信息
        # If the test case method has an existing description
        if func.__doc__:
            try:
                wrapper.__doc__ = func.__doc__.format(*args, **kwargs)
            except (IndexError, KeyError):
                pass

    return wrapper





def add_test(cls, test_name, test_docstring, func, *args, **kwargs):
    """
    向这个类添加一个测试用例。
    该测试将基于一个现有的功能，但将给它一个新的
    :param cls: 用例类实例
    :param test_name: 用例生成的新名称
    :param test_docstring: 用例描述
    :param func: 测试用例实例方法
    :param args: 数据参数
    :param kwargs:
    :return:
    """

    # 设置测试用例方法到当前的测试用例类中
    # Sets the test case method into the current test case class

    setattr(cls, test_name, set_testcase_data(func, test_name, test_docstring,
            *args, **kwargs))


def _add_tests_from_data(cls, name, func, data):
    """
    Add tests from data loaded from the data file into the class
    """
    for i, elem in enumerate(data):
        if isinstance(data, dict):
            key, value = elem, data[elem]
            test_name = generate_test_name(name, key, i)
        elif isinstance(data, list):
            value = elem
            test_name = generate_test_name(name, value, i)
        if isinstance(value, dict):
            add_test(cls, test_name, test_name, func, **value)
        else:
            add_test(cls, test_name, test_name, func, value)


def parameterized(arg=None, **kwargs):
    """

    :param arg:
    :param kwargs:
    :return:
    """

    def wrapper(cls):
        """

        :param cls: 拿到被装饰的类实例
        :return:
        """
        # cls.__dict__.items() 将类中的属性已列表返回可迭代对象

        for name, func in list(cls.__dict__.items()):

            # 将可迭代对象转换成列表
            # 再进行遍历分解每一个列表元素得到 方法名称及方法实例

            # 进行判断当前的方法中是否被 DATA_LIST_DRIVER 装饰
            if hasattr(func, DATA_DICT_DRIVER):

                for i, v in enumerate(getattr(func, DATA_DICT_DRIVER)):


                    test_name = generate_test_name(name, getattr(v, "__name__", v), i,)

                    test_data_docstring = func.__doc__
                    if isinstance(v, tuple) or isinstance(v, list):

                        add_test(cls, test_name, test_data_docstring, func, *v)

                    else:

                        add_test(cls, test_name, test_data_docstring, func, **v)
                delattr(cls, name)


            elif hasattr(func, DATA_LIST_DRIVER):
                for i, v in enumerate(getattr(func, DATA_LIST_DRIVER)):

                    setattr(func, UNPACK_DRVER, True)
                    test_name = generate_test_name(name, getattr(v, "__name__", v), i, )
                    test_data_docstring = func.__doc__
                    if  isinstance(v, tuple) or isinstance(v, list):
                        add_test(cls, test_name, test_data_docstring, func, *v)
                delattr(cls, name)



            elif hasattr(func, DATA_DRIVER):

                # 如果被装饰就进行对给用例数据进行枚举变量
                # getattr(func, DATA_ATTR) 首先拿到数据
                for i, v in enumerate(getattr(func, DATA_DRIVER)):
                    # 进行组装测试用例名

                    test_name = generate_test_name(name, getattr(v, "__name__", v),i,)
                    test_data_docstring = func.__doc__

                    add_test(cls,test_name,test_data_docstring,func,v)

                delattr(cls, name)
        return cls

    return wrapper(arg) if inspect.isclass(arg) else wrapper

