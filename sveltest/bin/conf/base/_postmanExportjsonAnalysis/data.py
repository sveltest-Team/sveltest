#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sveltest import HttpTestCase
from sveltest import main


class T(HttpTestCase):

    def setUp(self):
        pass


    def x(self):
        self.post(
            router="",headers={},data={},env_control=False
        )


    def tearDown(self):
        pass


if __name__ == '__main__':
    main(debug=True)
