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


import unittest
from typing import NoReturn

class TestCase(unittest.TestCase):

    def start_class(self) -> NoReturn:
        """"""
        pass

    def end_class(self) -> NoReturn:
        """
        """
        pass

    @classmethod
    def setUpClass(cls) -> NoReturn:
        cls().start_class()

    @classmethod
    def tearDownClass(cls) -> NoReturn :
        cls().end_class()


    def setUp(self) -> NoReturn :
        pass

    def tearDown(self) -> NoReturn :
        pass



