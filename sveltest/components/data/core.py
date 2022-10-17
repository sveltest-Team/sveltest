#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|
"""

import yaml


#
class SvelteYaml:
    """

    """
    def load(self,file):
        dt = open(file, "r", encoding="utf-8")
        return yaml.load(dt.read(), Loader=yaml.FullLoader)

import configparser
config = configparser.ConfigParser() # 类实例化




class TypeDict(dict):

    def __init__(self, **kv):

        super(TypeDict, self).__init__(**kv)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Model has not key %s" % key)

    def __setattr__(self, key, value):
        self[key] = value




class DictPlus(dict):
    """

    """
    def __init__(self, d=None):
        if d is not None:
            for k,v in d.items():
                self[k] = v
        super().__init__()

    def __key(self, key):
        return "" if key is None else key.lower()

    def __str__(self):
        import json
        return json.dumps(self)

    def __setattr__(self, key, value):
        self[self.__key(key)] = value

    def __getattr__(self, key):
        return self.get(self.__key(key))

    def __getitem__(self, key):
        return super().get(self.__key(key))

    def __setitem__(self, key, value):
        return super().__setitem__(self.__key(key), value)


class EasyDict(dict):
    """
    Get attributes

    >>> d = EasyDict({'foo':3})
    >>> d['foo']
    3
    >>> d.foo
    3
    >>> d.bar
    Traceback (most recent call last):
    ...
    AttributeError: 'EasyDict' object has no attribute 'bar'

    Works recursively

    >>> d = EasyDict({'foo':3, 'bar':{'x':1, 'y':2}})
    >>> isinstance(d.bar, dict)
    True
    >>> d.bar.x
    1

    Bullet-proof

    >>> EasyDict({})
    {}
    >>> EasyDict(d={})
    {}
    >>> EasyDict(None)
    {}
    >>> d = {'a': 1}
    >>> EasyDict(**d)
    {'a': 1}

    Set attributes

    >>> d = EasyDict()
    >>> d.foo = 3
    >>> d.foo
    3
    >>> d.bar = {'prop': 'value'}
    >>> d.bar.prop
    'value'
    >>> d
    {'foo': 3, 'bar': {'prop': 'value'}}
    >>> d.bar.prop = 'newer'
    >>> d.bar.prop
    'newer'


    Values extraction

    >>> d = EasyDict({'foo':0, 'bar':[{'x':1, 'y':2}, {'x':3, 'y':4}]})
    >>> isinstance(d.bar, list)
    True
    >>> from operator import attrgetter
    >>> map(attrgetter('x'), d.bar)
    [1, 3]
    >>> map(attrgetter('y'), d.bar)
    [2, 4]
    >>> d = EasyDict()
    >>> d.keys()
    []
    >>> d = EasyDict(foo=3, bar=dict(x=1, y=2))
    >>> d.foo
    3
    >>> d.bar.x
    1

    Still like a dict though

    >>> o = EasyDict({'clean':True})
    >>> o.items()
    [('clean', True)]

    And like a class

    >>> class Flower(EasyDict):
    ...     power = 1
    ...
    >>> f = Flower()
    >>> f.power
    1
    >>> f = Flower({'height': 12})
    >>> f.height
    12
    >>> f['power']
    1
    >>> sorted(f.keys())
    ['height', 'power']

    update and pop items
    >>> d = EasyDict(a=1, b='2')
    >>> e = EasyDict(c=3.0, a=9.0)
    >>> d.update(e)
    >>> d.c
    3.0
    >>> d['c']
    3.0
    >>> d.get('c')
    3.0
    >>> d.update(a=4, b=4)
    >>> d.b
    4
    >>> d.pop('a')
    4
    >>> d.a
    Traceback (most recent call last):
    ...
    AttributeError: 'EasyDict' object has no attribute 'a'
    """
    def __init__(self, d=None, **kwargs):
        if d is None:
            d = {}
        if kwargs:
            d.update(**kwargs)
        for k, v in d.items():
            setattr(self, k, v)
        # Class attributes
        for k in self.__class__.__dict__.keys():
            if not (k.startswith('__') and k.endswith('__')) and not k in ('update', 'pop'):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if isinstance(value, (list, tuple)):
            value = [self.__class__(x)
                     if isinstance(x, dict) else x for x in value]
        elif isinstance(value, dict) and not isinstance(value, self.__class__):
            value = self.__class__(value)
        super(EasyDict, self).__setattr__(name, value)
        super(EasyDict, self).__setitem__(name, value)

    __setitem__ = __setattr__

    def update(self, e=None, **f):
        d = e or dict()
        d.update(f)
        for k in d:
            setattr(self, k, d[k])

    def pop(self, k, d=None):
        delattr(self, k)
        return super(EasyDict, self).pop(k, d)




# TODO :已完成 待测试
# v1.0
# guanfl
# 20210528
class TkJson:
    def __init__(self):
        pass
    #转化字典
    def dict(self,data):
        return json.loads(data)

    #读取json文件中转化字典
    def json_file(self,file):
        jsObj = json.load(open(file,encoding="utf-8"))
        return jsObj

    #转换成json字符串
    def tkjson(self,data):
        return json.dumps(data)


    #将python数据类型文件转换成json文件数据
    def dict_json_file(self,data,file):
        with open(file,"w",encoding="utf-8") as f:
            return json.dump(data,f,indent=2)

    #不以ascii编码
    def json_cn(self,data):
        return json.dumps(data,ensure_ascii=False,indent=2)

    #不以ascii编码 美化json格式 indent 子元素每个空格2格
    def json_cn_format(self,data):
        return json.dumps(data,ensure_ascii=False,indent=2)


    #写json文件
    def tk_json_file(self,file,data):
        with open(file,"w",encoding="utf-8") as f:
            f.write(self.json_cn_format(data=data))

import json
import xmltodict

# 定义xml转json的函数
def xml_to_json(xml_str):
    # parse是的xml解析器
    xml_parse = xmltodict.parse(xml_str)
    # json库dumps()是将dict转化成json格式,loads()是将json转化成dict格式。
    # dumps()方法的ident=1,格式化json
    json_str = json.dumps(xml_parse, indent=1)
    dict_json = json.loads(json_str)

    return dict_json

def xml_json_loader(file):
    with open(file,"r",encoding="utf-8") as f:
        xmk_ = f.read()
        f.close()
    data = xml_to_json(xmk_)
    return data
