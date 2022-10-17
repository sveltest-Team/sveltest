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
import functools
import importlib
import unittest
from fnmatch import fnmatchcase
from sveltest.bin.conf import settings
from sveltest.case import TestCase
from typing import Optional, Any, Tuple, Dict


class Loader(unittest.TestLoader):

    """
    该类负责根据各种标准加载测试并将它们封装在测试套件中返回
    """
    testNamePatterns = None

    testMethodPrefix = 'test' if settings.TEST_METHOD_PREFIX == "test" else settings.TEST_METHOD_PREFIX
    CaseListInfo = []

    def getTestCaseNames(self, testCaseClass:Optional[Any]):
        """返回在testCaseClass中找到的方法名的排序序列
        """


        def shouldIncludeMethod(attrname):
            if not attrname.startswith(self.testMethodPrefix):
                return False
            testFunc = getattr(testCaseClass, attrname)
            if not callable(testFunc):
                return False
            fullName = f'%s.%s.%s' % (
                testCaseClass.__module__, testCaseClass.__qualname__, attrname
            )
            if settings.COLLECT_STATUS:
                case_info = {"module": testCaseClass.__module__,"class": {"testcase": testCaseClass.__name__,"declare": testCaseClass.__doc__},
                    "method": {"testcase": attrname,"declare": testFunc.__doc__}}

                self.CaseListInfo.append(case_info)

            return self.testNamePatterns is None or \
                   any(fnmatchcase(fullName, pattern) for pattern in self.testNamePatterns)

        testFnNames = list(filter(shouldIncludeMethod, dir(testCaseClass)))

        if self.sortTestMethodsUsing:
            testFnNames.sort(key=functools.cmp_to_key(self.sortTestMethodsUsing))
        return testFnNames




    def load_tests_module(self, module:Optional[str],
                          *args:Optional[Tuple],
                          pattern:Optional[str]=None,
                          **kws:Optional[Dict]
                          ) -> object:
        """返回给定模块中包含的所有测试用例的集合(暂未实现)"""


        # if len(args) > 0 or 'use_load_tests' in kws:
        #     warnings.warn('use_load_tests is deprecated and ignored',
        #                   DeprecationWarning)
        #     kws.pop('use_load_tests', None)
        # if len(args) > 1:
        #     # Complain about the number of arguments, but don't forget the
        #     # required `module` argument.
        #     complaint = len(args) + 1
        #     raise TypeError('loadTestsFromModule() takes 1 positional argument but {} were given'.format(complaint))
        # if len(kws) != 0:
        #     # Since the keyword arguments are unsorted (see PEP 468), just
        #     # pick the alphabetically sorted first argument to complain about,
        #     # if multiple were given.  At least the error message will be
        #     # predictable.
        #     complaint = sorted(kws)[0]
        #     raise TypeError("loadTestsFromModule() got an unexpected keyword argument '{}'".format(complaint))

        test_module = importlib.import_module(module)

        # 存储排序好的测试用例
        tests = []
        # 进行加载当前的模块下的所有属性及方法
        for name in dir(test_module):

            obj = getattr(test_module, name)


            # 判断是否是一个对象且进行继承至testcase
            # if isinstance(obj, type) and issubclass(obj, unittest.case.TestCase) :
            if isinstance(obj, type) and issubclass(obj, TestCase) :
                # 如果被继承了那么则将这个对象加入tests列表中
                tests.append(self.loadTestsFromTestCase(obj))

        # load_tests = getattr(module, 'load_tests', None)
        # 将测试用例传入测试用例集中
        tests = self.suiteClass(tests)
        # if load_tests is not None:
        #     try:
        #         return load_tests(self, tests, pattern)
        #     except Exception as e:
        #         error_case, error_message = _make_failed_load_tests(
        #             module.__name__, e, self.suiteClass)
        #         self.errors.append(error_message)
        #         return error_case
        return tests

class PlatformOperationLoader(Loader):

    """
    用于对测试平台化的支持
    """







svelteTestLoader = Loader()
