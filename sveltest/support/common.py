#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/8/23



import os

from sveltest.support import Log4J


log4j = Log4J()
var = ""


import random


def getID(index=8):
    """
    用于生成随机字符串
    :param index:
    :return:
    """
    id = ''

    var = '0123456789zxcvbnmasdfghjklqwertyuiopPOIUYTREWQASDFGHJKLMNBVCXZ'

    for i in range(index):
        name = random.choice(var)
        id = name+id

    return id


def is_dir(path):
    """
    判断是否为文件夹
    :param path:
    :return:
    """
    p = os.path.splitext(path)
    if p[0]:
        return True
    else:
        return False


import difflib


# TODO : 文本检查结果
class DiffLibPush:
    def __init__(self):
        pass

    def diff_context(self,a,b):
        """

        :param a:
        :param b:
        :return:
        """

        return difflib.context_diff(a, b)


    def diff_matcher_ratio(self,str1, str2):
        """比较差异的精度比例"""
        return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


    def diff_matcher(self,str1, str2):
        """比较差异的精度比例"""
        return difflib.SequenceMatcher(None, str1, str2).get_opcodes()


    def diff_matcher_format(self,reality, expect):
        """格式化对比
            equal:相同
            replace:被取代
            (tag, i1, i2, j1, j2)，其中tag表示动作，i1表示序列a的开始位置，i2表示序列a的结束位置，j1表示序列b的开始位置，j2表示序列b的结束位置。
            reality:实际 expect 预期
        """
        log4j.info(msg="实际文本内容为: %s,期望文本内容为: %s"%(reality,expect))
        diff_text_replace = ''
        result = []
        _diff =  difflib.SequenceMatcher(None, reality, expect).get_opcodes()
        text_cum = 0 #记录的是哪些存在差异的字符串数
        for tag,i1,i2,j1,j2 in _diff:
            if tag != "equal":
                log4j.info(msg="%s 实际文本结果:[%s]__期望文本结果:[%s][%d:%d]_[%s] obj2:[%s:%s]_[%s]" \
                                    ""%(tag,reality,expect,i1,i2,reality[i1:i2],j1,j2,expect[j1:j2]))
                # diff_text_replace = "%s 实际文本结果:[%s]__期望文本结果:[%s][%d:%d]_[%s] obj2:[%s:%s]_[%s]" \
                #                     ""%(tag,reality,expect,i1,i2,reality[i1:i2],j1,j2,expect[j1:j2])
                if i1 - i2 != 0 or j1 -j2 != 0:
                    result.append(reality[i1:i2]) # 将实际文本中的字符与期望字符中不存在的字符进行保存到result列表中
                    result.append(expect[j1:j2]) # 将期望文本中的字符与实际字符中不存在的字符进行保存到result列表中
                    text_cum += 1


        # text_cum 为0证明文本没有出现差异字符 其他均为有存在差异字符
        if text_cum == 0:
            log4j.info(msg="本次检测识别结果未发现存在差异字符")
            return 0
        else:
            log4j.info(msg="本次检测识别出%s个字符存在差异"%len("".join(result)))
            log4j.info(msg="差异字符为 %s"%"".join(result))
        return result


class ObjectDict(dict):

    def __getattr__(self, key):
        if key not in self:
            return None
        else:
            value = self[key]
            if isinstance(value,dict):
                value = ObjectDict(value)
            return value
