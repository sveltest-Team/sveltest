#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/6/17
import time

from selenium.webdriver.common.keys import Keys

from sveltest.components.web.base import PageBase
from sveltest.components.web.sume import (Keys_Home,Keys_Back_Space,Keys_Space,Keys_Tab,Keys_Escape,Keys_Enter,
                                      Keys_Ctrl_A,Keys_Ctrl_C,Keys_Ctrl_X,Keys_Ctrl_V)
class WebKeys(PageBase):


    # def __init__(self):
    #     super(WebKeys,self).__init__(self)

    F1 = Keys.F1
    F2 = Keys.F2
    F3 = Keys.F3
    F4 = Keys.F4
    F5 = Keys.F5
    F6 = Keys.F6
    F7 = Keys.F7
    F8 = Keys.F8
    F9 = Keys.F9
    F10 = Keys.F10
    F11 = Keys.F11
    F12 = Keys.F12


    def home(self,by,val):
        """
        :param by:
        :param val:
        :return:
        """
        return self.page_(by=by,element=val).send_keys(Keys_Home)

    def text_del(self,by,val):
        return self.page_(by=by,element=val).send_keys(Keys_Back_Space)

    def space(self,by,val,press=1):
        if press != 1:
            return self.page_(by=by,element=val).send_keys(Keys_Space * press)
            # return [self.element(by=by,ele=val).send_keys(Keys_Space) for x in range(press)]

        return self.page_(by=by,element=val).send_keys(Keys_Space)

    def tab(self,by,val):
        """
        tab键
        :param by:
        :param val:
        :return:
        """
        return self.page_(by=by,element=val).send_keys(Keys_Tab)

    def esc(self,by,val):
        """

        """
        return self.page_(by=by,element=val).send_keys(Keys_Escape)

    def enter(self,by,val):
        """

        """
        return self.page_(by=by,element=val).send_keys(Keys_Enter)

    def cla(self,by,val):
        """

        """
        return self.page_(by=by,element=val).send_keys(Keys_Ctrl_A)

    def cp(self,by,val):
        return self.page_(by=by,element=val).send_keys(Keys_Ctrl_C)

    def skr(self,by,val):
        return self.page_(by=by,element=val).send_keys(Keys_Ctrl_X)

    def ske(self,by,val):
        return self.page_(by=by,element=val).send_keys(Keys_Ctrl_V)

    def func(self,f,by=None,val=None):
        return self.page_(by=by, element=val).send_keys(f)







import json



class Cookies(PageBase):

    def get_cookies(self,url=None,path=None,timeout=20):
        self.driver.set_page_load_timeout(timeout)#限制页面加载时间
        self.driver.set_script_timeout(timeout)#限制JavaScript加载时间
        try:
            self.driver.get(url)
        except:
            self.driver.execute_script("window.stop()")
        time.sleep(5)
        input("请登录后按Enter")
        cookies = self.driver.get_cookies()
        print("cookies",cookies)
        jsonCookies = json.dumps(cookies)

        if path:
            path_file = path
        else:
            path_file = "cookies.txt"

        with open(path_file,"w",encoding="utf-8") as f:
            f.write(jsonCookies)
        time.sleep(5)
        self.driver.quit()

    def cookie_login(self,path,url=None,timeout=20):
        self.driver.set_page_load_timeout(timeout)  # 限制页面加载时间
        self.driver.set_script_timeout(timeout)  # 限制JavaScript加载时间
        try:
            self.driver.get(url)
        except:            self.driver.execute_script("window.stop()")
        f1 = open(path)
        cookies = f1.read()
        cookies = json.loads(cookies)
        for co in cookies:
            self.driver.add_cookie(co)
        self.driver.refresh()


class By(object):
    """
    Set of supported locator strategies.
    """

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
